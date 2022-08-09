from app import app
from flaskext.mysql import MySQL

mysql = MySQL(app)
app.config['MYSQL_DATABASE_USER'] = 'admin'
app.config['MYSQL_DATABASE_PASSWORD'] = 'camila123'
app.config['MYSQL_DATABASE_DB'] = 'APIDB'
app.config['MYSQL_DATABASE_HOST'] = 'db-camila.cxycaymkd24m.us-east-1.rds.amazonaws.com'


mysql.init_app(app)

debug = True