from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DateField, IntegerField, EmailField

from wtforms.fields.choices import SelectField
from wtforms.validators import DataRequired, Length

from department_app.service.department import DepartmentService
from department_app.service.position import PositionService
from department_app.shemas.department import DepartmentSchema
from department_app.shemas.position import PositionSchema

department_schema = DepartmentSchema(many=True)
position_schema = PositionSchema(many=True)


class DepartmentForm(FlaskForm):
    name = StringField('New department name', validators=[
                       DataRequired(), Length(min=3, max=64)])
    submit = SubmitField('Submit')


class PositionForm(FlaskForm):
    name = StringField('New position name', validators=[
                       DataRequired(), Length(min=3, max=64)])
    submit = SubmitField('Submit')


class SearchForm(FlaskForm):
    date_from = DateField(
        'Hire date from', format='%Y-%m-%d', validators=[DataRequired()])
    date_to = DateField('Hire date to', format='%Y-%m-%d',
                        validators=[DataRequired()])
    submit = SubmitField('Submit')


class EmployeeForm(FlaskForm):
    first_name = StringField('New employee first name', validators=[
                             DataRequired(), Length(min=2, max=64)])
    last_name = StringField('New employee last name', validators=[
                            DataRequired(), Length(min=2, max=64)])
    email = EmailField('New employee email', validators=[DataRequired()])
    hire_date = DateField('Hire date', format='%Y-%m-%d',
                          validators=[DataRequired()])
    department_name = SelectField(choices=[''])
    position_name = SelectField(choices=[''])
    salary = IntegerField('Salary', validators=[DataRequired()])
    submit = SubmitField('Submit')

    @classmethod
    def get_departments_list(cls):
        department_models = DepartmentService.get_all_dep()
        departments = department_schema.dump(department_models)
        cls.department_name = SelectField(
            choices=[department['name'] for department in departments])

    @classmethod
    def get_positions_list(cls):
        position_models = PositionService.get_all_pos()
        positions = position_schema.dump(position_models)
        cls.position_name = SelectField(
            choices=[position['name'] for position in positions])
