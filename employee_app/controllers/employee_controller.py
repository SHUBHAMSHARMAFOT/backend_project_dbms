from flask import request
from employee_app.services.employee_service import EmployeeService
from employee_app.views.employee_view import EmployeeView
from shared.models.employee_model import Employee

class EmployeeController:
    # Create a new employee
    @staticmethod
    def create_employee():
        data = request.get_json()
        name = data.get('name')
        contact_info = data.get('contact_info')
        role = data.get('role')
        department_id = data.get('department_id')


        # Call service to create a employee
        employee = EmployeeService.create_employee(name, contact_info, role, department_id)

        return EmployeeView.render_employee(employee), 201

    # Get employee details by employee ID
    @staticmethod
    def get_employee_by_id(employee_id):
        employee = EmployeeService.get_employee_by_employee_id(employee_id)
        if employee:
            return EmployeeView.render_employee(employee), 200
        else:
            return EmployeeView.render_error("Employee not found"), 404

    # Get all employees
    @staticmethod
    def get_all_employees():
        employees = EmployeeService.get_all_employees()
        return EmployeeView.render_employees(employees), 200

    # Delete employee by employee ID
    @staticmethod
    def delete_employee(employee_id):
        employee = EmployeeService.delete_employee(employee_id)
        if employee:
            return EmployeeView.render_employee(employee), 200
        else:
            return EmployeeView.render_error("Employee not found"), 404

