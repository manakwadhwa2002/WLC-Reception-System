import sqlite3

conn = sqlite3.connect('wlc_administration_system.db')

c = conn.cursor()

'''
c.execute(""" CREATE TABLE admin (
        first_name text,
        last_name text,
        password text,
        secQuestion text,
        secAnswer text,
        Phone integer,
        Address text,
        City text,
        zipcode integer

)""")

c.execute(""" CREATE TABLE worker (
        first_name text,
        last_name text,
        password text,
        secQuestion text,
        secAnswer text,
        Phone integer,
        Address text,
        City text,
        zipcode integer

)""")

c.execute(""" CREATE TABLE client (
        first_name text,
        last_name text,
        case_type text,
        case_consultant text,
        court_name text,
        court_location text,
        Phone integer,
        client_address text,
        client_city text,
        zipcode integer

)""")
'''

conn.commit()
conn.close()