# -*- coding:utf-8 -*-


from . import app_payment
from flask import render_template, session, flash, redirect, url_for
from models.forms import PaymentForm
from models.db_bean import User, Good, ShoppingCart, Payment
from app import db


@app_payment.route("/add/<good_name>", methods=["GET", "POST"])
def add(good_name):
	pay_form = PaymentForm()
	user_name = session.get("user_name")
	user = User.query.filter_by(user_name=user_name).first()
	good = Good.query.filter_by(good_name=good_name).first()
	price = good.price
	if user:
		if pay_form.validate_on_submit():
			if pay_form.pay_password.data == user.pay_password:
				payment = Payment(user_id=user.id, good_id=good.id)
				db.session.add(payment)
				db.session.commit()
				flash("付款成功!")
				cart_finished = ShoppingCart.query.filter_by(user_id=user.id, good_id=good.id).first()
				db.session.delete(cart_finished)
				db.session.commit()
				db.session.remove()
				return redirect(url_for("app_index.index"))
			else:
				flash("支付密码错误！")
	else:
		flash("请登录后再尝试！")
		return redirect(url_for("app_index.index"))
	return render_template("payment.html", pay_form=pay_form, user_name=user_name, good_name=good_name, price=price)


@app_payment.route("/add_directly/<good_name>", methods=["GET", "POST"])
def add_directly(good_name):
	pay_form = PaymentForm()
	user_name = session.get("user_name")
	user = User.query.filter_by(user_name=user_name).first()
	good = Good.query.filter_by(good_name=good_name).first()
	price = good.price
	if user:
		if pay_form.validate_on_submit():
			if pay_form.pay_password.data == user.pay_password:
				payment = Payment(user_id=user.id, good_id=good.id)
				db.session.add(payment)
				db.session.commit()
				flash("pay succeed!")
				return redirect(url_for("app_index.index"))
			else:
				flash("wrong password！")
	else:
		flash("please login！")
		return redirect(url_for("app_index.index"))
	return render_template("payment.html", pay_form=pay_form, user_name=user_name, good_name=good_name, price=price)
