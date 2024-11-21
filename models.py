from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# Define your database model here
# Example: class Item(db.Model):
class Fish(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    common_name = db.Column(db.String(100), nullable = False)
    scientific_name = db.Column(db.String(100))
    species = db.Column(db.String(100))
    water_type = db.Column(db.String(100))
    avg_length = db.Column(db.Integer)
    avg_lifespan = db.Column(db.Integer)
    shape = db.Column(db.String(100))
    legs = db.Column(db.Boolean, default = False)
    