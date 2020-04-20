# -*- coding:utf-8 -*-


from . import app_cart
from app import db
from models.db_bean import User, ShoppingCart
from flask import session, flash, redirect, url_for


@app_cart.route("/add/<good_id>")
def add(good_id):
	"""添加购物车"""
	user_name = session.get("user_name")
	if user_name:
		user = User.query.filter_by(user_name=user_name).first()
		user_id = user.id
		cart = ShoppingCart(user_id=user_id, good_id=good_id)
		db.session.add(cart)
		db.session.commit()
		db.session.remove()
		
		flash("add to cart！")
		return redirect(url_for("app_index.index"))
	else:
		flash("please sign in！")
		return redirect(url_for("app_index.index"))


@app_cart.route("/delete/<good_id>")
def delete(good_id):
	"""删除购物车"""
	user_name = session.get("user_name")
	if user_name:
		user = User.query.filter_by(user_name=user_name).first()
		cart = ShoppingCart.query.filter_by(user_id=user.id, good_id=good_id).first()
		db.session.delete(cart)
		db.session.commit()
		db.session.remove()
		
		flash("delete from cart！")
		return redirect(url_for("app_index.index"))
	else:
		flash("please retry！")
		return redirect(url_for("app_index.index"))
