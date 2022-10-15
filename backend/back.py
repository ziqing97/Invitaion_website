from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
import os

import config

app = Flask(__name__,)
app.config.from_object(config)
db = SQLAlchemy(app)

class Users(db.Model):
    __tablename__ = 'users'
    user_id = db.Column(db.Integer, primary_key=True, nullable=False)
    user_ip = db.Column(db.String(40), nullable=False)
    user_name = db.Column(db.String(40), nullable=False)
    user_password = db.Column(db.String(20), nullable=False)
    user_email = db.Column(db.String(40), nullable=False)
    user_profile_photo = db.Column(db.String(255), nullable=False)
    user_registration_time = db.Column(db.DateTime, nullable=False)
    user_birthday = db.Column(db.DateTime, nullable=False)
    user_age = db.Column(db.Integer, nullable=False)
    user_telephone_number = db.Column(db.Integer, nullable=False)
    user_nickname = db.Column(db.String(40), nullable=False)

class Articles(db.Model):
    __tablename__ = 'articles'
    article_id              = db.Column(db.Integer, primary_key=True, nullable=False)   
    user_id                 = db.Column(db.Integer, nullable=False)
    article_content         = db.Column(db.Text, nullable=False)
    article_views           = db.Column(db.Integer, nullable=False)
    article_comment_count   = db.Column(db.Integer, nullable=False)
    article_date            = db.Column(db.DateTime, nullable=False)
    article_last_edit_date  = db.Column(db.DateTime, nullable=False)
    article_like_count      = db.Column(db.Integer, nullable=False)
    article_catalogue       = db.Column(db.String(20), nullable=False)
    
    # def to_json(sefl):
    #     return{
    #         'article_id            ' = self.article_id,
    #         'user_id               ' = self.user_id,
    #         'article_content       ' = self.article_content,
    #         'article_views         ' = self.article_views,
    #         'article_comment_count ' = self.article_comment_count,
    #         'article_date          ' = self.article_date,
    #         'article_last_edit_date' = self.article_last_edit_date,
    #         'article_like_count    ' = self.article_like_count
    #     }
    def to_json(self):
        dict = self.__dict__
        if "_sa_instance_state" in dict:
            del dict["_sa_instance_state"]
        return dict  

class Comments(db.Model):
    __tablename__ = 'comments'
    comment_id          = db.Column(db.Integer, primary_key=True, nullable=False) 
    user_id             = db.Column(db.Integer, nullable=False)
    article_id          = db.Column(db.Integer, nullable=False)
    comment_like_count  = db.Column(db.Integer, nullable=False)
    comment_date        = db.Column(db.DateTime, nullable=False)
    comment_content     = db.Column(db.Text, nullable=False)
    parent_comment_id   = db.Column(db.Integer, nullable=False)

class Labels(db.Model):
    __tablename__ = 'labels'
    label_id            = db.Column(db.Integer, primary_key=True, nullable=False)
    label_name          = db.Column(db.String(20), nullable=False)
    label_alias         = db.Column(db.String(20), nullable=False)
    label_description   = db.Column(db.Text, nullable=False)

# 多个单词转换为小写并使用下划线分隔
class SetArtitleLabel(db.Model):
    __tablename__ = 'set_artitle_label'
    # id = db.Column(db.Integer, primary_key=True, nullable=False)
    article_id  = db.Column(db.Integer, primary_key=True, nullable=False)
    label_id    = db.Column(db.Integer, primary_key=True, nullable=False)

class Sorts(db.Model):
    __tablename__ = 'sorts'
    sort_id             = db.Column(db.Integer, primary_key=True, nullable=False)
    sort_name           = db.Column(db.String(20), nullable=False)
    sort_alias          = db.Column(db.String(15), nullable=False)
    sort_description    = db.Column(db.Text, nullable=False)
    parent_sort_id      = db.Column(db.Integer, nullable=False)

class UserFriends(db.Model):
    __tablename__ = 'user_friends'
    id              = db.Column(db.Integer, primary_key=True, nullable=False)
    user_id         = db.Column(db.Integer, nullable=False)
    user_friends_id = db.Column(db.Integer, nullable=False)
    user_note       = db.Column(db.String(20), nullable=False)
    user_status     = db.Column(db.String(20), nullable=False)

def initdb():
    db.create_all()
    click.echo('Intialized database.')


@app.route('/word/cloud/article', methods=['GET'])
def get_one_articles():
    data1 = Articles.query.all()
    result = []
    for data in data1:
        result.append(data.to_json()) 
    print(result[0]['article_content'])
    return result[0]


# for test
# data1 = Articles.query.all()
# result = []
# for data in data1:
#     result.append(data.to_json()) 
# print(result[0])
# db.create_all()