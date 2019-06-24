from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from server.config import Config

db = SQLAlchemy()
ma = Marshmallow()


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    ma.init_app(app)

    from server.client.routes import client
    from server.invoice.routes import invoice
    from server.payment_history.routes import payment_history

    app.register_blueprint(client, url_prefix='/client')
    app.register_blueprint(invoice, url_prefix='/invoice')
    app.register_blueprint(payment_history, url_prefix='/payment')

    return app