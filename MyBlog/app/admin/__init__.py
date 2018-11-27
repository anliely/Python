# user 目录:针对用户业务逻辑处理的目录
# 针对用户业务逻辑的处理
from flask import Blueprint
admin = Blueprint('user', __name__)

from . import views
