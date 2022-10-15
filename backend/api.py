import json
from flask import Blueprint,request
from .models import Invitation, Worker

api = Blueprint('main',__name__,url_prefix='/api')


# return all invitations order by time
@api.route('/invitation/all', methods=['GET'])
def get_all_invitations():
    sqlData = Invitation.query.order_by(Invitation.invitation_time.desc()).all()
    result = []
    for data in sqlData:
        result.append(data.to_dict()) 
    return json.dumps(result, default=str)

# return the invitation with given id
@api.route('/invitation/get', methods=['POST'])
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
@api.route('/invitation/add', methods=['POST'])
def add_new_invitation():
    a=1