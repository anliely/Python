from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import pymysql


pymysql.install_as_MySQLdb()
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    # 设置调试模式
    app.config['DEBUG'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://anliely:123456@localhost:3306/myblog"
    app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
    app.config['SECRET_KEY'] = 'you guess'
    # 数据库初始化
    db.init_app(app)


    # 将main蓝图程序与app关联到一起
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    # 将user蓝图程序与app关联到一起
    from .admin import admin as admin_blueprint
    app.register_blueprint(admin_blueprint)
    return app



