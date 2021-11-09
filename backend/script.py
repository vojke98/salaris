#!/usr/bin/python

import sqlite3
from sqlite3 import Error
#conn = sqlite3.connect('/home/ademir/Desktop/backend/db.sqlite3')




def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by the db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)

    return conn


def selectUsers(conn):

    cur = conn.cursor()
    cur.execute("SELECT id, first_name, last_name, email from webapp_user")

    rows = cur.fetchall()

    for row in rows:
        print(row)


def insert(conn):

    cur = conn.cursor()

    cur.execute('''INSERT INTO webapp_city(post_no, name)
                VALUES (1000, 'Ljubljana')''')

    cur.execute('''INSERT INTO webapp_city(post_no, name)
                    VALUES (2000, 'Maribor')''')

    cur.execute('''INSERT INTO webapp_city(post_no, name)
                    VALUES (4000, 'Kranj')''')

    cur.execute('''INSERT INTO webapp_address(house_no, street, city_id)
                    VALUES ('51a', 'Gerbičeva ulica', 1)''')

    cur.execute('''INSERT INTO webapp_address(house_no, street, city_id)
                    VALUES ('5', 'Cesta V', 1)''')

    cur.execute('''INSERT INTO webapp_address(house_no, street, city_id)
                    VALUES ('50', 'Ne znam za Dinu', 1)''')

    cur.execute('''INSERT INTO webapp_address(house_no, street, city_id)
                    VALUES ('1', 'Tržaška cesta', 1)''')

    cur.execute('''INSERT INTO webapp_address(house_no, street, city_id)
                    VALUES ('69', 'Neka cesta', 3)''')

    cur.execute('''INSERT INTO webapp_role(name, min_hourly_rate)
                    VALUES ('CEO', 50.0)''')

    cur.execute('''INSERT INTO webapp_role(name, min_hourly_rate)
                    VALUES ('MANAGER', 20.0)''')

    cur.execute('''INSERT INTO webapp_role(name, min_hourly_rate)
                    VALUES ('WORKER', 10.0)''')

    cur.execute('''INSERT INTO webapp_company(tax_no, name, address_id)
                    VALUES ('SI01234567', 'Salaris', 4)''')

    cur.execute('''INSERT INTO webapp_company(tax_no, name, address_id)
                    VALUES ('SI12345678', 'Njesrav2', 5)''')

    cur.execute('''INSERT INTO webapp_user(tax_no, first_name, last_name, email, address_id, company_id, role_id)
                    VALUES (01234567, 'Dejan', 'Vojinović', 'dv@gmail.com', 1, 1, 1)''')

    cur.execute('''INSERT INTO webapp_user(tax_no, first_name, last_name, email, address_id, company_id, role_id)
                    VALUES (12345678, 'Ademir', 'Jusić', 'aj@gmail.com', 2, 1, 1)''')

    cur.execute('''INSERT INTO webapp_user(tax_no, first_name, last_name, email, address_id, company_id, role_id)
                    VALUES (23456789, 'Dino', 'Čeliković', 'dc@gmail.com', 3, 1, 1)''')

    cur.execute('''INSERT INTO webapp_workhour(date_from, date_until, company_id, user_id)
                    VALUES (1636417320576, 1636417323576, 1, 1)''')

    cur.execute('''INSERT INTO webapp_workhour(date_from, date_until, company_id, user_id)
                    VALUES (1636407320576, 1636410323576, 1, 1)''')

    cur.execute('''INSERT INTO webapp_workhour(date_from, date_until, company_id, user_id)
                    VALUES (1636417320576, 1636417323576, 1, 2)''')

    cur.execute('''INSERT INTO webapp_workhour(date_from, date_until, company_id, user_id)
                    VALUES (1636407320576, 1636410323576, 1, 2)''')

    cur.execute('''INSERT INTO webapp_workhour(date_from, date_until, company_id, user_id)
                    VALUES (1636417320576, 1636417323576, 1, 2)''')

    cur.execute('''INSERT INTO webapp_workhour(date_from, date_until, company_id, user_id)
                    VALUES (1636407320576, 1636410323576, 1, 2)''')


    conn.commit()



def main():
    database = './db.sqlite3'

    # create a database connection
    conn = create_connection(database)
    with conn:
        # functions
        selectUsers(conn)
        insert(conn)
        print()
        selectUsers(conn)

    conn.close()


if __name__ == '__main__':
    main()




    """
cursor = conn.execute("SELECT id, first_name, last_name, email from webapp_user")

for row in cursor:
    print(row)
    print ("ID = ", row[0])
    print ("FIRST_NAME = ", row[1])
    print ("LAST_NAME = ", row[2])
    print ("EMAIL = ", row[3], "\n")

print("Done")

conn.close()
"""