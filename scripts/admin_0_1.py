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

# Main function start

output_path = './'
iso3_dict_csv_path = './config/iso3_dict_04_08_2020.json'
##yesterday variable
yesterday = datetime.date.today() - datetime.timedelta(days=41)
raw_url_path = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/'
raw_url = raw_url_path + yesterday.strftime("%m-%d-%Y") + '.csv'
case_df = pd.read_csv(raw_url)


conn_string = 'postgresql://' + os.getenv('DB_USER') + ':' + os.getenv('DB_PASSWORD') + \
    '@' + os.getenv('DB_HOST') + ':' + os.getenv('DB_PORT') + \
    '/' + os.getenv('DB_DATABASE')
engine = create_engine(conn_string)

dbConnection = engine.connect()


# In[8]:
daily_df = extract_admin0_JHU(yesterday.strftime(
    "%Y-%m-%d"), iso3_dict_csv_path, case_df)
daily_df.rename(columns={'deaths': 'death'}, inplace=True)
daily_df.to_sql('covid19_admin0_test', dbConnection,
                if_exists="append", index=False)

stc_admin1_iso3_list = ['CHN', 'CAN', 'AUS']
stc_admin1_init = pd.DataFrame()

for iso3 in stc_admin1_iso3_list:
    case_df = pd.read_csv(raw_url)
    out_df = extract_admin1_JHU(yesterday.strftime(
        "%Y-%m-%d"), output_path, case_df, iso3=iso3)
    stc_admin1_init = stc_admin1_init.append(out_df)
stc_admin1_init.to_sql('covid19_admin1_test', dbConnection,
                       if_exists="append", index=False)


dbConnection.close()
engine.dispose()

# Main function end
