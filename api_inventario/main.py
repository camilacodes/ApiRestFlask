import pymysql
from auth import auth_required
from app import app
from config import mysql
from flask import jsonify
from flask import request



@app.route('/create_inventory', methods =['POST'])
@auth_required
def create_inventory():
    try:
        _json = request.json
        _name_inventory = _json['_name_inventory']
        _idcliente_i =  _json['_idcliente_i']
        _idproduto_i = _json['_idproduto_i']
        if _name_inventory and _idcliente_i and _idproduto_i and request.method == 'POST':
            conn = mysql.connect()
            cursor = conn.cursor(pymysql.cursors.DictCursor)
            sqlQuery = "INSERT INTO inventory(name_inventory, idcliente_i, idproduto_i) VALUES(%s,%s, %s)"
            bindData = (_name_inventory, _idcliente_i, _idproduto_i)
            cursor.execute(sqlQuery, bindData)
            conn.commit()
            response = jsonify('Inventrário Criado!')
            response.status_code == 200
            return response
        else:
            return showMessage()
    except Exception as e:
       response = jsonify({"Message": f"{e}"})
       return response
    finally:
        cursor.close() 
        conn.close() 
        
@app.route('/inventory') 
@auth_required
def inventory():
    try:  
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT * FROM inventory")
        cliRow = cursor.fetchall()  
        response = jsonify(cliRow)
        response.status_code == 200
        return response
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()

@app.route('/inventory/<int:id_inventory>')
@auth_required
def inventory_detail(id_inventory):
    try:  
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT id_inventory, name_inventory, idcliente_i, id_produto FROM inventory WHERE id_inventory=%s", id_inventory)
        cliRow = cursor.fetchall()  
        response = jsonify(cliRow)
        response.status_code == 200
        return response
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()

@app.route('/update_inventory', methods=['PUT'])
@auth_required
def update_inventory():
    try:
        _json = request.json
        _id_inventory = _json['id_inventory']
        _name_inventory = _json['_name_inventory']
        _idcliente_i =  _json['_idcliente_i']
        _idproduto_i = _json['_idproduto_i']
        if _name_inventory and _idcliente_i and _idproduto_i and request.method == 'POST':
            conn = mysql.connect()
            cursor = conn.cursor(pymysql.cursors.DictCursor)
            sqlQuery = "UPDATE inventory SET name_inventory=%s, idcliente_i=%s, idproduto_i=%s WHERE id_inventory=%s"
            bindData = (_id_inventory, _name_inventory, _idcliente_i, _idproduto_i)
            cursor.execute(sqlQuery, bindData)
            conn.commit()
            response = jsonify('Produto atualizado!')
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

@app.route('/delete_inventory/<int:id_inventory>', methods=['DELETE'])
@auth_required
def delete_inventory(id_inventory):
	try:
		conn = mysql.connect()
		cursor = conn.cursor()
		cursor.execute("DELETE FROM inventory WHERE id_inventory =%s", (id_inventory))
		conn.commit()
		response = jsonify('Invetory deleted successfully!')
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