import pymysql
from auth import auth_required
from app import app
from config import mysql
from flask import jsonify
from flask import request
from validation import *


@app.route('/create', methods =['POST'])
@auth_required
def create_cliente():
    try:
        _json = request.json
        _name = _json['name']
        _email = _json['email']
        _cpf = _json['cpf']
        _tel = _json['tel']
        _age = _json['age']
        if _name and _email and _cpf and _tel and _age and request.method == 'POST':
            conn = mysql.connect()
            cursor = conn.cursor(pymysql.cursors.DictCursor)
            sqlQuery = "INSERT INTO cliente(name, email, cpf, tel, age) VALUES(%s,%s, %s, %s, %s)"
            bindData = (_name, _email, _cpf, _tel, _age,)
            cursor.execute(sqlQuery, bindData)
            conn.commit()
            response = jsonify('Cliente adicionado!')
            response.status_code == 200
            return response
        else:
            return showMessage()
    except Exception as e:
       reponse = jsonify({"Message": f"{e}"})
       return response
    finally:
        cursor.close() 
        conn.close() 
        
@app.route('/cliente') 
@auth_required
def cliente():
    try:  
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT * FROM cliente")
        cliRow = cursor.fetchall()  
        response = jsonify(cliRow)
        response.status_code == 200
        return response
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()

@app.route('/cliente/<int:id>')
@auth_required
def cliente_detail(id):
    try:  
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT id, name, email, cpf, tel, age FROM cliente WHERE id=%s", id)
        cliRow = cursor.fetchall()  
        response = jsonify(cliRow)
        response.status_code == 200
        return response
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()

@app.route('/update', methods=['PUT'])
@auth_required
def update_cliente():
    try:
        _json = request.json
        _id = _json['id']
        _name = _json['name']
        _email = _json['email']
        _cpf = _json['cpf']
        _tel = _json['tel']
        _age = _json['age']
        if _name and _email and _cpf and _tel and _age and _id and request.method == 'PUT':
            conn = mysql.connect()
            cursor = conn.cursor(pymysql.cursors.DictCursor)
            sqlQuery = "UPDATE cliente SET name=%s, email=%s, cpf=%s, tel=%s, age=%s WHERE id=%s"
            bindData = (_name, _email, _cpf, _tel, _age, _id)
            cursor.execute(sqlQuery, bindData)
            conn.commit()
            response = jsonify('Cliente Atualizado!')
            response.status_code == 200
            return response
        else:
            return showMessage()
    except Exception as e:
       reponse = jsonify({"Message": f"{e}"})
       return reponse
    finally:
        cursor.close() 
        conn.close() 

@app.route('/delete/<int:id>', methods=['DELETE'])
@auth_required
def delete(id):
	try:
		conn = mysql.connect()
		cursor = conn.cursor()
		cursor.execute("DELETE FROM cliente WHERE id =%s", (id,))
		conn.commit()
		response = jsonify('Client deleted successfully!')
		return response
	except Exception as e:
		print(e)
	finally:
		cursor.close() 
		conn.close()


@app.errorhandler(404)
def showMessage(error=None):
    message = {
        'status': 404,
        'message': 'Record not found: ' + request.url,
    }
    response = jsonify(message)
    return response



if __name__ == "__main__":
    app.run(debug=True)