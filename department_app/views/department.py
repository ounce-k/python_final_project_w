"""[summary]"""


# import json
from flask import render_template, redirect, url_for, flash
# from department_app.models import department

from department_app.forms.forms import DepartmentForm
from department_app.views import m_bp
from department_app.service.department import DepartmentService
from department_app.shemas.department import DepartmentSchema

department_schema = DepartmentSchema(many=True)


@m_bp.route('/', methods=['GET'])
@m_bp.route('/departments/', methods=['GET'])
def get_departments():
    """[summary]
    """
    department_models = DepartmentService.get_all_dep()
    departments = department_schema.dump(department_models)
    return render_template('departments.html', title='Departments', departments=departments)

@m_bp.route('/add_department', methods=['GET','POST'])
def add_department():
    form = DepartmentForm()
    if form.validate_on_submit():
        if not DepartmentService.get_dep_by_name(form.name.data):
            DepartmentService.add_dep(form.name.data)
            return redirect(url_for('m_bp.get_departments'))
        else:
            flash('Department {} already exists. Enter another name.'.format(form.name.data))
            return redirect(url_for('m_bp.add_department'))
    return render_template('add_department.html', form=form)

@m_bp.route('/departments/delete/<int:department_id>', methods=['GET'])
def delete_department(department_id):
    DepartmentService.delete(department_id)
    return redirect(url_for('m_bp.get_departments'))

@m_bp.route('/departments/<int:department_id>', methods=['GET'])
def get_department(department_id):
    department = DepartmentService.get_dep_by_id(department_id)
    return render_template('department.html',department=department)

@m_bp.route('/departments/edit/<int:department_id>', methods=['GET', 'POST'])
def edit_department(department_id):
    department = DepartmentService.get_dep_by_id(department_id)
    form = DepartmentForm(obj=department)
    if form.validate_on_submit():
        if not DepartmentService.get_dep_by_name(form.name.data):
            form.populate_obj(department)
            DepartmentService.save_changes()
            return redirect(url_for('m_bp.get_departments'))
        else:
            flash('Department {} already exists. Enter another name.'.format(form.name.data))
            return redirect(url_for('m_bp.edit_department', department_id=department.id))
    form.name.data = department.name
    return render_template('edit_department.html', form=form, department=department)