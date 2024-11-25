class DepartmentView:
    @staticmethod
    def render_department(department):
        return {
            "department_id": department.department_id, 
            "department_name": department.department_name
            }

    @staticmethod
    def render_departments(departments):
        return [DepartmentView.render_department(department) for department in departments]

    @staticmethod
    def render_error(message):
        return {"error": message}

    @staticmethod
    def render_success(message, department_id=None):
        response = {"message": message}
        if department_id:
            response["department_id"] = department_id
        return response
    

class ProductView:
    @staticmethod
    def render_product(product):
        return{
        "product_id": product.product_id,
        "name": product.name,
        "brand": product.brand,
        "price": product.price,
        "stock": product.stock,
        "department_id": product.department_id,
    }

    @staticmethod
    def render_products(product):
         return [ProductView.render_product(product) for product in product]


    @staticmethod
    def render_error(message):
        return {"error": message}

    @staticmethod
    def render_success(message, product_id=None):
        response = {"message": message}
        if product_id:
            response["Product_id"] = product_id
        return response