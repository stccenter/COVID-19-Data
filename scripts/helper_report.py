#!/usr/bin/env python
# coding: utf-8

import os
import pandas as pd
import datetime
import json
from sqlalchemy import create_engine
import psycopg2
import requests
from helper import *
import io
import errno
#
ADMIN_0_TABLE = 'covid19_admin0_test'
ADMIN_1_TABLE = 'covid19_admin1_test'
ADMIN_2_TABLE = 'covid19_admin2_test'
US_POLICY_TABLE = 'covid19_usa_state_policy'
ATTRIBUTES = ['confirmed', 'death', 'recovered']


ADMIN1_Dict = {
    "Canada": "Province",
    "China": "Province",
    "Australia": "State",
    "US": "State",
    "Austria": "State",
    "Germany": "State",
    "Italy": "Region",
    "Brazil": "State",
    "Chile": "Region",
    "Russia": "Subdivisions",
    "South Africa": "Province",
    "Japan": "Prefectures",
    "Croatia": "County",
    "Sweden": "Province",
    "India": "States",
    "Hungary": "County",
    "Denmark": "Region",
    "Latvia": "County",
    "Albania": "County",
    "Haiti": "Department",
    "Romania": "County",
    "Mexico": "State",
    "Nigeria": "State",
    "Pakistan": "Province"
}

ADMIN2_Dict = {
    "US": "County",
    "China": "City",
    "Italy": "Province"
}

ATTRIBUTES_DICT = {
    "USA": ['confirmed', 'death'],
    "default": ATTRIBUTES
}

iso3_dict_csv_path = './config/iso3_dict_04_08_2020.json'
ADMIN0_ISO3 = read_iso3_dic(iso3_dict_csv_path)


def checkExist(file):
    path = os.path.dirname(os.path.abspath(file))
    if not os.path.exists(path):
        os.makedirs(path)


def record_to_timeseries_file(record_df, attribute, aggregate_key, csvfile):
    admin_df = record_df.drop(columns=['date', attribute])
    admin_df = admin_df.drop_duplicates(subset=aggregate_key, keep="first")
    admin_df.to_csv(csvfile, index=False)
    grouped = record_df.groupby('date')
    for name, group in grouped:
        tmp_df = pd.read_csv(csvfile)
        attribute_df = group[[aggregate_key, attribute]]
        attribute_df.columns = [aggregate_key, name]
        admin_df = admin_df.merge(attribute_df, on=aggregate_key, how='left')
        tmp_df[name] = admin_df[name].fillna(0).astype(int).tolist()
        admin_df = admin_df.drop(columns=[name])
        tmp_df.to_csv(csvfile, index=False, encoding='utf-8-sig')


def admin1_daily(dataDir, date, engine):
    for admin0 in ADMIN1_Dict:
        iso3 = ADMIN0_ISO3[admin0]
        admin1 = ADMIN1_Dict[admin0]
        sql = "SELECT * FROM " + ADMIN_1_TABLE + " WHERE date = '" + date
        if admin0 == "China":
            sql += "' and iso3 in ('CHN', 'TWN', 'HKG', 'MAC')"
        else:
            sql += "' and iso3 = '" + iso3 + "'"
        rocord_df = pd.read_sql_query(sql, engine)
        rocord_df.columns = ['id', 'date', 'iso3', 'country_region',
                             'hasc', admin1, 'confirmed', 'death', 'recovered']
        rocord_df = rocord_df.sort_values(by='confirmed', ascending=False)
        filename = dataDir + admin0 + '/' + admin1 + '_level_daily/' + \
            admin0 + '_' + admin1 + '_' + date + '.csv'
        checkExist(filename)
        rocord_df.to_csv(filename, columns=[
                         admin1, 'hasc', 'confirmed', 'death', 'recovered'], index=False, encoding='utf-8-sig')
        print("generate admin1 daily repor for  " +
              admin0 + " on  " + date + " successfully")


def admin2_daily(dataDir, date, engine):
    for admin0 in ADMIN2_Dict:
        iso3 = ADMIN0_ISO3[admin0]
        admin2 = ADMIN2_Dict[admin0]
        sql = "SELECT * FROM " + ADMIN_2_TABLE + " WHERE date = '" + date
        if admin0 == "China":
            sql += "' and iso3 in ('CHN', 'TWN', 'HKG', 'MAC')"
        else:
            sql += "' and iso3 = '" + iso3 + "'"

        rocord_df = pd.read_sql_query(sql, engine)
        rocord_df.columns = ['id', 'date', 'iso3', 'country_region', 'admin1_hasc',
                             'local_id1', 'hasc', 'local_id2', admin2, 'confirmed', 'death', 'admin1_name', 'recovered']
        rocord_df = rocord_df.sort_values(by='confirmed', ascending=False)
        filename = dataDir + admin0 + '/' + admin2 + '_level_daily/' + \
            admin0 + '_' + admin2 + '_' + date + '.csv'
        checkExist(filename)
        rocord_df.to_csv(filename, columns=[
                         admin2, 'hasc', 'confirmed', 'death', 'recovered'], index=False)
        print("generate admin2 daily repor for  " +
              admin0 + "on  " + date + "  successfully")


