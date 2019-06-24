from server import db, ma


class PaymentHistory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime(timezone=True), nullable=False)
    payment_mode = db.Column(db.String(100), nullable=False)
    amount = db.Column(db.Integer, nullable=False)
    notes = db.Column(db.String(255))
    client_id = db.Column(db.Integer,
                          db.ForeignKey('client.id'),
                          nullable=False)


class PaymentHistorySchema(ma.ModelSchema):
    class Meta:
        model = PaymentHistory