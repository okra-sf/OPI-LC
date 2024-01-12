# pip install python-dotenv

import os
from dotenv import load_dotenv

init_env = True

# does .env file exist?
if os.path.isfile('.env'):
  res = input("Do you want to re-initialise .env file? (y/n) ")
  if res != 'y':
    init_env = False

if init_env:
  DB_DATABASE_FILE="db.sqlite3"
  FIRST_INSCRIPTION_HEIGHT="767430"
  FIRST_BRC20_HEIGHT="779832"
  REPORT_TO_INDEXER="true"
  REPORT_URL="https://api.opi.network/report_block"
  REPORT_RETRIES="10"
  REPORT_NAME=""
  print("Initialising .env file")
  print("leave blank to use default values")
  res = input("BRC20 SQLite3 DB file name (Default: db.sqlite3): ")
  if res != '':
    DB_DATABASE_FILE = res
  res = input("First inscription height (Default: 767430) leave default for correct hash reporting: ")
  if res != '':
    FIRST_INSCRIPTION_HEIGHT = res
  res = input("First brc20 height (Default: 779832) leave default for correct hash reporting: ")
  if res != '':
    FIRST_BRC20_HEIGHT = res
  res = input("Report to main indexer (Default: true): ")
  if res != '':
    REPORT_TO_INDEXER = res
  if REPORT_TO_INDEXER == 'true':
    res = input("Report URL (Default: https://api.opi.network/report_block): ")
    if res != '':
      REPORT_URL = res
    res = input("Report retries (Default: 10): ")
    if res != '':
      REPORT_RETRIES = res
    while True:
      res = input("Report name: ")
      if res != '':
        REPORT_NAME = res
        break
      else:
        print('Report name cannot be empty')
  f = open('.env', 'w')
  f.write("DB_DATABASE_FILE=\""+DB_DATABASE_FILE+"\"\n")
  f.write("FIRST_INSCRIPTION_HEIGHT=\""+FIRST_INSCRIPTION_HEIGHT+"\"\n")
  f.write("FIRST_BRC20_HEIGHT=\""+FIRST_BRC20_HEIGHT+"\"\n")
  f.write("REPORT_TO_INDEXER=\""+REPORT_TO_INDEXER+"\"\n")
  f.write("REPORT_URL=\""+REPORT_URL+"\"\n")
  f.write("REPORT_RETRIES=\""+REPORT_RETRIES+"\"\n")
  f.write("REPORT_NAME=\""+REPORT_NAME+"\"\n")
  f.close()
