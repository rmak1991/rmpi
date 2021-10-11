#!/usr/bin/python
import os,sys, mariadb
CHANGE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(CHANGE_PATH)
from Lib.T_Global import PATHS as _P

def DBConnect():
    try:
        conn = mariadb.connect(
            user="RMPIDBU",
            password="rmpi2021",
            host="localhost",
            port=3306,
            database="RMPIDB"
        )
        return conn
    except mariadb.Error as e:
        print(f"Error connecting to MariaDB Platform: {e}")
        sys.exit(1)
def dbinsert_param(query,param):
    conn = DBConnect()
    cursor = conn.cursor()
    try:
        cursor.execute(query,param)
    except mariadb.Error as e: 
        print(f"Error: {e}")
    conn.commit() 
    conn.close()
def dbinsert(query):
    conn = DBConnect()
    cursor = conn.cursor()
    try:
        cursor.execute(query)
    except mariadb.Error as e: 
        print(f"Error: {e}")
    conn.commit()
    conn.close()  
#    conn.autocommit = False
