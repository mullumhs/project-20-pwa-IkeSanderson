from flask import render_template, request, redirect, url_for, flash
from models import db, Fish # Also import your database model here


# Define your routes inside the 'init_routes' function
# Feel free to rename the routes and functions as you see fit
# You may need to use multiple methods such as POST and GET for each route
# You can use render_template or redirect as appropriate
# You can also use flash for displaying status messages

def init_routes(app):

    @app.route('/', methods=['GET'])
    def get_items():
        fishes = Fish.query.all()
        return render_template('index.html', message='Displaying all items', fishes = fishes)



    @app.route('/add', methods=['GET','POST'])
    def create_item():
        if request.method == 'POST':
            new_fish = Fish(
                common_name = request.form['common_name'],
                scientific_name = request.form['scientific_name'],
                species = request.form['species'],
                shape = request.form['shape'],
                avg_length = int(request.form['avg_length']),
                avg_lifespan = int(request.form['avg_lifespan']),
                water_type = request.form['water_type'],
                has_legs = request.form['has_legs'],
            )

            db.session.add(new_fish)
            db.session.commit()
            return redirect(url_for('get_items'))
        
        return render_template('add.html')


    @app.route('/update', methods=['Get','POST'])
    def update_item():
        # This route should handle updating an existing item identified by the given ID.
        

        if request.method == 'POST':
            id = request.form['id']
            fish = Fish.query.get(id)
            fish.common_name = request.form['common_name']
            fish.scientific_name = request.form['scientific_name']
            fish.species = request.form['species']
            fish.shape = request.form['shape']
            fish.avg_length = int(request.form['avg_length'])
            fish.avg_lifespan = int(request.form['avg_lifespan'])
            fish.water_type = request.form['water_type']
            fish.has_legs = request.form['has_legs']
            
            db.session.commit()
            return redirect(url_for('get_items'))
        
        id = request.args.get("id")
        fish = db.get_or_404(Fish, id)
        print(fish)
        return render_template('update.html', fish=fish)



    @app.route('/delete', methods=['GET'])
    def delete_item():
        # This route should handle deleting an existing item identified by the given ID.
        id = request.args.get("id")
        fish = db.get_or_404(Fish, id)
        print(fish)
        db.session.delete(fish)
        db.session.commit()
        return redirect(url_for('get_items'))
    
    @app.route('/search',methods=['GET', 'POST'])
    def search_fish():
        if request.method == 'POST':
            print("Search!!!!")
            query = request.form['search']
            return redirect(url_for('search_fish', query = query  ))
       
        query = request.args.get('query')
        fishes = db.session.query(Fish).filter(Fish.common_name.like(query)).all()
        print(query)
        return render_template('search.html', fishes=fishes, query=query)
