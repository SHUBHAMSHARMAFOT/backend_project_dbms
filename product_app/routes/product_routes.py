from flask import Blueprint
from product_app.controllers.product_controller import DepartmentController,ProductController

product_bp = Blueprint('product_bp', __name__)

@product_bp.route('/api/departments', methods=['GET'])
def get_all_departments():
    return DepartmentController.get_all_departments()

@product_bp.route('/api/departments/<int:department_id>', methods=['GET'])
def get_department(department_id):
    return DepartmentController.get_department(department_id)

@product_bp.route('/api/departments', methods=['POST'])
def create_department():
    return DepartmentController.create_department()

@product_bp.route('/api/departments/<int:department_id>', methods=['PUT'])
def update_department(department_id):
    return DepartmentController.update_department(department_id)

@product_bp.route('/api/departments/<int:department_id>', methods=['DELETE'])
def delete_department(department_id):
    return DepartmentController.delete_department(department_id)



@product_bp.route('/api/products', methods=['GET'])
def get_all_products():
    return ProductController.get_all_products()

@product_bp.route('/api/products/<int:product_id>', methods=['GET'])
def get_product(product_id):
    return ProductController.get_product(product_id)

@product_bp.route('/api/products', methods=['POST'])
def create_product():
    return ProductController.create_product()

@product_bp.route('/api/products/<int:product_id>', methods=['PUT'])
def update_product(product_id):
    return ProductController.update_product(product_id)

@product_bp.route('/api/products/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
    return ProductController.delete_product(product_id)

@product_bp.route('/api/products/department/<int:department_id>', methods = ['GET'])
def get_product_by_department_id(department_id):
    return ProductController.get_product_by_department_id(department_id)




