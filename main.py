import psycopg2
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
import sys


def connection():
    con = psycopg2.connect(
        database='testuser',
        user='postgres',
        password='MaximRozov24',
        host='localhost',
        port='5432'
    )

    cur = con.cursor()
    # per = cur.execute('''CREATE  table Control_money( id INTEGER, name VARCHAR(50), category VARCHAR(50), cost INTEGER);''')
    per = cur.execute(
        '''INSERT INTO Control_money (id, name, category, cost) VALUES ('2', 'ботинки', 'одежда', '5000');''')

    # a = cur.fetchall()[1][1]
    # print(a, len(a))

    con.commit()
    con.close()


def sort_by_cost():
    con = psycopg2.connect(
        database='testuser',
        user='postgres',
        password='MaximRozov24',
        host='localhost',
        port='5432'
    )

    cur = con.cursor()
    # per = cur.execute('''CREATE  table Control_money( id INTEGER, name VARCHAR(50), category VARCHAR(50), cost INTEGER);''')
    # per = cur.execute(
    #    '''INSERT INTO Control_money (id, name, category, cost) VALUES ('1', 'куртка', 'одежда', '7000');''')
    per = cur.execute('''SELECT name, category, cost FROM Control_money ORDER BY cost''')

    a = cur.fetchall()
    con.commit()
    con.close()
    print(a)
    return a



