from shared.models.employee_model import Employee
from shared.utils.db_utils import db
from flask import request

class EmployeeService:
    @staticmethod
    def create_employee(name, contact_info, role, department_id):
        new_employee = Employee(name=name, contact_info=contact_info, role=role, department_id=department_id)
        db.session.add(new_employee)
        db.session.commit()

        return new_employee

    @staticmethod
    def get_employee_by_employee_id(employee_id):
        return Employee.query.filter_by(employee_id=employee_id).first()

    @staticmethod
    def get_all_employees():
        return Employee.query.all()


    @staticmethod
    def delete_employee(employee_id):
        employee=Employee.query.filter_by(employee_id=employee_id).first()
        db.session.delete(employee)
        db.session.commit()
        return employee
    


