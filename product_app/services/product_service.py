from shared.models.product_model import Department
from shared.utils.db_utils import db
from shared.models.product_model import Product
from product_app.views.product_view import DepartmentView,ProductView
from datetime import datetime

class DepartmentService:
    @staticmethod
    def create_department(department_name):
        # Step 1: Check if a department with the same name and license number already exists
        existing_department = Department.query.filter_by(department_name=department_name).first()
        if existing_department:
            raise ValueError(f"A department with the name '{department_name}' already exists.")

        # Step 2: Create a new department if no existing department is found
        new_department = Department(department_name=department_name)
        db.session.add(new_department)
        db.session.commit()

        return new_department



    @staticmethod
    def get_department_by_id(department_id):
        return Department.query.filter_by(department_id=department_id).first()

    @staticmethod
    def get_departments_by_user(user_id):
        return Department.query.filter_by(user_id=user_id).all()

    @staticmethod
    def get_all_departments():
        return Department.query.order_by(Department.department_id.desc()).all()

    @staticmethod
    def delete_department(department_id):
        department = Department.query.filter_by(department_id=department_id).first()
        if department:
            db.session.delete(department)
            db.session.commit()
        return department

class ProductService:
    @staticmethod
    def create_product(name,brand,price,stock,department_id):
        existing_product = Product.query.filter_by(name=name).first()
        if existing_product:
            raise ValueError(f"A department with the name '{name}' already exists.")

        # Step 2: Create a new department if no existing department is found
        new_product = Product(name=name, brand=brand, price=price, stock=stock, department_id=department_id)
        db.session.add(new_product)
        db.session.commit()

        return new_product
    
    @staticmethod
    def get_product_by_id(product_id):
        return Product.query.filter_by(product_id=product_id).first()
    
    @staticmethod
    def get_product_by_department_id(department_id):
        return Product.query.filter_by(department_id=department_id).all()
    
    @staticmethod
    def get_all_products():
        return Product.query.order_by(Product.product_id.desc()).all()
    
    
    
    @staticmethod
    def delete_product(product_id):
        product = Product.query.filter_by(product_id=product_id).first()
        if product:
            db.session.delete(product)
            db.session.commit()
        return product

