from app import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))

    def __repr__(self):
        return f"<User {self.username}>"


class Books(db.Model):
    __tablename__ = "books"
    id = db.Column(db.Integer, primary_key=True)
    isbn = db.Column(db.String(10))
    title = db.Column(db.String(100))
    author = db.Column(db.String)
    year = db.Column(db.Integer)

    def __repr__(self):
        return f"<Books {self.isbn}, {self.title}, {self.author}, {self.year}>"
