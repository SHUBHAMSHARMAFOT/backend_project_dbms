class EmployeeView:
    @staticmethod
    def render_employee(employee):
        return {
            "employee_id": employee.employee_id,
            "name": employee.name,
            "contact_info": employee.contact_info,
            "role": employee.role,
            "department_id": employee.department_id,
            "hired_at": employee.hired_at,
            "updated_at": employee.updated_at,
        }




    @staticmethod
    def render_employees(employees):
        return [ EmployeeView.render_employee(employee) for employee in employees]

    @staticmethod
    def render_error(message):
        return {"error": message}

    @staticmethod
    def render_success(message, employee_id=None):
        response = {"message": message}
        if employee_id:
            response["user_id"] = employee_id
        return response
    
