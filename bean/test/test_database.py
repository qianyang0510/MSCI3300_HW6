# -*- coding:utf-8 -*-

from bean.app import app, db
from bean.models.db_bean import User, Good, ShoppingCart
import unittest


class DatabaseTest(unittest.TestCase):
	def setUp(self):
		app.testing = True
		app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://ygc:123@127.0.0.1:3306/db_bean_test"
		db.create_all()
	
	@staticmethod
	def sleep_time():
		import time
		time.sleep(10)
	
	def test_user_register(self):
		"""测试添加用户的数据库操作"""
		user_name = "叶子"
		password = "leaf_22330"
		user = User(user_name=user_name, password=password)
		db.session.add(user)
		db.session.commit()
		
		DatabaseTest.sleep_time()
		
		ret = User.query.filter_by(user_name=user_name).first()
		self.assertIsNotNone(ret)
	
	def test_good_add(self):
		"""测试添加商品的数据库操作"""
		good_name = "苹果"
		good = Good(good_name=good_name)
		db.session.add(good)
		db.session.commit()
		
		DatabaseTest.sleep_time()
		
		ret = Good.query.filter_by(good_name=good_name).first()
		self.assertIsNotNone(ret)
	
	def test_shoppingCart_add(self):
		"""测试添加购物车的数据库操作"""
		# 首先要添加用户和商品
		# 添加2个用户
		user_name1 = "白百何"
		user_name2 = "向日葵"
		password1 = "flower1_22330"
		password2 = "flower2_22330"
		user1 = User(user_name=user_name1, password=password1)
		user2 = User(user_name=user_name2, password=password2)
		db.session.add_all([user1, user2])
		db.session.commit()
		# 添加2件商品
		good_name1 = "苹果"
		good_name2 = "火龙果"
		good1 = Good(good_name=good_name1)
		good2 = Good(good_name=good_name2)
		db.session.add_all([good1, good2])
		db.session.commit()
		# 测试购物车(1个用户添加2件商品)
		user_id = 1
		good_id1 = 1
		good_id2 = 2
		cart1 = ShoppingCart(user_id=user_id, good_id=good_id1)
		cart2 = ShoppingCart(user_id=user_id, good_id=good_id2)
		db.session.add_all([cart1, cart2])
		db.session.commit()
		
		DatabaseTest.sleep_time()
		
		ret = ShoppingCart.query.filter_by(user_id=user_id).first()
		self.assertIsNotNone(ret)
	
	def tearDown(self):
		"""所有执行结束后，清除操作"""
		db.session.remove()
		db.drop_all()


if __name__ == "__main__":
	unittest.main()
