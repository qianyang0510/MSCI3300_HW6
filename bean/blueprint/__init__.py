# -*- coding:utf-8 -*-


from flask import Blueprint

app_index = Blueprint("app_index", __name__)
app_user = Blueprint("app_user", __name__, url_prefix="/user")
app_good = Blueprint("app_good", __name__, url_prefix="/good")
app_cart = Blueprint("app_cart", __name__, url_prefix="/cart")
app_payment = Blueprint("app_payment", __name__, url_prefix="/payment")
app_goodType = Blueprint("app_goodType", __name__, url_prefix="/goodType")
from .index import index, payment_records, view_by_type
from .user import login, register, logout
from .good import add, delete, view
from .cart import add, delete
from .payment import add, add_directly
from .goodtype import add
