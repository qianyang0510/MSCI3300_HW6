# -*- coding:utf-8 -*-


from app import db


class User(db.Model):
	"""用户"""
	__tablename__ = "tbl_user"
	id = db.Column(db.Integer, primary_key=True)
	user_name = db.Column(db.String(32), nullable=False)
	password = db.Column(db.String(64), nullable=False)
	pay_password = db.Column(db.String(64), nullable=False)
	
	cart = db.relationship("ShoppingCart", backref="user")  # 方便查询(用户的购物车)
	payments = db.relationship("Payment", backref="user")  # 方便查询(用户的交易记录)


class GoodType(db.Model):
	"""商品分类"""
	__tablename__ = "tbl_goodType"
	id = db.Column(db.Integer, primary_key=True)
	type_name = db.Column(db.String(64), nullable=False)
	
	goods = db.relationship("Good", backref="goodType")  # 方便查询(商品分类对应的商品)


class Good(db.Model):
	"""商品"""
	__tablename__ = "tbl_good"
	id = db.Column(db.Integer, primary_key=True)
	good_name = db.Column(db.String(64), nullable=False)
	type = db.Column(db.Integer, db.ForeignKey('tbl_goodType.id'), nullable=False)
	price = db.Column(db.Numeric(7, 2), nullable=False)
	stock = db.Column(db.Integer, nullable=False)
	
	type_name = db.relationship("GoodType", backref="good")  # 方便查询(商品对应的商品分类)


class ShoppingCart(db.Model):
	"""购物车"""
	__tablename__ = "tbl_shoppingCart"
	id = db.Column(db.Integer, primary_key=True)
	user_id = db.Column(db.Integer, db.ForeignKey('tbl_user.id'), nullable=False)
	good_id = db.Column(db.Integer, db.ForeignKey('tbl_good.id'), nullable=False)
	
	users = db.relationship("User", backref="shoppingcart")  # 方便查询(购物车对应的用户)
	goods = db.relationship("Good", backref="shoppingcart")  # 方便查询(购物车对应的商品)


class Payment(db.Model):
	"""交易记录"""
	__tablename__ = "tbl_payment"
	id = db.Column(db.Integer, primary_key=True)
	user_id = db.Column(db.Integer, db.ForeignKey('tbl_user.id'), nullable=False)
	good_id = db.Column(db.Integer, db.ForeignKey('tbl_good.id'), nullable=False)
	
	user_pay = db.relationship("User", backref="payment")  # 方便查询(交易记录对应的用户)
	good_pay = db.relationship("Good", backref="payment")  # 方便查询(交易记录对应的商品)
