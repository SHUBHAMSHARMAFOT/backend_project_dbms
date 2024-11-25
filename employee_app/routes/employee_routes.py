from flask import Blueprint
from employee_app.controllers.employee_controller import EmployeeController

# Create a blueprint for Employee routes
employee_bp = Blueprint('employee', __name__)

# Employee Routes

# Get all employees (GET)
@employee_bp.route('/employees', methods=['GET'])
def get_all_employees():
    return EmployeeController.get_all_employees()

# Get a specific employee by ID (GET)
@employee_bp.route('/employee/<int:employee_id>', methods=['GET'])
def get_employee(employee_id):
    return EmployeeController.get_employee_by_id(employee_id)

# Create a employee (POST)
@employee_bp.route('/employee', methods=['POST'])
def create_employee():
    return EmployeeController.create_employee()

# Delete a employee by ID (DELETE)
@employee_bp.route('/employee/<int:employee_id>', methods=['DELETE'])
def delete_employee(employee_id):
    return EmployeeController.delete_employee(employee_id)


