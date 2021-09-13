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

# Main Start
conn_string = 'postgresql://' + os.getenv('DB_USER') + ':' + os.getenv('DB_PASSWORD') + \
    '@' + os.getenv('DB_HOST') + ':' + os.getenv('DB_PORT') + \
    '/' + os.getenv('DB_DATABASE')
engine = create_engine(conn_string)

dbConnection = engine.connect()
# Main Start

output_path = './'
yesterday = datetime.date.today() - datetime.timedelta(days=2)
url1 = "https://raw.githubusercontent.com/stevenliuyi/covid19-csv/master/csv/admin1_" + \
    yesterday.strftime("%Y-%m-%d") + ".csv?token=AFNE5H7EAI7XIHTT53C24N3BJDWIS"
url2 = "https://raw.githubusercontent.com/stevenliuyi/covid19-csv/master/csv/admin2_" + \
    yesterday.strftime("%Y-%m-%d") + ".csv?token=AFNE5HYX6RFRDO4NJINL2Z3BJDWJ4"


GITHUB_USER = os.getenv('USERNAME')
GITHUB_PASSWRD = os.getenv('PASSWD')
url1_df = fetchgit(url1, GITHUB_USER, GITHUB_PASSWRD)
country_list = [
    'Austria',
    'Brazil',
    'Chile',
    'Germany',
    'Italy',
    'Russia',
    'South Africa',
    'Japan',
    'Croatia',
    'Sweden',
    'India',
    'Hungary',
    'Denmark',
    'Latvia',
    'Albania',
    'Haiti',
    'Romania',
    'Mexico',
    'Nigeria',
    'Pakistan'
]
upload_countries = url1_df[url1_df['admin0_name'].isin(country_list)]
upload_countries = upload_countries.drop(columns=['Unnamed: 0'])
upload_countries.loc[upload_countries['admin1_hasc']
                     == 'PK.PB', 'admin1_name'] = 'Punjab.PAK'
upload_countries.to_sql('covid19_admin1_test', dbConnection,
                        if_exists="append", index=False)
url2_df = fetchgit(url2, GITHUB_USER, GITHUB_PASSWRD)
url2_df = url2_df.drop(columns=['Unnamed: 0'])
url2_df.to_sql('covid19_admin2_test', dbConnection,
               if_exists="append", index=False)

dbConnection.close()
engine.dispose()
# Main End
