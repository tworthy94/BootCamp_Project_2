from flask import (
    Flask,
    render_template,
    jsonify,
    request)
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost/Volcano_Data'
app.config['DEBUG'] = True
db = SQLAlchemy(app)
db_uri = 'postgresql://postgres:postgres@localhost/Volcano_Data'
engine = create_engine(db_uri)

@app.route("/")
def index():
     return render_template("index.html")

@app.route("/data")
def db_push():
    query = engine.execute('SELECT * FROM ' '"volcano_data"')
    full_db = query.fetchall()
    return render_template("raw_data.html", data=full_db)

@app.route("/dashboards")
def dashboard():
    return render_template("dashboards.html")

@app.route("/geo")
def geo():
    return render_template("geo_data.html")

if __name__ == "__main__":
    app.run()