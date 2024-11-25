from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://user:password@localhost/dbname'
db = SQLAlchemy(app)

@app.route('/')
def index():
    return "Hello, Production Planning!"

if __name__ == '__main__':
    app.run(debug=True)
