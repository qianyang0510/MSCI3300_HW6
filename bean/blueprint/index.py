# -*- coding:utf-8 -*-


from . import app_index
from models.db_bean import User, GoodType, Good, ShoppingCart
from flask import render_template, session


@app_index.route("/")
def index():
	"""首页-展示商品"""
	user_name = session.get("user_name")
	goods = Good.query.all()
	good_types = [g.type_name for g in GoodType.query.all()]
	if user_name:
		user = User.query.filter_by(user_name=user_name).first()
		price = []
		for cart in user.cart:
			price.append(float(cart.goods.price))
		total_money = "{:.2f}".format(sum(price))
		return render_template("index.html", user_name=user_name, user=user, goods=goods,
		                       total_money=total_money, good_types=good_types)
	else:
		return render_template("index.html", user_name="guest", goods=goods, good_types=good_types)


@app_index.route("/payment_records")
def payment_records():
	"""购物记录"""
	user = User.query.filter_by(user_name=session.get("user_name")).first()
	price = []
	for payment in user.payments:
		price.append(float(payment.good_pay.price))
	total_money = "{:.2f}".format(sum(price))
	return render_template("payment_records.html", user=user, total_numbers=len(price), total_money=total_money)


@app_index.route("/view_by_type/<type_name>")
def view_by_type(type_name):
	user_name = session.get("user_name")
	good_type = GoodType.query.filter_by(type_name=type_name).first()
	goods = Good.query.filter_by(type=good_type.id).all()
	good_types = [g.type_name for g in GoodType.query.all()]
	if user_name:
		user = User.query.filter_by(user_name=user_name).first()
		price = []
		for cart in user.cart:
			price.append(float(cart.goods.price))
		total_money = "{:.2f}".format(sum(price))
		return render_template("index.html", user_name=user_name, user=user, goods=goods,
		                       total_money=total_money, good_types=good_types)
	else:
		return render_template("index.html", user_name="guest", goods=goods, good_types=good_types)
