from flask import Flask
from routes.listings import listings_blueprint
from routes.users import users_blueprint
from routes.search import search_blueprint
from database import init_db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///realestate.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize Database
init_db(app)

# Register Blueprints
app.register_blueprint(listings_blueprint, url_prefix="/listings")
app.register_blueprint(users_blueprint, url_prefix="/users")
app.register_blueprint(search_blueprint, url_prefix="/search")

if __name__ == "__main__":
    app.run(debug=True)
