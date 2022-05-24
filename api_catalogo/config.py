from app import app
from flaskext.mysql import MySQL

mysql = MySQL(app)
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'camila123'
app.config['MYSQL_DATABASE_DB'] = 'catalog'
app.config['MYSQL_DATABASE_HOST'] = '127.0.0.1'


mysql.init_app(app)

debug = True