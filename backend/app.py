from sre_constants import SUCCESS
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask import request
import json

import config

app = Flask(__name__)
app.config.from_object(config)
db = SQLAlchemy(app)

class Todict:
    def to_dict(self):
        dict = self.__dict__
        if "_sa_instance_state" in dict:
            del dict["_sa_instance_state"]
        return dict  

class Invitation(db.Model):
    __tablename__ = 'invitations'
    invitation_id = db.Column(db.String(20), primary_key=True, nullable=False)
    guest_name = db.Column(db.String(20), nullable=False)
    invitation_time = db.Column(db.DateTime, nullable=False)
    guest_count = db.Column(db.Integer, nullable=False)
    contact_number = db.Column(db.Integer, nullable=False)
    main_lawyer_name = db.Column(db.String, nullable=False)
    assistant_name = db.Column(db.String, nullable=True)

class Worker(db.Model):
    __tablename__ = 'workers'
    worker_id = db.Column(db.Integer, primary_key=True, nullable=False)
    worker_name = db.Column(db.String(20), nullable=False)

def initdb():
    db.create_all()
    click.echo('Intialized database.')

# return all invitations order by time
@app.route('/invitation/all', methods=['GET'])
def get_all_invitations():
    sqlData = Invitation.query.order_by(Invitation.invitation_time.desc()).all()
    result = []
    for data in sqlData:
        result.append(data.to_dict())
    print(sqlData)
    return json.dumps(result, default=str)

# return the invitation with given id
@app.route('/invitation/get', methods=['POST'])
def get_invitation_in_id():
    title = request.form.get("invitation_id")
    
    if(title == None):
        return "FAILED"

    sqlData = Invitation.query.filter(Invitation.invitation_id == str(title))
    result = []
    for data in sqlData:
        result.append(data.to_dict())
   
    return json.dumps(result, default=str)

# add a new invitation
@app.route('/invitation/add', methods=['POST','GET'])
def add_new_invitation():
    if not request.form['invitation_id'] or not request.form['guest_name'] or not request.form['invitation_time'] \
        or not request.form['guest_count'] or not request.form['contact_number'] or not request.form['main_lawyer_name'] \
        or not request.form['assistant_name']:
        flash('有内容为空！')
    else:
        invitation = Invitation(request.form['invitation_id'],request.form['guest_name'],request.form['invitation_time'],\
        request.form['guest_count'],request.form['contact_number'],request.form['main_lawyer_name'],\
        request.form['assistant_name'])

        db.session.add(invitation)
