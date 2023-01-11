from sre_constants import SUCCESS
import os
import random
import string
import time
from flask_sqlalchemy import SQLAlchemy
from flask import request,url_for,render_template,Response,Flask
import json
import requests
import urllib.parse
from hashlib import sha1
from django.core.cache import cache

import config

app = Flask(__name__,static_folder="../frontend/dist/static",template_folder="../frontend/dist/")
app.config.from_object(config)
db = SQLAlchemy(app)

os.environ['DJANGO_SETTINGS_MODULE'] = 'setting'

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    return render_template("index.html")

class Todict:
    def to_dict(self):
        dict = self.__dict__
        if "_sa_instance_state" in dict:
            del dict["_sa_instance_state"]
        return dict  

class Invitation(db.Model, Todict):
    __tablename__ = 'invitations'
    invitation_id = db.Column(db.String(20), primary_key=True, nullable=False)
    guest_name = db.Column(db.String(20), nullable=False)
    invitation_time = db.Column(db.String(20), nullable=False)
    guest_count = db.Column(db.Integer, nullable=False)
    contact_number = db.Column(db.String(20), nullable=False)
    main_lawyer_name = db.Column(db.String(20), nullable=False)
    assistant_name = db.Column(db.String(20), nullable=True)
    invitation_hour = db.Column(db.Integer, nullable=False)

class Worker(db.Model, Todict):
    __tablename__ = 'workers'
    worker_id = db.Column(db.Integer, primary_key=True, nullable=False)
    worker_name = db.Column(db.String(20), nullable=False)

class AppItem(db.Model, Todict):
    __tablename__ = 'apiToken'
    Token = db.Column(db.String(128), primary_key=True, nullable=False)
    Appid = db.Column(db.String(128), primary_key=True, nullable=False)
    Appsecret = db.Column(db.String(128), primary_key=True, nullable=False)

def initdb():
    db.create_all()
    #　click.echo('Intialized database.')

# return all invitations order by time
@app.route('/invitation/all', methods=['GET'])
def get_all_invitations():
    sqlData = Invitation.query.order_by(Invitation.invitation_time.desc()).all()
    result = []
    for data in sqlData:
        result.append(data.to_dict())
    return json.dumps(result, default=str)

# validation for wechat
@app.route('/MP_verify_ziT6pOvsViIMgLQlj.txt', methods=['GET'])
def return_weixin_api():
    return "ziT6pOvsViIMgLQl"

def get_chunk(filename, byte1=None, byte2=None):
    filesize = os.path.getsize(filename)
    yielded = 0
    yield_size = 1024 * 1024

    if byte1 is not None:
        if not byte2:
            byte2 = filesize
        yielded = byte1
        filesize = byte2

    with open(filename, 'rb') as f:
        content = f.read()

    while True:
        remaining = filesize - yielded
        if yielded == filesize:
            break
        if remaining >= yield_size:
            yield content[yielded:yielded+yield_size]
            yielded += yield_size
        else:
            yield content[yielded:yielded+remaining]
            yielded += remaining

@app.route('/download/<filepath>', methods=['GET','POST'])
def return_sharepicture(filepath):
    fullfilename = '/usr/static/'+filepath
    filename=filepath.split('/')[-1] # 切割出文件名称
    filedir=fullfilename.replace(filename,'')

    def send_file(fullfilename):
        with open(fullfilename, 'rb') as targetfile:
            while True:
                data = targetfile.read(1 * 1024 * 1024)   # 每次读取1MB (可用限速)
                if not data:
                    break
                yield data
    response = Response(send_file(fullfilename=fullfilename), content_type='application/octet-stream')
    response.headers["Content-disposition"] = f'attachment; filename={filename}'
    return response

# generating jssdk validation token and ticket
@app.route('/wechat/apitoken', methods=['POST'])
def return_weixin_sig():
    data = request.get_json()
    app_id = 'wxbc77294cc827500b'
    noncestr = ''.join(random.sample(string.ascii_letters + string.digits, 8))
    timestamp = round(time.time())
    url = urllib.parse.unquote(data["url"])
    token = cache.get(app_id)
    if token:
        print('token in cache')
    else:
        secret = '1b190b69588f2350dbe377a14d044eb3'
        wechat_r = requests.get(f'https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid={app_id}&secret={secret}')
        if wechat_r.status_code == 200:
            token_dict = wechat_r.json()
            token = token_dict['access_token']
            expires_in = token_dict['expires_in']
            cache.set(app_id, token,expires_in-60)
        else:
            raise Exception('calling token mistake')
        print('called new token')
    ticket = cache.get(app_id+'ticket')
    if ticket:
        print("tickets in cache")
    else:
        wechat_t = requests.get(f'https://api.weixin.qq.com/cgi-bin/ticket/getticket?access_token={token}&type=jsapi')
        if wechat_t.status_code == 200:
            ticket_dict = wechat_t.json()
            ticket = ticket_dict['ticket']
            expires_in_ticket = ticket_dict['expires_in']
            cache.set(app_id+'ticket', ticket,expires_in_ticket-60)
        else:
            raise Exception('calling ticket mistake')
        print('calling new ticket')
    jsapi_ticket = f'jsapi_ticket={ticket}&noncestr={noncestr}&timestamp={timestamp}&url={url}'
    signature = sha1(jsapi_ticket.encode('utf-8'))
    re_data = {'appId':app_id,'noncestr':noncestr,'timestamp':timestamp,'signature':signature.hexdigest()}
    
    return re_data

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
    return result[0]

# add a new invitation
@app.route('/invitation/add', methods=['POST','GET'])
def add_new_invitation():
    data = request.get_json()
    if not data['invitation_id'] or not data['guest_name'] or not data['invitation_time'] \
        or not data['guest_count'] or not data['contact_number'] or not data['main_lawyer_name'] \
        or not data['assistant_name']:
        print("There is something empty, which is not allowed")
        return '-1'
    else:
        date = data['invitation_time'][0:10]
        hour = data['invitation_time'][11:13]
        print(data['invitation_time'])
        new_invitation = Invitation(invitation_id=data['invitation_id'],guest_name=data['guest_name'],\
        invitation_time=date,guest_count=data['guest_count'],contact_number=data['contact_number'],\
        main_lawyer_name=data['main_lawyer_name'],assistant_name=data['assistant_name'],invitation_hour=hour)
        db.session.add(new_invitation)
        db.session.commit()
        db.session.close()
        return '200'

if __name__ == "__main__":
    app.run(host="0.0.0.0",port="5000",debug=True)