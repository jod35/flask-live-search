from flask import Flask,render_template,url_for,make_response,jsonify,request
from flask_sqlalchemy import SQLAlchemy
from marshmallow import Schema,fields
import os

from sqlalchemy.ext.declarative import base


basedir=os.path.dirname(os.path.realpath(__file__))




app=Flask(__name__)


DATABASE_URI="sqlite:///"+os.path.join(basedir,"app.db")

app.config["SQLALCHEMY_DATABASE_URI"]=DATABASE_URI

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]=False





db=SQLAlchemy(app)


class User(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    username=db.Column(db.String(),nullable=False)
    email=db.Column(db.String(),nullable=False)


    def __repr__(self):
        return f"{self.username}"
    
    def save(self):
        db.session.add(self)
        db.session.commit()


class UserSchema(Schema):
    id=fields.Int()
    username=fields.Str()
    email=fields.Str()


    


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/search',methods=['POST','GET'])
def search():
    results=User.query


    data=request.get_json()

    print(data)

    results=User.query.filter_by(username=data['username']).all()
    # results=results.order_by(User.username).all()

    users=UserSchema(many=True).dump(results)
    
    print(users)
    return make_response(jsonify(
        {
            "results": users
        }
    ))



@app.shell_context_processor
def make_shell_context():
    return {
        "User":User,
        "app":app,
        "db":db
    }


if __name__ =="__main__":
    app.run(debug=True)