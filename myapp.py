from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route("/")
def smartHome():
    return render_template('index.html', index_active="active")

@app.route("/lights")
def lights():
    return render_template('lights.html', lights_active="active")

@app.route("/ac")
def ac():
    return render_template('ac.html', ac_active="active")

@app.route("/boiler")
def boiler():
    return render_template('boiler.html', boiler_active="active")



if __name__ == "__main__":
    app.run(host='0.0.0.0', port=3000, debug=True)
