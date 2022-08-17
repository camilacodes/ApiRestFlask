import pymysql
from auth import auth_required
from app import app
from config import mysql
from flask import jsonify
from flask import request



@app.route('/create_products', methods =['POST'])
@auth_required
def create_products():
    try:
        _json = request.json
        _prod_1 = _json['prod_1']
        _prod_2 = _json['prod_2']
        _prod_3 = _json['prod_3']
        _prod_4 = _json['prod_4']
        _prod_5 = _json['prod_5']
        if _prod_1 and _prod_2 and _prod_3 and _prod_4 and _prod_5 and request.method == 'POST':
            conn = mysql.connect()
            cursor = conn.cursor(pymysql.cursors.DictCursor)
            sqlQuery = "INSERT INTO products(prod_1, prod_2, prod_3, prod_4, prod_5) VALUES(%s,%s, %s, %s, %s)"
            bindData = (_prod_1, _prod_2, _prod_3, _prod_4, _prod_5)
            cursor.execute(sqlQuery, bindData)
            conn.commit()
            response = jsonify('Produto adicionado!')
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
        
@app.route('/products') 
@auth_required
def products():
    try:  
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT id_produto, prod_1, prod_2, prod_3, prod_4, prod_5 FROM products")
        cliRow = cursor.fetchall()  
        response = jsonify(cliRow)
        response.status_code == 200
        return response
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()

@app.route('/products/<int:id_produto>')
@auth_required
def product_detail(id_produto):
    try:  
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT id_produto, prod_1, prod_2, prod_3, prod_4, prod_5 FROM products WHERE id_produto=%s", id_produto)
        cliRow = cursor.fetchall()  
        response = jsonify(cliRow)
        response.status_code == 200
        return response
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()

@app.route('/update_products', methods=['PUT'])
@auth_required
def update_product():
    try:
        _json = request.json
        _id_produto = _json['id_produto']
        _prod_1 = _json['prod_1']
        _prod_2 = _json['prod_2']
        _prod_3 = _json['prod_3']
        _prod_4 = _json['prod_4']
        _prod_5 = _json['prod_5']
        if _id_produto and _prod_1 and _prod_2 and _prod_3 and _prod_4 and _prod_5 and request.method == 'PUT':
            conn = mysql.connect()
            cursor = conn.cursor(pymysql.cursors.DictCursor)
            sqlQuery = "UPDATE products SET prod_1=%s, prod_2=%s, prod_3=%s, prod_4=%s, prod_5=%s WHERE id_produto=%s"
            bindData = (_prod_1, _prod_2, _prod_3, _prod_4, _prod_5, _id_produto)
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

@app.route('/delete_products/<int:id_produto>', methods=['DELETE'])
@auth_required
def delete_product(id_produto):
	try:
		conn = mysql.connect()
		cursor = conn.cursor()
		cursor.execute("DELETE FROM products WHERE id_produto =%s", (id_produto))
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

health_status = True

@app.route('/toggle')
def toggle():
    global health_status
    health_status = not health_status
    return jsonify(health_value=health_status)

@app.route('/health')
def health():
    if health_status:
        resp = jsonify(health="healthy")
        resp.status_code = 200
    else:
        resp = jsonify(health="unhealthy")
        resp.status_code = 500

    return resp

if __name__ == "__main__":
     app.run(host='0.0.0.0', port=5003, debug=True)