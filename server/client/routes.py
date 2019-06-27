from flask import Blueprint

client = Blueprint('client', __name__)


@client.route('/get_all')
def get_all():
    return 'Hello PY..!'