def admin2_summary(dataDir, date, engine):
    for admin0 in ADMIN2_Dict:
        iso3 = ADMIN0_ISO3[admin0]
        admin2 = ADMIN2_Dict[admin0]
        # to do, need to change after dexuan provide a complete dictionary
        if iso3 in ATTRIBUTES_DICT.keys():
            attributes = ATTRIBUTES_DICT[iso3]
        else:
            attributes = ATTRIBUTES_DICT['default']

        for attribute in attributes:
            sql = "SELECT date, admin2_hasc, admin2_name," + \
                attribute + " FROM " + ADMIN_2_TABLE
            if admin0 == "China":
                sql += " where iso3 in ('CHN', 'TWN', 'HKG', 'MAC')"
            else:
                sql += " where iso3 = '" + iso3 + "'"

            record_df = pd.read_sql_query(sql, engine)
            record_df.columns = ['date', 'hasc', admin2, attribute]
            filename = dataDir + admin0 + '/' + admin2 + '_level_summary/' + \
                admin0 + '_' + admin2 + '_summary_covid19_' + attribute + '.csv'
            if os.path.exists(filename):
                os.remove(filename)
            checkExist(filename)
            # to do, need to change to hasc after dexuan update code
            record_to_timeseries_file(record_df, attribute, 'hasc', filename)
            print("generate admin2 summary report of " +
                  attribute + " for  " + admin0 + " successfully")


def global_summary(dataDir, date, engine):
    for attribute in ATTRIBUTES:
        sql = "SELECT id, date, iso3, admin0_name, " + attribute + \
            " FROM " + ADMIN_0_TABLE + " ORDER BY admin0_name ASC"
        rocord_df = pd.read_sql_query(sql, engine)
        rocord_df.columns = ['id', 'date', 'iso3', 'admin0_name', attribute]
        cdvfile = dataDir + 'Global/country_level_summary/Global_summary_covid19_' + \
            attribute + '.csv'
        if os.path.exists(cdvfile):
            os.remove(cdvfile)
        checkExist(cdvfile)
        record_to_timeseries_file(rocord_df, attribute, 'iso3', cdvfile)
        print("generate global " + attribute + " summary report successfully")


def admin1_summary(dataDir, date, engine):
    for admin0 in ADMIN1_Dict:
        iso3 = ADMIN0_ISO3[admin0]
        admin1 = ADMIN1_Dict[admin0]
        if iso3 in ATTRIBUTES_DICT.keys():
            attributes = ATTRIBUTES_DICT[iso3]
        else:
            attributes = ATTRIBUTES_DICT['default']

        for attribute in attributes:
            sql = "SELECT id, date, admin1_hasc, admin1_name," + \
                attribute + " FROM " + ADMIN_1_TABLE
            if admin0 == "China":
                sql += " where iso3 in ('CHN', 'TWN', 'HKG', 'MAC')"
            else:
                sql += " where iso3 = '" + iso3 + "'"

            record_df = pd.read_sql_query(sql, engine)
            record_df.columns = ['id', 'date', 'hasc', admin1, attribute]

            filename = dataDir + admin0 + '/' + admin1 + '_level_summary/' + \
                admin0 + '_' + admin1 + '_summary_covid19_' + attribute + '.csv'
            checkExist(filename)
            # to do, need to change admin1 to hasc after dexuan update code
            record_to_timeseries_file(record_df, attribute, admin1, filename)
            print("generate admin1 summary report of " +
                  attribute + " for  " + admin0 + " successfully")


def admin2_summary(dataDir, date, engine):
    for admin0 in ADMIN2_Dict:
        iso3 = ADMIN0_ISO3[admin0]
        admin2 = ADMIN2_Dict[admin0]
        # to do, need to change after dexuan provide a complete dictionary
        if iso3 in ATTRIBUTES_DICT.keys():
            attributes = ATTRIBUTES_DICT[iso3]
        else:
            attributes = ATTRIBUTES_DICT['default']

        for attribute in attributes:
            sql = "SELECT id, date, admin2_hasc, admin2_name," + \
                attribute + " FROM " + ADMIN_2_TABLE
            if admin0 == "China":
                sql += " where iso3 in ('CHN', 'TWN', 'HKG', 'MAC')"
            else:
                sql += " where iso3 = '" + iso3 + "'"

            record_df = pd.read_sql_query(sql, engine)
            record_df.columns = ['id', 'date', 'hasc', admin2, attribute]
            filename = dataDir + admin0 + '/' + admin2 + '_level_summary/' + \
                admin0 + '_' + admin2 + '_summary_covid19_' + attribute + '.csv'
            if os.path.exists(filename):
                os.remove(filename)
            checkExist(filename)
            record_to_timeseries_file(record_df, attribute, 'hasc', filename)
            print("generate admin2 summary report of " +
                  attribute + " for  " + admin0 + " successfully")


def global_daily(dataDir, date, engine):
    sql = "SELECT * FROM " + ADMIN_0_TABLE + " WHERE date = '" + date + "'"
    rocord_df = pd.read_sql_query(sql, engine)
    rocord_df.columns = ['id', 'date', 'iso3', 'admin0_name',
                         'confirmed', 'death', 'recovered', 'temperature', 'humidity']
    rocord_df = rocord_df.rename(columns={'admin0_name': 'country_region'})
    rocord_df = rocord_df.sort_values(by='confirmed', ascending=False)
    filename = dataDir + 'Global/country_level_daily/Global_' + date + '.csv'
    if os.path.exists(filename):
        os.remove(filename)
    checkExist(filename)
    rocord_df.to_csv(filename,
                     columns=['country_region', 'iso3', 'confirmed', 'death', 'recovered'], index=False)
    print("generate historical global daily report  on " + date + " successfully")
