#-*- coding:utf-8 -*-

wsgi_app="manage:app"
errorlog="error.log"
capture_output=True

workers=4
bind=["0.0.0.0:80"]