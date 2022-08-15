from app import app
from flaskext.mysql import MySQL

mysql = MySQL(app)
app.config['MYSQL_DATABASE_USER'] = 'admin'
app.config['MYSQL_DATABASE_PASSWORD'] = 'camila123'
app.config['MYSQL_DATABASE_DB'] = 'address'
app.config['MYSQL_DATABASE_HOST'] = 'db-camila.ckatnedhbqjh.us-east-2.rds.amazonaws.com'


mysql.init_app(app)

debug = True