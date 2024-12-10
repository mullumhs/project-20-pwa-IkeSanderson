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
    has_legs = db.Column(db.String(100))
    image = db.Column(db.String(200))
    
    def __str__(self):
        display = f"""
            {self.scientific_name}
            {self.species}
            {self.shape}
            {self.water_type}
            {self.avg_length}
            {self.avg_lifespan}
            {self.has_legs}


        """
        return display