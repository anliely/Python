from . import db


class Userinfo(db.Model):
    # 用户信息表
    __tablename__ = "userinfo"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False)
    userpassword = db.Column(db.String(50), nullable=False)
    usertype = db.Column(db.Integer)
    comments = db.relationship("Comments", backref="users", lazy="dynamic")

    def __repr__(self):
        return "<Userinfo %r>" % self.usrname


class Articles(db.Model):
    # 文章信息表
    __tablename__ = "articles"
    id = db.Column(db.Integer, primary_key=True)
    A_title = db.Column(db.String(50), nullable=False)
    A_content = db.Column(db.String(4000), nullable=False)
    A_publishedtime = db.Column(db.DateTime, nullable=False)
    T_name = db.Column(db.Integer, db.ForeignKey("tags.id"))
    # 评论数量
    a_commentnum = db.Column(db.Integer,default=0)
    # 阅读数量
    A_viewnum = db.Column(db.Integer, default=0)
    conmments = db.relationship("Comments", backref="articles", lazy="dynamic")

    def __repr__(self):
        return "<Articles %r>" % self.A_title


class Tags(db.Model):
    # 文章分类表
    __tablename__ = "tags"
    id = db.Column(db.Integer, primary_key=True)
    T_name = db.Column(db.String(50), nullable=False)
    articles = db.relationship("Articles", backref="tags", lazy="dynamic")

    def __repr__(self):
        return "<Tags %r>" % self.T_name


class Comments(db.Model):
    # 评论信息表
    __tablename__ = "comments"
    C_id = db.Column(db.Integer, primary_key=True)
    # 评论内容
    C_comment = db.Column(db.String(50))
    C_leavetime = db.Column(db.DateTime)
    A_id = db.Column(db.Integer, db.ForeignKey("articles.id"))
    U_id = db.Column(db.Integer, db.ForeignKey("userinfo.id"))



