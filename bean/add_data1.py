# -*- coding:utf-8 -*-


from app import db
from models.db_bean import User, GoodType, Good, ShoppingCart


def init_data():
	# 初始用户
	user0 = User(user_name="mike_admin", password="1233456", pay_password="1233456")
	user1 = User(user_name="mike_user", password="1233456", pay_password="1233456")

	db.session.add_all([user0, user1])
	db.session.commit()
	
	# 初始商品类型
	type1 = GoodType(type_name="fruit")
	type2 = GoodType(type_name="Electronics")
	type3 = GoodType(type_name="snacks")
	type4 = GoodType(type_name="Sports")
	type5 = GoodType(type_name="Drinks")
	db.session.add_all([type1, type2, type3, type4, type5])
	db.session.commit()
	
	# 初始商品
	good1 = Good(good_name="apple", type=type1.id, price=15.50, stock=200)
	good2 = Good(good_name="orangge", type=type1.id, price=6.50, stock=100)
	good3 = Good(good_name="banana", type=type1.id, price=6.00, stock=50)
	good4 = Good(good_name="phone", type=type2.id, price=2888.8, stock=500)
	good5 = Good(good_name="PC", type=type2.id, price=6888.8, stock=100)
	good6 = Good(good_name="basketball", type=type4.id, price=223.30, stock=30)
	good7 = Good(good_name="ping-pong", type=type4.id, price=1.50, stock=100)
	good8 = Good(good_name="football", type=type4.id, price=199.99, stock=20)
	good9 = Good(good_name="coke", type=type5.id, price=4.00, stock=200)
	good10 = Good(good_name="bread", type=type3.id, price=6.50, stock=150)
	db.session.add_all([good1, good2, good3, good4, good5, good6, good7, good8, good9, good10])
	db.session.commit()
	
	# 初始购物车
	# user1的购物车
	cart1 = ShoppingCart(user_id=user1.id, good_id=good1.id)
	cart2 = ShoppingCart(user_id=user1.id, good_id=good3.id)
	cart3 = ShoppingCart(user_id=user1.id, good_id=good5.id)
	cart4 = ShoppingCart(user_id=user1.id, good_id=good7.id)

	db.session.add_all([cart1, cart2, cart3, cart4])
	db.session.commit()
	
	db.session.remove()


if __name__ == "__main__":
	init_data()
