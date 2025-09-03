from db.db import db

class Order(db.Model):
    __tablename__ = 'orders'
    
    id = db.Column(db.Integer, primary_key=True)
    userName = db.Column(db.String(255), nullable=False)
    userEmail = db.Column(db.String(255), nullable=False)
    saleTotal = db.Column(db.DECIMAL(10,2), nullable=False)
    date = db.Column(db.DateTime, nullable=False)

    def __init__(self, userName, userEmail, saleTotal):
        self.userName = userName
        self.userEmail = userEmail
        self.saleTotal = saleTotal
        self.date = db.func.current_timestamp()

    def to_dict(self):
        return {
            'id': self.id,
            'userName': self.userName,
            'userEmail': self.userEmail,
            'saleTotal': self.saleTotal,
            'date': self.date
        }
