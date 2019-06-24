#!/usr/bin/env python
import os
import subprocess

from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager, Shell

from server import create_app, db
from server.invoice.models import Invoice
from server.payment_history.models import PaymentHistory
from server.client.models import Client
from server.config import Config

app = create_app(Config)
manager = Manager(app)
migrate = Migrate(app, db)


def make_shell_context():
    return dict(app=app,
                db=db,
                Client=Client,
                Invoice=Invoice,
                PaymentHistory=PaymentHistory)


manager.add_command('shell', Shell(make_context=make_shell_context))
manager.add_command('db', MigrateCommand)


@manager.command
def test():
    """Run the unit tests."""
    import unittest

    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)


@manager.command
def reset_db():
    """
    Recreates a local database. You probably should not use this on
    production.
    """
    db.drop_all()
    db.create_all()
    db.session.commit()


@manager.command
def format():
    """Runs the yapf and isort formatters over the project."""
    yapf = 'yapf -r -i *.py server/'
    print('Running {}'.format(yapf))
    subprocess.call(yapf, shell=True)


if __name__ == '__main__':
    manager.run()
