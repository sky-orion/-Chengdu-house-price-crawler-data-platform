
from config import db
import json
import json

from flask import Blueprint
# from views.data_view import data_provider
# Blueprint:蓝图，用来创建一个模块
from config import db

class Cityprice_cd(db.Model):
    # 这个类与数据库的成都房价表形成映射关系
    __tablename__ = "fangjia_成都"#表名
    id = db.Column(db.INTEGER, primary_key=True)#必须和表中一样
    district = db.Column(db.String(50))
    price = db.Column(db.INTEGER)#这个类必须对应数据库中表的各列名称
class Cityprice_gz(db.Model):
    # 这个类与数据库的成都房价表形成映射关系
    __tablename__ = "fangjia_广州"#表名
    id = db.Column(db.INTEGER, primary_key=True)#必须和表中一样
    district = db.Column(db.String(50))
    price = db.Column(db.INTEGER)#这个类必须对应数据库中表的各列名称
class Cityprice_xm(db.Model):
    # 这个类与数据库的成都房价表形成映射关系
    __tablename__ = "fangjia_厦门"#表名
    id = db.Column(db.INTEGER, primary_key=True)#必须和表中一样
    district = db.Column(db.String(50))
    price = db.Column(db.INTEGER)#这个类必须对应数据库中表的各列名称
class Cityprice_qhd(db.Model):
    # 这个类与数据库的成都房价表形成映射关系
    __tablename__ = "fangjia_秦皇岛"#表名
    id = db.Column(db.INTEGER, primary_key=True)#必须和表中一样
    district = db.Column(db.String(50))
    price = db.Column(db.INTEGER)#这个类必须对应数据库中表的各列名称
class Cityprice_hz(db.Model):
    # 这个类与数据库的成都房价表形成映射关系
    __tablename__ = "fangjia_杭州"#表名
    id = db.Column(db.INTEGER, primary_key=True)#必须和表中一样
    district = db.Column(db.String(50))
    price = db.Column(db.INTEGER)#这个类必须对应数据库中表的各列名称
class Cityprice_sh(db.Model):
    # 这个类与数据库的成都房价表形成映射关系
    __tablename__ = "fangjia_上海"#表名
    id = db.Column(db.INTEGER, primary_key=True)#必须和表中一样
    district = db.Column(db.String(50))
    price = db.Column(db.INTEGER)#这个类必须对应数据库中表的各列名称
class Cityprice_wh(db.Model):
    # 这个类与数据库的成都房价表形成映射关系
    __tablename__ = "fangjia_武汉"#表名
    id = db.Column(db.INTEGER, primary_key=True)#必须和表中一样
    district = db.Column(db.String(50))
    price = db.Column(db.INTEGER)#这个类必须对应数据库中表的各列名称
class Cityprice_sy(db.Model):
    # 这个类与数据库的成都房价表形成映射关系
    __tablename__ = "fangjia_沈阳"#表名
    id = db.Column(db.INTEGER, primary_key=True)#必须和表中一样
    district = db.Column(db.String(50))
    price = db.Column(db.INTEGER)#这个类必须对应数据库中表的各列名称
class Cityprice_nj(db.Model):
    # 这个类与数据库的成都房价表形成映射关系
    __tablename__ = "fangjia_南京"#表名
    id = db.Column(db.INTEGER, primary_key=True)#必须和表中一样
    district = db.Column(db.String(50))
    price = db.Column(db.INTEGER)#这个类必须对应数据库中表的各列名称
class Cityprice_tj(db.Model):
    # 这个类与数据库的成都房价表形成映射关系
    __tablename__ = "fangjia_天津"#表名
    id = db.Column(db.INTEGER, primary_key=True)#必须和表中一样
    district = db.Column(db.String(50))
    price = db.Column(db.INTEGER)#这个类必须对应数据库中表的各列名称
