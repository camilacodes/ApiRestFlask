import pymysql
import json
import requests
from auth import auth_required
from app import app
from config import mysql
from flask import jsonify
from flask import request

@app.route('/inventory', methods =['POST'])
@auth_required
def create_inventory():
    try:
        _json = request.json
        _idcliente_i = _json['idcliente_i']
        _idproduto_i = _json['idproduto_i']
        if _idcliente_i and _idproduto_i and request.method == 'POST':
            conn = mysql.connect()
            cursor = conn.cursor(pymysql.cursors.DictCursor)
            sqlQuery = "INSERT INTO inventory(idcliente_i, idproduto_i) VALUES(%s,%s)"
            bindData = (_idcliente_i, _idproduto_i)
            cursor.execute(sqlQuery, bindData)
            conn.commit()
            response = jsonify('Inventário Criado!')
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

@app.route('/inventory/<int:idinventory>')
@auth_required
def inventory_detail(idinventory):
    try:  
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT * FROM inventory WHERE idinventory=%s", idinventory)
        cliRow = cursor.fetchall()  
        response = jsonify(cliRow)
        response.status_code == 200
        return response
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route('/inventory/cliente/<int:idcliente_i>')
@auth_required
def inventory_client(idcliente_i):
    #REQUEST CLIENTE  
    url = requests.get('http://127.0.0.1:5000/cliente', auth=('admin', '123'))
    text = url.text
    data_cliente =json.loads(text)
    
    listaCliente = []
    for cliente in data_cliente:
        if cliente['id'] == idcliente_i:
            listaCliente.append(cliente)

    #REQUEST PRODUTO  
    conn = mysql.connect()
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    cursor.execute("SELECT idproduto_i FROM inventory WHERE idcliente_i = %s", idcliente_i)
    
    ids = cursor.fetchall()  
    list = []
    for id in ids:
        idproduto = id['idproduto_i'] 
        
        r = requests.get('http://127.0.0.1:5002/products/'+str(idproduto), auth=('admin', '123'))
        products_text = r.text
        data =json.loads(products_text)
        list.append(data)
    try:  
        response ={}
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT * FROM inventory WHERE idcliente_i=%s", idcliente_i)
        cliRow = cursor.fetchall()  
        response['Inventário'] = cliRow
        response['Cliente'] = listaCliente
        response['Produtos'] = list
        return response
    except Exception as e:
            print(e)
    finally:
        cursor.close()
    conn.close()

@app.route('/inventory', methods=['PUT'])
@auth_required
def update_inventory():
    try:
        _json = request.json
        _idinventory = _json['idinventory']
        _idcliente_i = _json['idcliente_i']
        _idproduto_i = _json['idproduto_i']
        if _idinventory and _idcliente_i and _idproduto_i and request.method == 'PUT':
            conn = mysql.connect()
            cursor = conn.cursor(pymysql.cursors.DictCursor)
            sqlQuery = "UPDATE inventory SET idcliente_i=%s, idproduto_i=%s WHERE idinventory=%s"
            bindData = (_idcliente_i, _idproduto_i, _idinventory)
            cursor.execute(sqlQuery, bindData)
            conn.commit()
            response = jsonify('Inventário Updated!')
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


@app.route('/delete_inventory/<int:idinventory>', methods=['DELETE'])
@auth_required
def delete_inventory(idinventory):
    try:
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM inventory WHERE idinventory=%s", (idinventory))
        conn.commit()
        response = jsonify('Deletado com sucesso')
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
     app.run(host='0.0.0.0', port=5002, debug=True)