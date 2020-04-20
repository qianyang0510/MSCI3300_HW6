# -*- coding:utf-8 -*-


from . import app_goodType
from flask import render_template, flash, redirect, url_for, session
from models.forms import GoodTypeForm
from models.db_bean import GoodType
from app import db


@app_goodType.route("/add", methods=["GET", "POST"])
def add():
	type_form = GoodTypeForm()
	if type_form.validate_on_submit():
		type_name = type_form.type_name.data
		type_names = [g.type_name for g in GoodType.query.all()]
		if type_name not in type_names:
			good_type = GoodType(type_name=type_name)
			db.session.add(good_type)
			db.session.commit()
			db.session.remove()
			flash("add new good！")
			redirect(url_for("app_index.index"))
		else:
			flash("good type has been exsit！")
	return render_template("good_type.html", type_form=type_form, user_name=session.get("user_name"))
