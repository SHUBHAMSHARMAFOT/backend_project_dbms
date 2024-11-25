import sys, os
sys.path.append(os.getcwd())

from flask import Flask
from product_app.routes.product_routes import product_bp
from shared.utils.db_utils import db


from shared.models.product_model import Department,Product
from shared.models.employee_model import Employee
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:shubham@localhost/dbms_project'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

db.init_app(app)

app.register_blueprint(product_bp)

if __name__ == '__main__':
    app.run(debug=True, port=5001)