"""
Module defines employee web application view.
"""
from flask import render_template, redirect, url_for, flash
from wtforms.fields import form

from department_app.forms.forms import EmployeeForm, SearchForm
from department_app.service.department import DepartmentService
from department_app.service.position import PositionService
from department_app.views import m_bp
from department_app.service.employee import EmployeeService
from department_app import app


@m_bp.route('/employees/', methods=['GET'])
def get_employees():
    """
    Returns rendered template to show all employees.
    """
    employees = EmployeeService.get_all_emp()
    return render_template('employees.html', title='Employees', employees=employees)


@m_bp.route('/employee/edit/<int:employee_id>', methods=['GET', 'POST'])
def edit_employee(employee_id):
    """
    Returns rendered template to edit employee.
    """
    employee = EmployeeService.get_emp_by_id(employee_id)
    EmployeeForm.get_departments_list()
    EmployeeForm.get_positions_list()
    form = EmployeeForm(obj=employee)

    if form.validate_on_submit():
        if not EmployeeService.get_emp_by_email(form.email.data) or form.email.data == employee.email:
            form.populate_obj(employee)
            employee.department = DepartmentService.get_dep_by_name(
                form.department_name.data)
            employee.position = PositionService.get_pos_by_name(
                form.position_name.data)
            EmployeeService.save_changes()
            return redirect(url_for('m_bp.get_employees'))
        else:
            flash('Employee with this email {} already exists. Enter another email.'.format(
                form.email.data))
            return redirect(url_for('m_bp.edit_employee', employee_id=employee.id))

    form.first_name.data = employee.first_name
    form.last_name.data = employee.last_name
    form.email.data = employee.email
    form.hire_date.data = employee.hire_date
    form.department_name.data = employee.department.name
    form.position_name.data = employee.position.name
    form.salary.data = employee.salary

    return render_template('edit_employee.html', form=form, employee=employee)


@m_bp.route('/add_employee', methods=['GET', 'POST'])
def add_employee():
    """
    Returns rendered template to add employee.
    """
    EmployeeForm.get_departments_list()
    EmployeeForm.get_positions_list()
    form = EmployeeForm()

    if form.validate_on_submit():
        if not EmployeeService.get_emp_by_email(form.email.data):
            EmployeeService.add_emp(form.first_name.data, form.last_name.data, form.hire_date.data,
                                    form.salary.data, form.email.data, form.department_name.data, form.position_name.data)
            return redirect(url_for('m_bp.get_employees'))
        else:
            flash('Employee with this email {} already exists. Enter another email.'.format(
                form.email.data))
            return redirect(url_for('m_bp.add_employee'))

    return render_template('add_employee.html', form=form)


@m_bp.route('/employees/delete/<int:employee_id>', methods=['GET'])
def delete_employee(employee_id):
    """
    Returns rendered template to delete employee.
    """
    EmployeeService.delete(employee_id)
    return redirect(url_for('m_bp.get_employees'))


@m_bp.route('/search/', methods=['GET', 'POST'])
def search():
    """
    Returns rendered template to search employee by hire date.
    """
    form = SearchForm()
    if form.validate_on_submit():
        date_from = form.date_from.data
        date_to = form.date_to.data
        employees = EmployeeService.get_emp_by_hire_date(date_from, date_to)
        return render_template('employees.html', employees=employees)
    return render_template('search.html', form=form)
