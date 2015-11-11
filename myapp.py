from flask import Flask
from flask import render_template
from functools import wraps
from flask import request, Response


app = Flask(__name__)




"""declare auth settings"""
def check_auth(username, password):
    """This function is called to check if a username /
    password combination is valid.
    """
    return username == 'admin' and password == 'admin'

def authenticate():
    """Sends a 401 response that enables basic auth"""
    return Response(
    'Could not verify your access level for that URL.\n'
    'You have to login with proper credentials', 401,
    {'WWW-Authenticate': 'Basic realm="Login Required"'})

def requires_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth = request.authorization
        if not auth or not check_auth(auth.username, auth.password):
            return authenticate()
        return f(*args, **kwargs)
    return decorated

"""end of auth settings"""


@app.route("/")
@requires_auth
def smartHome():
    return render_template('index.html', index_active="active")

@app.route("/home")
@requires_auth
def home():
    return render_template('index.html', index_active="active")


@app.route("/lights", methods=['GET', 'POST'])
@requires_auth
def lights():
    if request.method == 'POST':
        if (request.form['checked'] == "true"):
            print "light on!"
        else:
            print "light off!"
        return 'ok'
    else:
        return render_template('lights.html', lights_active="active",checked="")

@app.route("/ac")
@requires_auth
def ac():
    return render_template('ac.html', ac_active="active")

@app.route("/boiler")
@requires_auth
def boiler():
    return render_template('boiler.html', boiler_active="active")




if __name__ == "__main__":
    app.run(host='0.0.0.0', port=3000, debug=True)

