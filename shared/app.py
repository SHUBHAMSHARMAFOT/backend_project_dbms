from flask import Flask
from shared.utils.db_utils import db
from shared.utils.db_utils import migrate
from shared.models.employee_model import Employee
from shared.models.product_model import Department,Product



# Initialize the Flask App
app = Flask(__name__)

# Initialization configuration
# (later move this configuration to config/config.py)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:shubham@localhost/dbms_project'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
migrate.init_app(app, db)

