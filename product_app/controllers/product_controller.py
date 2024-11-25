from flask import request
from product_app.services.product_service import DepartmentService
from product_app.services.product_service import ProductService
from product_app.views.product_view import DepartmentView,ProductView

class DepartmentController:
    @staticmethod
    def get_all_departments():
        departments = DepartmentService.get_all_departments()
        return DepartmentView.render_departments(departments), 200

    @staticmethod
    def get_department(department_id):
        department = DepartmentService.get_department_by_id(department_id)
        if not department:
            return DepartmentView.render_error('department not found'), 404
        return DepartmentView.render_department(department), 200

    @staticmethod
    def create_department():
        try:
            data = request.get_json()
            department_name = data.get('department_name')
            

            department = DepartmentService.create_department(department_name)
            return DepartmentView.render_success('Department created successfully', department.department_id), 201

        except ValueError as e:
            return DepartmentView.render_error(str(e)), 400


    @staticmethod
    def delete_department(department_id):
        department = DepartmentService.delete_department(department_id)
        if department:
            return DepartmentView.render_success('department deleted successfully', department.department_id), 200
        return DepartmentView.render_error('department not found'), 404

    
class ProductController:
    @staticmethod
    def get_all_products():
        products = ProductService.get_all_products()
        return ProductView.render_products(products), 200

    @staticmethod
    def get_product(product_id):
        product = ProductService.get_product_by_id(product_id)
        if not product:
            return ProductView.render_error('product not found'), 404
        return ProductView.render_product(product), 200

    @staticmethod
    def create_product():
        try:
            data = request.get_json()
            name = data.get('name')
            brand = data.get('brand')
            price = data.get('price')
            stock = data.get('stock')
            department_id = data.get('department_id')

            product = ProductService.create_product(name,brand,price,stock,department_id)
            return ProductView.render_success('Product created successfully', product.product_id), 201

        except ValueError as e:
            return ProductView.render_error(str(e)), 400


    @staticmethod
    def delete_product(product_id):
        product = ProductService.delete_product(product_id)
        if product:
            return ProductView.render_success('product deleted successfully', product.product_id), 200
        return ProductView.render_error('product not found'), 404

    @staticmethod
    def get_product_by_department_id(department_id):
        product = ProductService.get_product_by_department_id(department_id)
        if not product:
            return ProductView.render_error('product not found'), 404
        return ProductView.render_product(product), 200