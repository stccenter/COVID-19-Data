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

# Function definition start


def read_iso3_dic(path):
    file = open(path, 'r')
    js = file.read()
    iso3_dict = json.loads(js)
    file.close()
    return iso3_dict


def get_key(dict, value):
    return [k for k, v in dict.items() if v == value]


def return_iso3(x, iso3_dict):
    if x not in iso3_dict.keys():
        return None
    return iso3_dict[x]


def fixed_admin0_CHN(x, y):
    CHN_sub_list = ['Hong Kong',
                    'Macau',
                    'Guam',
                    'Puerto Rico',
                    'Virgin Islands',
                    'Northern Mariana Islands']
    if x in CHN_sub_list:
        return x
    else:
        return y


def extract_admin0_JHU(daily_time, iso3_dict_csv_path, case_df):
    region_column_name = 'Country_Region'
    state_column_name = 'Province_State'
    # get case country name list and find the iso3 based on defined standard table
    iso3_dict = read_iso3_dic(iso3_dict_csv_path)
    case_df[region_column_name] = case_df.apply(lambda row: fixed_admin0_CHN(
        row[state_column_name], row[region_column_name]), axis=1)
    case_admin0_df = case_df.groupby(
        region_column_name).agg('sum').reset_index()
    case_admin0_df['date'] = daily_time
    case_admin0_df['iso3'] = case_admin0_df.apply(
        lambda row: return_iso3(row[region_column_name], iso3_dict), axis=1)
    case_admin0_df['temperature'] = None
    case_admin0_df['humidity'] = None

    stcenter_admin0 = case_admin0_df[["date", "iso3", region_column_name,
                                      "Confirmed", "Deaths", "Recovered", "temperature", "humidity"]]

    # rename to table schema and data format
    key_dict = {
        region_column_name: "admin0_name",
        "Confirmed": "confirmed",
        "Deaths": "deaths",
        "Recovered": "recovered"
    }
    stcenter_admin0 = stcenter_admin0.rename(columns=key_dict)

    stcenter_admin0.confirmed = stcenter_admin0.confirmed.astype(int)
    stcenter_admin0.deaths = stcenter_admin0.deaths.astype(int)
    stcenter_admin0.recovered = stcenter_admin0.recovered.astype(int)

    stcenter_admin0 = stcenter_admin0.drop_duplicates(['iso3'])

    return stcenter_admin0


# In[6]:

def return_hasc1(admin1_table, x):
    if x not in admin1_table.NAME_1.tolist():
        return None
    return (admin1_table[admin1_table['NAME_1'] == x].HASC_1).tolist()[0]


def return_fixed_hasc1(x, y):
    admin1_dict = {'Quebec': 'CA.QC',
                   'Hong Kong': 'HKG',
                   'Inner Mongolia': 'CN.NM',
                   'Macau': 'MAC',
                   'Ningxia': 'CN.NX',
                   'Tibet': 'CN.XZ',
                   'Xinjiang': 'CN.XJ',
                   'Guam': 'GUM',
                   'Puerto Rico': 'PRI',
                   'Virgin Islands': 'VIR',
                   'Northern Mariana Islands': 'MNP'}
    dict_key_list = [*admin1_dict]
    if x in dict_key_list:
        if '.' in (admin1_dict[x]):
            return (admin1_dict[x])
    else:
        return y


def return_fixed_iso3(x, y):
    admin1_dict = {'Quebec': 'CA.QC',
                   'Hong Kong': 'HKG',
                   'Inner Mongolia': 'CN.NM',
                   'Macau': 'MAC',
                   'Ningxia': 'CN.NX',
                   'Tibet': 'CN.XZ',
                   'Xinjiang': 'CN.XJ',
                   'Guam': 'GUM',
                   'Puerto Rico': 'PRI',
                   'Virgin Islands': 'VIR',
                   'Northern Mariana Islands': 'MNP'}
    dict_key_list = [*admin1_dict]
    if x in dict_key_list:
        if len(admin1_dict[x]) == 3:
            return (admin1_dict[x])
        else:
            return y
    else:
        return y


