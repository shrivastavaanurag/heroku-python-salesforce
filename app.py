import os
import psycopg2
from flask import Flask
import json
from urllib.parse import urlparse
from os.path import exists
from os import makedirs

url = urlparse(os.environ.get('DATABASE_URL'))
db = "dbname=%s user=%s password=%s host=%s " % (url.path[1:], url.username, url.password, url.hostname)
schema = "schema.sql"
conn = psycopg2.connect(db)
cur = conn.cursor()

app = Flask(__name__)
# app.config["DEBUG"] = True


@app.route('/contacts', methods=['GET'])
def contacts():
    try:
        cur.execute("""SELECT name from pythonsalesforceexample.Contact""")
        rows = cur.fetchall()
        #response = ''
        my_list = []
        for row in rows:
            my_list.append(row[0])
        print('------------___>>>>>>>>>> : ' + str(my_list))
        return {"name": "anurag", "id": "007"}
    except Exception as e:
        print('------------------->>>> Exception : ', e)
        return []

if __name__ == '__main__':
    app.run()