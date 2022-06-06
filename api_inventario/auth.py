from app import app
from flask import Flask, request, make_response
from functools import wraps


app = Flask(__name__)


def auth_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth = request.authorization
        if auth and auth.username == 'admin' and auth.password == '123':
            return f(*args, **kwargs)
        return make_response('Deu ruim!', 401, {'WWW-Authenticate': 'Basic realm="Login necessário"'})
    return decorated

@app.route('/auth')
def index():
    if request.authorization and request.authorization.username == 'admin' and request.authorization.password == '123':
        return 'Logado!'
    
    return make_response('errouuuuuu!', 401, {'WWW-Authenticate': 'Basic realm="Login necessário"'})


    


if __name__ == "__main__":
    app.run(port=5000, debug=True)
