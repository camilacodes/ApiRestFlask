from app import app
from flaskext.mysql import MySQL

mysql = MySQL(app)
app.config['MYSQL_DATABASE_USER'] = 
app.config['MYSQL_DATABASE_PASSWORD'] = 
app.config['MYSQL_DATABASE_DB'] = 
app.config['MYSQL_DATABASE_HOST'] = 

mysql.init_app(app)

debug = True
