import os
import time
import sys
import pymysql
from time import strftime
from nestpension import NestPension

USERNAME = os.environ.get('NEST_USERNAME')
PASSWORD = os.environ.get('NEST_PASSWORD')
DB_HOST = os.environ.get('DB_HOST')
DB_USERNAME = os.environ.get('DB_USERNAME')
DB_PORT = int(os.environ.get('DB_PORT'))
DB_PASSWORD = os.environ.get('DB_PASSWORD')
DB_DATABASE = os.environ.get('DB_DATABASE')

if USERNAME is None or PASSWORD is None or DB_HOST is None:
    print("Environment variables are needed!")
    sys.exit(0)

db_create_query = """
CREATE TABLE IF NOT EXISTS nest_pension (
    Id INT AUTO_INCREMENT,
    Value DECIMAL(18,2) NOT NULL,
    RecordDateTime DATETIME NOT NULL,
    PRIMARY KEY (Id)
)
"""


def execute_query(query):
    conn = pymysql.connect(host=DB_HOST, port=DB_PORT,
                           user=DB_USERNAME, passwd=DB_PASSWORD, db=DB_DATABASE)
    cur = conn.cursor()

    cur.execute(query)

    cur.close()
    conn.commit()
    conn.close()


execute_query(db_create_query)

print("Created database")

nest = NestPension(USERNAME, PASSWORD)
nest.login()

value = nest.get_value()
print("Found value of %s" % (value))

insert_query = "INSERT INTO nest_pension (Value, RecordDateTime) values (%s, '%s')" % (
    value, strftime("%Y-%m-%d %H:%M:%S"))

execute_query(insert_query)

print("Inserted data point.")
