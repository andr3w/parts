from flask import Flask, render_template
import pymysql

app = Flask(__name__)

@app.route('/parts', strict_slashes=False)
def parts():
    return render_template('parts.html')

@app.route('/parts/api/parts')
def parts_api():
    con = pymysql.connect(user='parts',database='parts')
    cur = con.cursor()
    cur.execute('SELECT * FROM parts')
    results = cur.fetchall()
    return {'data':[{'id':a[0],'description':a[1]} for a in results]}
