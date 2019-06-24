from server import db, ma


class Invoice(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime(timezone=True))
    invoice_ref = db.Column(db.Integer, nullable=False)
    item_breakdown = db.Column(db.PickleType)
    cgst = db.Column(db.Integer, nullable=False)
    sgst = db.Column(db.Integer, nullable=False)
    client_id = db.Column(db.Integer,
                          db.ForeignKey('client.id'),
                          nullable=False)


class InvoiceSchema(ma.ModelSchema):
    class Meta:
        model = Invoice