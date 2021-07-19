import os
import pandas as pd
import datetime
import json
from sqlalchemy import create_engine
import psycopg2
import requests
import errno
from helper_report import *
from helper import *
import time

# Main Start
conn_string = 'postgresql://' + os.getenv('DB_USER') + ':' + os.getenv('DB_PASSWORD') + \
    '@' + os.getenv('DB_HOST') + ':' + os.getenv('DB_PORT') + \
    '/' + os.getenv('DB_DATABASE')

engine = create_engine(conn_string)
dbConnection = engine.connect()


# Main Start


outputDir = "./"
#yesterday variable
yesterday = datetime.date.today() - datetime.timedelta(days=3)
admin1_daily(outputDir, str(yesterday), engine)
admin1_summary(outputDir, str(yesterday), engine)

global_daily(outputDir, str(yesterday), engine)
global_summary(outputDir, str(yesterday), engine)

admin2_daily(outputDir, str(yesterday), engine)
admin2_summary(outputDir, str(yesterday), engine)


dbConnection.close()
engine.dispose()

## Main End#
