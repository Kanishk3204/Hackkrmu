from flask import Flask,render_template
import json
from model import predictDisease

app = Flask(__name__)
# app.debug = True


# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
# db = SQLAlchemy(app)
# class Todo(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     first_name = db.Column(db.String(20), unique=False, nullable=False)
#     last_name = db.Column(db.String(20), unique=False, nullable=False)
#     age = db.Column(db.Integer, nullable=False)
  
#     def __repr__(self):
#         return f"Name : {self.first_name}, Age: {self.age}"

@app.route('/')
def index():
    return render_template('index.html')
    # return '<h2>Hello from Flask!</h2>'

@app.route('/prusinfo/<string:info>', methods=['POST'])
def prusinfo(info):
    output = json.loads(info)
    syms = output['query']
    return predictDisease(syms)

  
app.run(
  host = "0.0.0.0", # or 127.0.0.1
  port = 8080,  # this will allow us to easily fix problems and bugs
)
