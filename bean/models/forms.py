# -*- coding:utf-8 -*-


from flask_wtf import Form
from wtforms import StringField, PasswordField, SubmitField, BooleanField, DecimalField, IntegerField, SelectField
from wtforms.validators import DataRequired, EqualTo, Regexp
from models.db_bean import GoodType


class RegisterForm(Form):
	"""用户注册表单"""
	user_name = StringField(label=u"username", validators=[DataRequired(u"User name cannot be empty！")])
	password = PasswordField(label=u"password", validators=[DataRequired(u"password cannot be empty!"), Regexp(
		"^(?=.*[0-9])(?=.*[a-zA-Z])(?=.*[!@#$_&*+-])[0-9a-zA-Z!@#$_&*+-]{8,18}$",
		message=u"wrong password!")])
	check_password = PasswordField(label=u"repeat password",
	                               validators=[DataRequired(u"password cannot be empty!"), EqualTo("password", message="passwords are inconsistent"),
	                                           Regexp(
		                                           "^(?=.*[0-9])(?=.*[a-zA-Z])(?=.*[!@#$_&*+-])[0-9a-zA-Z!@#$_&*+-]{8,18}$",
		                                           message=u"wrong password！")])
	pay_password = PasswordField(label=u"pay password", validators=[DataRequired(u'password cannot be empty!'), Regexp(
		"^(?=.*[0-9])(?=.*[a-zA-Z])(?=.*[!@#$_&*+-])[0-9a-zA-Z!@#$_&*+-]{8,18}$",
		message=u"wrong password!")])
	check_pay_password = PasswordField(label=u"confirm password",
	                                   validators=[DataRequired(u"pay password cannot be empty!"),
	                                               EqualTo("pay_password", message=u"passwords are inconsistent"),
	                                               Regexp(
		                                               "^(?=.*[0-9])(?=.*[a-zA-Z])(?=.*[!@#$_&*+-])[0-9a-zA-Z!@#$_&*+-]{8,18}$",
		                                               message=u"wrong password")])
	remember_me = BooleanField(label=u'remember', default=False)
	submit = SubmitField(label=u"register")


class UserForm(Form):
	"""用户登录表单"""
	user_name = StringField(label=u"username", validators=[DataRequired(u"用户名不能为为空！")])
	password = PasswordField(label=u"password", validators=[DataRequired(u"!"), Regexp(
		"^(?=.*[0-9])(?=.*[a-zA-Z])(?=.*[!@#$_&*+-])[0-9a-zA-Z!@#$_&*+-]{8,18}$",
		message=u"wrong!")])
	check_password = PasswordField(label=u"confirm password",
	                               validators=[DataRequired(u"assword cannot be empty!"), EqualTo("password", message=u"passwords are inconsistent"),
	                                           Regexp(
		                                           "^(?=.*[0-9])(?=.*[a-zA-Z])(?=.*[!@#$_&*+-])[0-9a-zA-Z!@#$_&*+-]{8,18}$",
		                                           message=u"wrong password！")])
	remember_me = BooleanField(label=u'remember', default=False)
	submit = SubmitField(label=u"login")


class GoodTypeForm(Form):
	"""商品表单"""
	type_name = StringField(label=u"good_type", validators=[DataRequired(u"！Can not be empty")])
	submit = SubmitField(label=u"add")


class GoodForm(Form):
	"""商品表单"""
	good_name = StringField(label=u"good_name", validators=[DataRequired(u"Can not be empty!")])
	try:
		good_types = [(g.id, (g.id, g.type_name)) for g in GoodType.query.all()]
		type = SelectField(label=u"good_type", choices=good_types, coerce=int, validators=[DataRequired(u"Can not be empty！")])
	except Exception:
		pass
	price = DecimalField(label=u"good_price", validators=[DataRequired(u"add failed！")])
	stock = IntegerField(label=u"good_", validators=[DataRequired(u"add failed！")])
	
	submit = SubmitField(label=u"add")


class PaymentForm(Form):
	"""付款表单"""
	pay_password = PasswordField(label=u"pay password", validators=[DataRequired(u"empty!")])
	submit = SubmitField(label=u"check out")
