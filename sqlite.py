import sqlite3
from webbrowser import get
from classes import Certificate
conn = sqlite3.connect('certificates.db')

c = conn.cursor()

# c.execute("""CREATE TABLE certificates (
#             name text
#             )""")


def insert_certificate(certificate):
    with conn: #automatically commits
        c.execute("INSERT INTO certificates VALUES (:name)",{'name': certificate.name})

def get_certificate(certificate):
    c.execute("SELECT * FROM certificates WHERE name = :name", {'name': certificate})
    return c.fetchall()


def update_certificate(old_name, new_name):
    with conn:
        c.execute("UPDATE certificates SET name = :new_name WHERE name = :old_name",{'new_name': new_name, 'old_name': old_name})


def remove_certificate(certificate):
    with conn:
        c.execute("DELETE from certificates WHERE name = :name",{'name': certificate})

# cert_1 = Certificate('John')
# cert_2 = Certificate('Joe')
# # insert_certificate(cert_1)
# # insert_certificate(cert_2)
# update_certificate('Joe','Nam')
# remove_certificate('John')
# x = get_certificate('John')
# print(x)

conn.close()



