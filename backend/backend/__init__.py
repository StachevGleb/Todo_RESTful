from flask import Flask, jsonify
import flask_migrate
import flask_sqlalchemy
from flask_cors import CORS
app = Flask(__name__)

app.config.from_object(__name__)

CORS(app, resources={r"/*": {'origin': "*"}})

# db_info = {'host': 'localhost',
#            'database': 'taskstore',
#            'psw': 'Lena091165',
#            'user': 'postgres',
#            'port': '5432'}
#
# app.config[
#     'SQLALCHEMY_DATABASE_URI'] = f"postgresql://{db_info['user']}:{db_info['psw']}@{db_info['host']}/{db_info['database']}"


db_info = {'host': 'dpg-cjaf095m2m9c73cvpn7g-a.frankfurt-postgres.render.com',
           'database': 'todorestful',
           'psw': 'AoPYcgE3Vk8iJWw5LWli7CiWLA7o2aZg',
           'user': 'stachev',
           'port': '5432'}

app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://stachev:AoPYcgE3Vk8iJWw5LWli7CiWLA7o2aZg@dpg-cjaf095m2m9c73cvpn7g-a.frankfurt-postgres.render.com/todorestful"

# postgresql://stachev:AoPYcgE3Vk8iJWw5LWli7CiWLA7o2aZg@dpg-cjaf095m2m9c73cvpn7g-a.frankfurt-postgres.render.com/todorestful

db = flask_sqlalchemy.SQLAlchemy(app)
migrate = flask_migrate.Migrate(app, db)

from backend import routes, models
