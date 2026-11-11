# parts
Generate part numbers in a database

Installation:

sudo apt install mariadb-server
sudo mysql -u root < mktable.sql

sudo apt install python3-venv
python3 -m venv venv
source ./venv/bin/activate
pip install flask
pip install pymysql


touch /tmp/parts.touchme; tail -f /var/log/uwsgi/app/parts.log
