import mysql.connector
from mysql.connector import errorcode
import configparser
import json
from operator import itemgetter

def querie_execute(controller,code):
    high_critical(controller, code)
    mid_critical(controller, code)
    low_critical(controller, code)
    not_critical(controller, code)

def configuration ():
    config = configparser.ConfigParser()
    config.read('config.ini')

    host = config['DEFAULT']['host']
    user = config['DEFAULT']['user']
    db = config['DEFAULT']['database']
    psswd = config['DEFAULT']['password']

    return host, user, db, psswd
host, user, db, psswd = configuration()


def readQueries ():
    with open("config.txt","r") as f:
        code = f.read()
    #print(queries)
    return code
code = readQueries()


def connect(host, user, db, psswd):
    try:
      user = mysql.connector.connect(host= host,user= user,database= db,password= psswd)
      print("Connection Successful, Connected to %s " %(db))
      print()
      return user
    except mysql.connector.Error as err:
      if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Something is wrong with your user name or password")
      elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist")
      else:
        print(err)
controller =  (connect(host, user, db, psswd))

def calc_percent(r):
    return r[5] / r[2] * 100

def high_critical(controller,code):
    critical = 75

    cursor = controller.cursor()
    cursor.execute(code)    # execute code

    with open('report.txt', 'w') as f:
        print("********************************************** Critical Needs Attention: **********************************************", file=f)
        rows = []
        for r in cursor:  #show tables one by one
            if str(type(r[5])) == "<class 'decimal.Decimal'>":
                percent = calc_percent(r)
                if  percent  > critical:
                    rows.append(r)
        rows.sort(key=calc_percent, reverse=True)

        for r in rows:
            percent = calc_percent(r)
            print(r[1],"\nOwner:",r[8],"\nValues:",r[5],"out of", r[2] ,"\nPercent used: %d%% \n" %(percent), file=f)


def mid_critical(controller,code):
    critical = 75
    mid_critical = 50

    cursor = controller.cursor()
    cursor.execute(code)    # execute code

    with open('report.txt', 'a') as f:
        print("\n**********************************************  Mid Critical: ********************************************** ", file=f)
        rows = []
        for r in cursor:  #show tables one by one
            if str(type(r[5])) == "<class 'decimal.Decimal'>":
                percent = calc_percent(r)
                if percent > mid_critical and percent < critical:
                    rows.append(r)
        rows.sort(key=calc_percent, reverse=True)

        for r in rows:
            percent = calc_percent(r)
            print(r[1],"\nOwner:",r[8],"\nValues:",r[5],"out of", r[2] ,"\nPercent used: %d%% \n" %(percent), file=f)


def low_critical(controller,code):
    critical = 75
    mid_critical = 50
    low_critical = 25

    cursor = controller.cursor()
    cursor.execute(code)    # execute code

    with open('report.txt', 'a') as f:
        print("\n**********************************************  Low Critical:********************************************** ", file=f)
        rows = []
        for r in cursor:  #show tables one by one
            if str(type(r[5])) == "<class 'decimal.Decimal'>":
                percent = calc_percent(r)
                if percent > low_critical and percent < mid_critical:
                    rows.append(r)
        rows.sort(key=calc_percent, reverse=True)

        for r in rows:
            percent = calc_percent(r)
            print(r[1],"\nOwner:",r[8],"\nValues:",r[5],"out of", r[2] ,"\nPercent used: %d%% \n" %(percent), file=f)


def not_critical(controller,code):
    critical = 75
    mid_critical = 50
    low_critical = 25
    not_critical = 0


    cursor = controller.cursor()
    cursor.execute(code)    # execute code

    with open('report.txt', 'a') as f:
        print("\n********************************************** Not Critical: **********************************************", file=f)
        rows = []
        for r in cursor:  #show tables one by one
            if str(type(r[5])) == "<class 'decimal.Decimal'>":
                percent = calc_percent(r)
                if percent > not_critical and percent < low_critical:
                    rows.append(r)
        rows.sort(key=calc_percent, reverse=True)

        for r in rows:
            percent = calc_percent(r)
            print(r[1],"\nOwner:",r[8],"\nValues:",r[5],"out of", r[2] ,"\nPercent used: %d%% \n" %(percent), file=f)


#configuration()
#connect(host, user, db, psswd)
querie_execute(controller, code)
