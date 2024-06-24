from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from sqlalchemy_serializer import SerializerMixin

# Define the naming convention for the database
convention = {
    "ix": "ix_%(column_0_label)s",
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(constraint_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s"
}

metadata = MetaData(naming_convention=convention)
db = SQLAlchemy(metadata=metadata)

# Define Zookeeper model
class Zookeeper(db.Model, SerializerMixin):
    __tablename__ = 'zookeepers'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True, nullable=False)
    birthday = db.Column(db.Date, nullable=False)

    animals = db.relationship('Animal', back_populates='zookeeper', cascade="all, delete-orphan")

    def __repr__(self):
        return f'<Zookeeper {self.name}, born on {self.birthday}>'

# Define Enclosure model
class Enclosure(db.Model, SerializerMixin):
    __tablename__ = 'enclosures'

    id = db.Column(db.Integer, primary_key=True)
    environment = db.Column(db.String, nullable=False)
    open_to_visitors = db.Column(db.Boolean, default=True)

    animals = db.relationship('Animal', back_populates='enclosure', cascade="all, delete-orphan")

    def __repr__(self):
        return f'<Enclosure {self.environment}, open to visitors: {self.open_to_visitors}>'

# Define Animal model
class Animal(db.Model, SerializerMixin):
    __tablename__ = 'animals'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True, nullable=False)
    species = db.Column(db.String, nullable=False)

    zookeeper_id = db.Column(db.Integer, db.ForeignKey('zookeepers.id'), nullable=False)
    enclosure_id = db.Column(db.Integer, db.ForeignKey('enclosures.id'), nullable=False)

    zookeeper = db.relationship('Zookeeper', back_populates='animals')
    enclosure = db.relationship('Enclosure', back_populates='animals')

    def __repr__(self):
        return f'<Animal {self.name}, a {self.species}>'
