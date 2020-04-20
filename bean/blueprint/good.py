# -*- coding:utf-8 -*-


from . import app_good
from models.forms import GoodForm
from models.db_bean import Good, GoodType, User
from app import db
from flask import flash, redirect, url_for, render_template, session, request


@app_good.route("/add", methods=["GET", "POST"])
def add():
	"""新增商品"""
	user_name = session.get("user_name")
	good_form = GoodForm()
	if good_form.validate_on_submit():
		good_name = good_form.good_name.data
		good_type = good_form.type.data
		price = good_form.price.data
		stock = good_form.stock.data
		goods = [g.good_name for g in Good.query.all()]
		if good_name not in goods:
			good = Good(good_name=good_name, type=good_type, price=price, stock=stock)
			db.session.add(good)
			db.session.commit()
			db.session.remove()
			
			flash("add new good!")
			return redirect(url_for("app_index.index"))
		else:
			flash("good's name has been existed！")
	return render_template("good.html", good_form=good_form, user_name=user_name)


@app_good.route("/delete")
def delete():
	"""删除商品"""
	good_id = request.args.get("good_id")
	if good_id:
		good = Good.query.get(good_id)
		db.session.delete(good)
		db.session.commit()
		db.session.remove()
		flash("delete good！")
		return redirect(url_for("app_index.index"))
	return render_template("index.html")


@app_good.route("/view/<good_id>")
def view(good_id):
	"""商品详细信息"""
	user_name = session.get("user_name")
	goods = Good.query.all()
	good_info = Good.query.filter_by(id=good_id).first()
	good_types = [g.type_name for g in GoodType.query.all()]
	if user_name:
		user = User.query.filter_by(user_name=user_name).first()
		price = []
		for cart in user.cart:
			price.append(float(cart.goods.price))
		total_money = sum(price)
		return render_template("index.html", user_name=user_name, user=user, goods=goods, good_info=good_info,
		                       total_money=total_money, good_types=good_types)
	else:
		return render_template("index.html", user_name="guest", goods=goods, good_info=good_info, good_types=good_types)
