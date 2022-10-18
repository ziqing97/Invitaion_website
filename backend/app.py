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

class Article(db.Model, Todict):
    __tablename__ = 'article'
    article_id          = db.Column(db.Integer, autoincrement=True, primary_key=True, nullable=False)
    article_name        = db.Column(db.String(40), nullable=False)
    author_id           = db.Column(db.Integer, nullable=False)
    last_edit_time      = db.Column(db.DateTime, nullable=False)
    create_time         = db.Column(db.DateTime, nullable=False)
    views               = db.Column(db.Integer, nullable=False)
    content             = db.Column(db.Text, nullable=False)

class User(db.Model, Todict):
    __tablename__ = 'user'
    user_id             = db.Column(db.Integer, autoincrement=True, primary_key=True, nullable=False)
    user_name           = db.Column(db.String(40), nullable=False)
    nickname            = db.Column(db.String(40), nullable=False)
    email               = db.Column(db.String(40), nullable=False)
    group               = db.Column(db.Integer, nullable=False)
    password            = db.Column(db.String(40), nullable=False)

class Category(db.Model, Todict):
    __tablename__ = 'category'
    category_id         = db.Column(db.Integer, autoincrement=True, primary_key=True, nullable=False)
    category_name       = db.Column(db.Integer, primary_key=True, nullable=False)
    
# 多个单词转换为小写并使用下划线分隔
class CategoryArticle(db.Model, Todict):
    __tablename__ = 'category_article'
    category_id         = db.Column(db.Integer, primary_key=True, nullable=False)
    article_id          = db.Column(db.String(20), primary_key=True, nullable=False)

class Tag(db.Model, Todict):
    __tablename__ = 'tag'
    tag_id              = db.Column(db.Integer, autoincrement=True, primary_key=True, nullable=False)
    tag_name            = db.Column(db.String(20), nullable=False)
        
# 多个单词转换为小写并使用下划线分隔
class TagArticle(db.Model, Todict):
    __tablename__ = 'tag_article'
    tag_id              = db.Column(db.Integer, primary_key=True, nullable=False)
    article_id          = db.Column(db.Integer, primary_key=True, nullable=False)



def initdb():
    db.create_all()
    click.echo('Intialized database.')


## 所有文章根据，最近修改时间排序
@app.route('/article/all', methods=['GET'])
def get_all_articles():
    sqlData = Article.query.order_by(Article.last_edit_time.desc()).all()
    result = []
    for data in sqlData:
        userName = User.query.filter_by(user_id=data.author_id).first()
        dataDict = data.to_dict()
        dataDict["author_id"]=userName.nickname
        result.append(dataDict) 
    return json.dumps(result, default=str)

## 所有的tag
@app.route('/tag/all', methods=['GET'])
def get_all_tags():
    sqlData = Tag.query.all()
    result = []
    for data in sqlData:
        # result.append(data.to_dict())
        result.append(data.tag_name)
    return json.dumps(result, default=str)

## 所有的category
@app.route('/category/all', methods=['GET'])
def get_all_categories():
    sqlData = Category.query.all()
    result = []
    for data in sqlData:
        # result.append(data.to_dict())
        result.append(data.category_name)
    return json.dumps(result, default=str)

## 所有的nickname
@app.route('/nickname/all', methods=['GET'])
def get_all_nickname():
    sqlData = User.query.all()
    result = []
    for data in sqlData:
        # result.append(data.to_dict())
        result.append(data.nickname)
    return json.dumps(result, default=str)

## 所有的username
@app.route('/username/all', methods=['GET'])
def get_all_username():
    sqlData = User.query.all()
    result = []
    for data in sqlData:
        # result.append(data.to_dict())
        result.append(data.user_name)
    return json.dumps(result, default=str)


## 已知tag，返回该tag下所有的文章 POST(string)
@app.route('/tag/articles', methods=['POST'])
def get_articles_in_tag():
    tagName = request.form.get("tag_name")
    tagId   = request.form.get("tag_id")
    
    if(tagId == None and tagName == None):
        return "FAILED"
    
    if(tagId == None):
        # 查询tag表获取tag_id
        sqlData = Tag.query.filter(Tag.tag_name == str(tagName))
        result = []
        for data in sqlData:
            result.append(data.to_dict())
        tagId = result[0]["tag_id"]
    
    # 查询tag_article表下所有的article_id
    sqlData = TagArticle.query.filter(TagArticle.tag_id == int(tagId))
    articleIds = []
    for data in sqlData:
        articleIds.append(data.to_dict()["article_id"])
    
    # 查询article表下的所有文章
    result = []
    data = []
    for id in articleIds:
        sqlData = Article.query.filter(Article.article_id == int(id))
        for data in sqlData:
            userName = User.query.filter_by(user_id=data.author_id).first()
            dataDict = data.to_dict()
            dataDict["author_id"]=userName.nickname
            result.append(dataDict) 
    return json.dumps(result, default=str)

