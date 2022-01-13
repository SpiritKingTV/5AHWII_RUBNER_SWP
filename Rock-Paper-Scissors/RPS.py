##Database Stuff


import MySQLdb.connections

def connect():
    try:
        db_connection = MySQLdb.connect("localhost","root","ABC13Y@12Bz","RPS")
    except:
        print("Connection didnt work")
        return 0
    #print("Connected")
    db_connection.close()


def createTable():
    try:
        db_connection = MySQLdb.connect("localhost", "root", "ABC13Y@12Bz", "RPS")
    except:
        return 0
    connect()
    sql = "create Table if not exists results(username varchar(30)not null,rock int, paper int, scissors int, lizard int, spock int);"
    cursor = db_connection.cursor()
    cursor.execute(sql)
    db_connection.close()

def selectValues():
    try:
        db_connection = MySQLdb.connect("localhost", "root", "ABC13Y@12Bz", "RPS")
    except:
        return 0

  #select
    sqlselect = "select * from results"
    cursor = db_connection.cursor()
    cursor.execute(sqlselect)
    values = (cursor.fetchone())
    db_connection.close()
    return values;

def drop():
    try:
        db_connection = MySQLdb.connect("localhost", "root", "ABC13Y@12Bz", "RPS")
    except:
        return 0
    cursor = db_connection.cursor()
    cursor.execute("drop table if exists results")
    db_connection.close()


def insert(values):
    try:
        db_connection = MySQLdb.connect("localhost", "root", "ABC13Y@12Bz", "RPS")
    except:
        return 0
    cursor = db_connection.cursor()
    sql = ("insert into results(username,rock,paper, scissors,lizard,spock) values(%s,%s,%s,%s,%s,%s)")
    cursor.execute(sql,values)
    db_connection.commit()
    db_connection.close()

def nocolums():
    try:
        db_connection = MySQLdb.connect("localhost", "root", "ABC13Y@12Bz", "RPS")
    except:
        return 0
    cursor = db_connection.cursor()
    cursor.execute("select count(username) from results")
    valrow = (cursor.fetchone())
    valrow1 = int(valrow[0])
    return valrow1

def firstInsert():
    try:
        db_connection = MySQLdb.connect("localhost", "root", "ABC13Y@12Bz", "RPS")
    except:
        return 0
    cursor = db_connection.cursor()
    cursor.execute("insert into results values ('Manuel Repetschnig',0,0,0,0,0)")
    db_connection.commit()
    db_connection.close()

