# -*- coding:utf-8 -*-


from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from models.myconfig import Config

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)

from blueprint import app_index, app_user, app_good, app_cart, app_payment, app_goodType

app.register_blueprint(app_index)
app.register_blueprint(app_user)
app.register_blueprint(app_good)
app.register_blueprint(app_cart)
app.register_blueprint(app_payment)
app.register_blueprint(app_goodType)
if __name__ == "__main__":
    app.run(host="localhost", port=8000)
