from flask import render_template, request, redirect, url_for, flash
from models import db, Fish # Also import your database model here



# Displays all the fish in the data base (home page)
def init_routes(app):

    @app.route('/', methods=['GET'])
    def get_items():
        query = request.args.get('query')
        if query == None:
            fishes = Fish.query.all()
        else:
            fishes = db.session.query(Fish).filter(Fish.common_name.like(query)).all()
        return render_template('index.html', message='Displaying all items', fishes = fishes)



    @app.route('/add', methods=['GET','POST'])
    # Uses the add form to create a new fish for the database 
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
                image = request.form['image'],
            )

            db.session.add(new_fish)
            db.session.commit()
            return redirect(url_for('get_items'))
        
        return render_template('add.html')


    @app.route('/update', methods=['Get','POST'])
    def update_item():
        # This route updates an existing item identified by the given ID.
        

        if request.method == 'POST':
            # Updates the Fish's information from the form, redirects to the index page 
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
            fish.image = request.form['image']
            
            db.session.commit()
            return redirect(url_for('get_items'))
        # Finds the Fish by ID and returns the update page
        id = request.args.get("id")
        fish = db.get_or_404(Fish, id)
        print(fish)
        return render_template('update.html', fish=fish)



    @app.route('/delete', methods=['GET'])
    def delete_item():
        # Deleting an existing Fish identified by the given ID.
        id = request.args.get("id")
        fish = db.get_or_404(Fish, id)
        print(fish)
        db.session.delete(fish)
        db.session.commit()
        return redirect(url_for('get_items'))
    
    @app.route('/search',methods=['GET', 'POST'])
    def search_fish():
        # Searches existing Fish by common name and overides the index page with the query
        if request.method == 'POST':
            print("Search!!!!")
            query = request.form['search']
            return redirect(url_for('get_items', query = query  ))
       
        query = request.args.get('query')
        
        fishes = db.session.query(Fish).filter(Fish.common_name.like(query)).all()
        print(query)
        return render_template('search.html', fishes=fishes, query=query)
