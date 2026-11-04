from flask import Flask
import pymysql

app = Flask(__name__)

@app.route('/parts')
def parts():
    return 'Parts endpoint'

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')
