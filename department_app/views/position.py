
from flask import render_template, redirect, url_for, flash

from department_app.forms.forms import PositionForm
from department_app.views import m_bp
from department_app.service.position import PositionService
from department_app.shemas.position import PositionSchema

position_schema = PositionSchema(many=True)


@m_bp.route('/positions/', methods=['GET'])
def get_positions():
    """[summary]
    """
    positions_models = PositionService.get_all_pos()
    positions = position_schema.dump(positions_models)
    return render_template('positions.html', title='Positions', positions=positions)

@m_bp.route('/positions/<int:position_id>', methods=['GET'])
def get_position(position_id):
    position = PositionService.get_pos_by_id(position_id)
    return render_template('position.html',position=position)

@m_bp.route('/add_position', methods=['GET','POST'])
def add_position():
    form = PositionForm()
    if form.validate_on_submit():
        if not PositionService.get_pos_by_name(form.name.data):
            PositionService.add_pos(form.name.data)
            return redirect(url_for('m_bp.get_positions'))
        else:
            flash('Position {} already exists. Enter another name.'.format(form.name.data))
            return redirect(url_for('m_bp.add_position'))
    return render_template('add_position.html', form=form)

@m_bp.route('/positions/delete/<int:position_id>', methods=['GET'])
def delete_position(position_id):
    PositionService.delete(position_id)
    return redirect(url_for('m_bp.get_positions'))


@m_bp.route('/positions/edit/<int:position_id>', methods=['GET', 'POST'])
def edit_position(position_id):
    position = PositionService.get_pos_by_id(position_id)
    form = PositionForm(obj=position)
    if form.validate_on_submit():
        if not PositionService.get_pos_by_name(form.name.data):
            form.populate_obj(position)
            PositionService.save_changes()
            return redirect(url_for('m_bp.get_positions'))
        else:
            flash('Position {} already exists. Enter another name.'.format(form.name.data))
            return redirect(url_for('m_bp.edit_position', position_id=position.id))
    form.name.data = position
    return render_template('edit_position.html', form=form, position=position)