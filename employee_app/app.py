import sys, os
sys.path.append(os.getcwd())

from flask import Flask
from employee_app.routes.employee_routes import employee_bp
from shared.utils.db_utils import db
  
from shared.models.product_model import Product,Department
from shared.models.employee_model import Employee
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:shubham@localhost/dbms_project'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

db.init_app(app)

app.register_blueprint(employee_bp)

if __name__ == '__main__':
    app.run(debug=True, port=5002)
