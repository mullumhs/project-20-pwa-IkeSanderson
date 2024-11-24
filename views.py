from flask import render_template, request, redirect, url_for, flash
from models import db # Also import your database model here
from views import Fish

# Define your routes inside the 'init_routes' function
# Feel free to rename the routes and functions as you see fit
# You may need to use multiple methods such as POST and GET for each route
# You can use render_template or redirect as appropriate
# You can also use flash for displaying status messages

def init_routes(app):

    @app.route('/', methods=['GET'])
    def get_items():
        # This route should retrieve all items from the database and display them on the page.
        return render_template('index.html', message='Displaying all items')



    @app.route('/add', methods=['GET','POST'])
    def create_item():
        if request.method == 'POST':
            new_fish = Fish(
                common_name = request.form['common_name'],
                scientific_name = request.form['scientific_name'],
                species = request.form['species'],
                shape = request.form['shape'],
                avg_length = int(request.form['avg_length']),
                avg_lifespan = int(request.form['avg_lifespan'])
                water_type = request.form['water_type'],
                has_legs = request.form['has_legs'],
            )

            db.session.add(new_fish)
            db.session.commit()
            return render_template('index.html', message='Fish added successfully')
        
        return render_template('add.html')


    @app.route('/update', methods=['POST'])
    def update_item():
        # This route should handle updating an existing item identified by the given ID.
        return render_template('index.html', message=f'Item updated successfully')



    @app.route('/delete', methods=['POST'])
    def delete_item():
        # This route should handle deleting an existing item identified by the given ID.
        return render_template('index.html', message=f'Item deleted successfully')