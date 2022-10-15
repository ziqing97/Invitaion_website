from .import db

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
    
    # def to_dict(self):
    #     dict = self.__dict__
    #     if "_sa_instance_state" in dict:
    #         del dict["_sa_instance_state"]
    #     return dict  

class User(db.Model, Todict):
    __tablename__ = 'user'
    user_id             = db.Column(db.Integer, autoincrement=True, primary_key=True, nullable=False)
    user_name           = db.Column(db.String(40), nullable=False)
    nickname            = db.Column(db.String(40), nullable=False)
    email               = db.Column(db.String(40), nullable=False)
    group               = db.Column(db.Integer, nullable=False)
    user_password       = db.Column(db.String(40), nullable=False)

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

#def initdb():
#    db.create_all()
#    click.echo('Intialized database.')
