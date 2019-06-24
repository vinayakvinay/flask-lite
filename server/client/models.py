from server import db, ma


class Client(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    gst = db.Column(db.String(30))
    address_line1 = db.Column(db.String(50))
    address_line2 = db.Column(db.String(50))
    phone = db.Column(db.String(15))
    pending_amount = db.Column(db.Integer, default=0)
    invoices = db.relationship('Invoice', backref='client', lazy=True)
    payment_history = db.relationship('PaymentHistory',
                                      backref='client',
                                      lazy=True)


class ClientSchema(ma.ModelSchema):
    class Meta:
        model = Client