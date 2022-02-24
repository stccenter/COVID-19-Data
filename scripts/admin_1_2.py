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

# Main Start


conn_string = 'postgresql://' + os.getenv('DB_USER') + ':' + os.getenv('DB_PASSWORD') + \
    '@' + os.getenv('DB_HOST') + ':' + os.getenv('DB_PORT') + \
    '/' + os.getenv('DB_DATABASE')
engine = create_engine(conn_string)

dbConnection = engine.connect()
url1 = "https://static.usafacts.org/public/data/covid-19/covid_confirmed_usafacts.csv"
#url1 = "https://usafactsstatic.blob.core.windows.net/public/data/covid-19/covid_confirmed_usafacts.csv"
#url2 = "https://usafactsstatic.blob.core.windows.net/public/data/covid-19/covid_deaths_usafacts.csv"
url2="https://static.usafacts.org/public/data/covid-19/covid_deaths_usafacts.csv"

output_path = './'
iso3_dict_csv_path = './config/iso3_dict_04_08_2020.json'
#yesterday variable
yesterday = datetime.date.today() - datetime.timedelta(days=11)

storage_options = {'User-Agent': 'Mozilla/5.0'}

confirmed_df = pd.read_csv(
    url1, storage_options=storage_options, usecols=['countyFIPS', 'County Name', 'State', 'StateFIPS', yesterday.strftime("%Y-%m-%d")])
death_df = pd.read_csv(
    url2, storage_options=storage_options, usecols=['County Name', yesterday.strftime("%Y-%m-%d")])
confirmed_df = confirmed_df[~confirmed_df['County Name'].isin(
    ['Statewide Unallocated'])]
confirmed_df.columns = ['countyFIPS', 'county',
                        'stateAbbr', 'stateFIPS', 'confirmed']
death_df = death_df[~death_df['County Name'].isin(
    ['Statewide Unallocated'])]
death_df.columns = ['county', 'death']

result_df = pd.concat([confirmed_df, death_df], axis=1)

# Remove duplicated country column due to merge
USA_admin2 = result_df.loc[:, ~result_df.columns.duplicated()]
USA_admin2['date'] = yesterday.strftime("%Y-%m-%d")
tmp_USA_admin2 = USA_admin2
admin1_table = pd.read_csv('./config/admin1_name.csv')
USA_admin1_table = admin1_table[admin1_table['GID_0'] == 'USA']
USA_admin1_table = USA_admin1_table[['HASC_1', 'GID_0', 'NAME_0', 'NAME_1']]
USA_admin2 = USA_admin2.drop(columns=['countyFIPS', 'county', 'stateFIPS'])
USA_admin2.fillna('0')
USA_admin1_df = USA_admin2.groupby(
    ['date', 'stateAbbr']).agg('sum').reset_index()
USA_admin1_df['HASC_1'] = USA_admin1_df.apply(
    lambda row: 'US.' + row['stateAbbr'], axis=1)
USA_admin1_df = USA_admin1_df.merge(USA_admin1_table, on='HASC_1', how='left')
key_dict = {
    "HASC_1": "admin1_hasc",
    "GID_0": "iso3",
    "NAME_0": "admin0_name",
    "deaths": "death",
    "NAME_1": "admin1_name"
}
USA_admin1_df = USA_admin1_df.rename(columns=key_dict)

USA_admin1_df = USA_admin1_df[[
    'date', 'iso3', 'admin0_name', 'admin1_hasc', 'admin1_name', 'confirmed', 'death']]
USA_admin1_df.to_sql('covid19_admin1_test', dbConnection,
                     if_exists="append", index=False)


extra_data = pd.read_csv("./config/USA_admin2_HASC2_FIPS.csv")
extra_data = extra_data[["FIPS", "HASC"]]


result = pd.merge(left=extra_data, right=tmp_USA_admin2,
                  left_on='FIPS', right_on='countyFIPS', how='left')
result['iso3'] = 'USA'
result['admin0_name'] = 'United States'
result['stateAbbr'] = 'US.' + result['stateAbbr'].astype(str)

result.rename(columns={'stateAbbr': 'admin1_hasc', 'stateFIPS': 'local_id1',
                       'HASC': 'admin2_hasc', 'countyFIPS': 'local_id2', 'county': 'admin2_name'}, inplace=True)
result = result[['date', 'iso3', 'admin0_name', 'admin1_hasc', 'local_id1',
                 'admin2_hasc', 'local_id2', 'admin2_name', 'confirmed', 'death']]
result.to_sql('covid19_admin2_test', dbConnection,
              if_exists="append", index=False)

dbConnection.close()
engine.dispose()

# Main End#