def return_fixed_admin0_name(x, y):
    admin1_dict = {'Quebec': 'CA.QC',
                   'Hong Kong': 'HKG',
                   'Inner Mongolia': 'CN.NM',
                   'Macau': 'MAC',
                   'Ningxia': 'CN.NX',
                   'Tibet': 'CN.XZ',
                   'Xinjiang': 'CN.XJ',
                   'Guam': 'GUM',
                   'Puerto Rico': 'PRI',
                   'Virgin Islands': 'VIR',
                   'Northern Mariana Islands': 'MNP'}
    dict_key_list = [*admin1_dict]
    if x in dict_key_list:
        if len(admin1_dict[x]) == 3:
            return (x)
        else:
            return y
    else:
        return y


def extract_admin1_JHU(daily_time, output_path, case_df, iso3='USA'):
    region_column_name = 'Country_Region'
    state_column_name = 'Province_State'
    # get case country name list and find the iso3 based on defined standard table
    iso3_dict = read_iso3_dic("./config/iso3_dict_04_08_2020.json")
    admin0_name_list = get_key(iso3_dict, iso3)

    admin1_df = case_df[case_df[region_column_name].isin(admin0_name_list)]
    admin1_df[state_column_name][admin1_df[region_column_name]
                                 == 'Taiwan*'] = 'Taiwan'
    admin1_df[state_column_name][admin1_df[state_column_name]
                                 == 'London, ON'] = 'Ontario'
    admin1_df[state_column_name][admin1_df[state_column_name]
                                 == 'Toronto, ON'] = 'Ontario'
    admin1_df[state_column_name][admin1_df[state_column_name]
                                 == ' Montreal, QC'] = 'Quebec'

    admin1_df = admin1_df.groupby(state_column_name).agg('sum').reset_index()
    admin1_df = admin1_df[[state_column_name,
                           'Confirmed', 'Deaths', 'Recovered']]
    admin1_df['date'] = daily_time
    admin1_df['iso3'] = iso3
    admin1_df['admin0_name'] = admin0_name_list[0]

    key_dict = {
        state_column_name: 'admin1_name',
        "Confirmed": "confirmed",
        "Deaths": "death",
        "Recovered": "recovered"
    }
    admin1_df = admin1_df.rename(columns=key_dict)

    admin1_df.confirmed = admin1_df.confirmed.astype(int)
    admin1_df.death = admin1_df.death.astype(int)
    admin1_df.recovered = admin1_df.recovered.astype(int)

    admin1_table = pd.read_csv('./config/admin1_name.csv')
    admin1_table = admin1_table[admin1_table['GID_0'] == iso3]

    if len(admin1_df) > 0:
        admin1_df['admin1_hasc'] = admin1_df.apply(
            lambda row: return_hasc1(admin1_table, row['admin1_name']), axis=1)
        admin1_df['admin1_hasc'] = admin1_df.apply(
            lambda row: return_fixed_hasc1(row['admin1_name'], row['admin1_hasc']), axis=1)
        admin1_df['iso3'] = admin1_df.apply(
            lambda row: return_fixed_iso3(row['admin1_name'], row['iso3']), axis=1)
        admin1_df['admin0_name'] = admin1_df.apply(lambda row: return_fixed_admin0_name(
            row['admin1_name'], row['admin0_name']), axis=1)

    # change colume order
        admin1_df = admin1_df[['date', 'iso3', 'admin0_name',
                               'admin1_hasc', 'admin1_name', 'confirmed', 'death', 'recovered']]

    return admin1_df


def fetchgit(url: str, GITHUB_USER: str, GITHUB_PASSWRD: str):
    downloaded_csv = pd.DataFrame()
    download = github_session = None
    github_session = requests.Session()
    github_session.auth = (GITHUB_USER, GITHUB_PASSWRD)
    download = github_session.get(url).content
    downloaded_csv = pd.read_csv(io.StringIO(
        download.decode('utf-8')), error_bad_lines=False)
    return downloaded_csv


# https://raw.githubusercontent.com/stevenliuyi/covid19-csv/master/csv/admin1_2020-05-01.csv

# Function definition end
