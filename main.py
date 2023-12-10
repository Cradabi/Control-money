import psycopg2
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
import sys


def get_last_id():
    con = psycopg2.connect(
        database='testuser',
        user='postgres',
        password='MaximRozov24',
        host='localhost',
        port='5432'
    )

    cur = con.cursor()
    per1 = cur.execute('''SELECT * FROM Control_money;''')

    a = cur.fetchall()[-1][0]
    return a


def add_transaction(name, category, date, cost):
    con = psycopg2.connect(
        database='testuser',
        user='postgres',
        password='MaximRozov24',
        host='localhost',
        port='5432'
    )
    cur = con.cursor()
    last_id = int(get_last_id()) + 1
    cur.execute("INSERT INTO Control_money (id, name, category, date, cost) VALUES (%s, %s, %s, %s, %s)",
                (last_id, name, category, date, int(cost),))

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
    per = cur.execute('''SELECT name, category, date, cost FROM Control_money ORDER BY cost''')

    a = cur.fetchall()
    con.commit()
    con.close()
    print(a)
    return a


def sort_by_cost_reverse():
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
    per = cur.execute('''SELECT name, category, date, cost FROM Control_money ORDER BY cost DESC''')

    a = cur.fetchall()
    con.commit()
    con.close()
    print(a)
    return a
