# -*- coding:utf-8 -*-


class Config(object):
	"""配置参数"""
	# sqlalchemy的配置参数
	SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:Ztc1639643261!@127.0.0.1:3306/beans"
	# 设置sqlalchemy自动跟踪数据库
	SQLALCHEMY_TRACE_MODIFICATIONS = True
	# 设置秘钥
	SECRET_KEY = "secret key 123456"
	# 设置session有效时间（秒）
	# PERMANENT_SESSION_LIFETIME = 604800
