from flask import Flask
from flask import render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)


@app.route("/")
def hello():
    return render_template('index.html')
#    return "Hello World!"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=3000, debug=True)
