from flask import Flask, request, Response
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, login_manager, login_user, logout_user, login_required, UserMixin
app = Flask(__name__)
#DB
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://user.db'
app.config['SECRET_KEY'] = "m"

db = SQLAlchemy(app)
login_manager = LoginManager()

login_manager.init_app(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)


db.create_all()

@app.route("/user/signup", methods = ['POST'])
def signup():
    if(request.method=='POST'):
        req = request.get_json()
        name_ = req['name']
        email_ = req['email']
        password_ = req['password']
        usr = User(name=name_, email=email_, password=password_)
        db.session.add(usr)
        db.session.commit()
        payload ={
            "message": "User Added Successfully"
        }
        return Response(payload, 201)
    else:
        return Response("Error", 501)

@app.route("/user/signin", methods = ['POST'])
def signin():
    if(request.method=='POST'):
        req = request.get_json()
        email_ = req['email']
        password_ = req['password']
        if (User.query.filter_by(email=email_).first()):
            if(User.query.filter_by(email=email_).first().password == password_):
                return "Login Successfull", 201
            else:
                return "Password Doesn't Match", 501
        else:
            return "Invalid email", 501
    else:
        return Response("Error", 501)

@app.route("/user/signout", methods = ['GET'])
def signout():
    return "Logout Successfull", 201

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080)