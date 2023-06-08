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

@app.route('/MP_verify_ziT6pOvsViIMgLQlj.txt', methods=['GET'])
def return_weixin_api():
    return "ziT6pOvsViIMgLQl"

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