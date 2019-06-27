from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_wtf import CsrfProtect
from flask_cors import CORS
from flask_compress import Compress

from server.config import Config




db = SQLAlchemy()
ma = Marshmallow()
csrf = CsrfProtect()
cors = CORS()
compress = Compress()


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    ma.init_app(app)
    csrf.init_app(app)
    cors.init_app(app)
    compress.init_app(app)

    # Blueprints
    from server.client.routes import client
    from server.invoice.routes import invoice
    from server.payment_history.routes import payment_history

    app.register_blueprint(client, url_prefix='/client')
    app.register_blueprint(invoice, url_prefix='/invoice')
    app.register_blueprint(payment_history, url_prefix='/payment')

    return app