## 已知category，返回该category下所有的文章 POST(string)
@app.route('/category/articles', methods=['POST'])
def get_articles_in_category():
    categoryName = request.form.get("category_name")
    categoryId   = request.form.get("category_id")
    
    if(categoryId == None and categoryName == None):
        return "FAILED"
    
    if(categoryId == None):
        # 查询category表获取tag_id
        sqlData = Category.query.filter(Category.category_name == str(categoryName))
        result = []
        for data in sqlData:
            result.append(data.to_dict())
        categoryId = result[0]["category_id"]
    
    # 查询category_article表下所有的article_id
    sqlData = CategoryArticle.query.filter(CategoryArticle.category_id == int(categoryId))
    articleIds = []
    for data in sqlData:
        articleIds.append(data.to_dict()["article_id"])
    
    print(articleIds)
    
    # 查询article表下的所有文章
    result = []
    for id in articleIds:
        sqlData = Article.query.filter(Article.article_id == id)
        for data in sqlData:
            userName = User.query.filter_by(user_id=data.author_id).first()
            dataDict = data.to_dict()
            dataDict["author_id"]=userName.nickname
            result.append(dataDict) 
    return json.dumps(result, default=str)


## 已知文章标题，返回文章
@app.route('/title', methods=['POST'])
def get_article_in_title():
    title = request.form.get("article_title")
    
    if(title == None):
        return "FAILED"
    
    sqlData = Article.query.filter(Article.article_name == str(title))
    result = []
    for data in sqlData:
        userName = User.query.filter_by(user_id=data.author_id).first()
        dataDict = data.to_dict()
        dataDict["author_id"]=userName.nickname
        result.append(dataDict) 
   
    return json.dumps(result, default=str)

# 已知文章标题，返回该文章的tag和category
@app.route('/article/query', methods=['POST'])
def get_tag_category_of_article():
    title = request.form.get("article_title")
    if(title == None):
        return "FAILED"
    
    # 获取article_id
    sqlData = Article.query.filter(Article.article_name == str(title)).first()
    sqlId = sqlData.article_id
    
    # 根据article_id在tag_article表中查询tag_id
    sqlTag = TagArticle.query.filter_by(article_id=sqlId).all() 
    tagNameList = []
    for data in sqlTag:
        sqlTagId = data.tag_id
        # 查询每个tag的名字
        tagData = Tag.query.filter_by(tag_id=sqlTagId).first()
        if(tagData):
            tagNameList.append(tagData.tag_name)
            
    result = {}
    result["tag_name"] = tagNameList
    
    # 根据article_id在category_article中查询category_id       
    sqlCat = CategoryArticle.query.filter_by(article_id=sqlId).all() 
    CatNameList = []
    for data in sqlCat:
        sqlCatId = data.category_id
        # 查询每个tag的名字
        CatData = Category.query.filter_by(category_id=sqlCatId).first()
        if(CatData):
            CatNameList.append(CatData.category_name)
    
    result["category_name"] = CatNameList
    print(result)
    
    # 如果返回一对多的json??
    # return json.dumps(tagNameList, default=str)
    return result

# 已知作者名，返回该作者下的所有文章
@app.route('/author/query', methods=['POST'])
def get_article_of_author():
    nickName = request.form.get("nick_name")
    userName = request.form.get("user_name")
    
    # 获取id
    userId = -1
    if(nickName == None and userName == None):
        return "FAILED"
    elif(nickName != None):
        # 根据nickName获取id
        userId = User.query.filter_by(nickname = nickName).first().user_id
    else:
        # 根据userName获取id
        userId = User.query.filter_by(user_name = userName).first().user_id
    
    # 获取article_id
    sqlData = Article.query.filter_by(author_id = userId).all()
    
    result = []
    for data in sqlData:
        dataDict = data.to_dict()
        dataDict["author_id"] = nickName
        result.append(dataDict) 
   
    return json.dumps(result, default=str)  

## 提交新的文章
@app.route('/article/publish', methods=['POST'])
def save_new_article():
    ## TO DO
    
    
    return