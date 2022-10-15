import json
from flask import Blueprint,request
from .models import Article,Tag,Category,TagArticle,CategoryArticle

api = Blueprint('main',__name__,url_prefix='/api')


## 所有文章根据，最近修改时间排序
@api.route('/article/all', methods=['GET'])
def get_all_articles():
    sqlData = Article.query.order_by(Article.last_edit_time.desc()).all()
    result = []
    for data in sqlData:
        result.append(data.to_dict()) 
    return json.dumps(result, default=str)

## 所有的tag
@api.route('/tag/all', methods=['GET'])
def get_all_tags():
    sqlData = Tag.query.all()
    result = []
    for data in sqlData:
        result.append(data.to_dict())
    return json.dumps(result, default=str)

## 所有的category
@api.route('/category/all', methods=['GET'])
def get_all_categories():
    sqlData = Category.query.all()
    result = []
    for data in sqlData:
        result.append(data.to_dict())
    return json.dumps(result, default=str)

## 已知tag，返回该tag下所有的文章 POST(string)
@api.route('/tag/articles', methods=['POST'])
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
    for id in articleIds:
        sqlData = Article.query.filter(Article.article_id == id)
        for data in sqlData:
            result.append(data.to_dict())
    
    return json.dumps(result, default=str)

## 已知category，返回该category下所有的文章 POST(string)
@api.route('/category/articles', methods=['POST'])
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
            result.append(data.to_dict())
    
    return json.dumps(result, default=str)


## 已知文章标题，返回文章
@api.route('/title', methods=['POST'])
def get_article_in_title():
    title = request.form.get("article_title")
    
    if(title == None):
        return "FAILED"
    
    sqlData = Article.query.filter(Article.article_name == str(title))
    result = []
    for data in sqlData:
        result.append(data.to_dict())
   
    return json.dumps(result, default=str)

