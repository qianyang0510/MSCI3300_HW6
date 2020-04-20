# -*- coding:utf-8 -*-


from . import app_user
from app import db
from models.db_bean import User
from models.forms import UserForm, RegisterForm
from flask import render_template, flash, session, redirect, url_for


@app_user.route("/register", methods=["GET", "POST"])
def register():
	"""
	注册
	"""
	user_form = RegisterForm()
	if user_form.validate_on_submit():
		user_name = user_form.user_name.data
		password = user_form.password.data
		pay_password = user_form.pay_password.data
		users = User.query.all()
		if user_name in [user.user_name for user in users]:
			flash("usrname has been register")
		elif user_name and password:
			user = User(user_name=user_name, password=password, pay_password=pay_password)
			db.session.add(user)
			db.session.commit()
			db.session.remove()
			flash("register succeed！")
			return redirect(url_for("app_index.index"))
		else:
			flash("register failed！")
	return render_template("register.html", user_form=user_form)


@app_user.route("/login", methods=["GET", "POST"])
def login():
	"""
	登录
	"""
	user_form = UserForm()
	user_name = user_form.user_name.data
	password = user_form.password.data
	
	if user_form.validate_on_submit():
		user = User.query.filter_by(user_name=user_name).first()
		if user:
			if password == user.password:
				session['user_name'] = user_name
				flash("%s, welcome！" % user_name)
				return redirect(url_for("app_index.index"))
			else:
				flash("wrong password！")
		else:
			flash("no user！")
	return render_template("login.html", user_form=user_form)


@app_user.route("/logout", methods=["GET", "POST"])
def logout():
	"""
	退出
	"""
	user_name = session.get("user_name")
	if user_name:
		session.pop("user_name")
		flash("log out！")
	else:
		flash("must sign in！")
	return redirect(url_for("app_index.index"))
