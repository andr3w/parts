from flask import Flask, render_template
import pymysql

app = Flask(__name__)

@app.route('/parts', strict_slashes=False)
def parts():
    return render_template('parts.html')

'''
    con = pymysql.connect(user='parts',database='parts')
    cur = con.cursor()
    cur.execute('SELECT * FROM parts')
    results = cur.fetchall()
    table = '<table border=1>' +\
       ''.join( ['<tr><td>{}</td><td>{}</td></tr>'.format(row[0], row[1]) for row in results]) +\
         '</table>'
    return f'Parts endpoint {table}'
'''