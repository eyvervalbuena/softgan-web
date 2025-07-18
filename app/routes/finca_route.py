from flask import Blueprint, render_template, request, redirect, url_for, flash
from app.dao.finca_dao import FincaDao
from app.modelo.finca import Finca

bp_finca = Blueprint('finca', __name__, url_prefix='/finca')
dao = FincaDao()

@bp_finca.route('/listar')
def listar():
    fincas = dao.list_all()
    return render_template('finca_list.html', fincas=fincas)

@bp_finca.route('/nuevo', methods=['GET'])
def nuevo():
    return render_template('finca_form.html', finca=None)

@bp_finca.route('/crear', methods=['POST'])
def crear():
    d = request.form
    finca = Finca(
        nombre         = d['nombre'],
        propietario    = d['propietario'],
        direccion      = d.get('direccion'),
        hectareas      = float(d['hectareas']),
        num_potreros   = int(d['num_potreros']),
        marca1         = d.get('marca1') or None,
        marca2         = d.get('marca2') or None,
        marca3         = d.get('marca3') or None,
        nit            = d.get('nit'),
        email          = d.get('email'),
        edades_hembras = d.get('edades_hembras'),
        edades_machos  = d.get('edades_machos'),
    )
    dao.insert(finca)
    flash("Finca creada correctamente.", "success")
    return redirect(url_for('finca.listar'))

@bp_finca.route('/editar/<int:id>', methods=['GET'])
def editar(id):
    finca = dao.get_by_id(id)
    if not finca:
        flash("Finca no encontrada.", "danger")
        return redirect(url_for('finca.listar'))
    return render_template('finca_form.html', finca=finca)

@bp_finca.route('/editar/<int:id>', methods=['POST'])
def actualizar(id):
    d = request.form
    finca = Finca(
        id_finca       = id,
        nombre         = d['nombre'],
        propietario    = d['propietario'],
        direccion      = d.get('direccion'),
        hectareas      = float(d['hectareas']),
        num_potreros   = int(d['num_potreros']),
        marca1         = d.get('marca1') or None,
        marca2         = d.get('marca2') or None,
        marca3         = d.get('marca3') or None,
        nit            = d.get('nit'),
        email          = d.get('email'),
        edades_hembras = d.get('edades_hembras'),
        edades_machos  = d.get('edades_machos'),
    )
    dao.update(finca)
    flash("Finca actualizada correctamente.", "success")
    return redirect(url_for('finca.listar'))

@bp_finca.route('/eliminar/<int:id>', methods=['POST'])
def eliminar(id):
    if dao.delete(id):
        flash("Finca eliminada correctamente.", "success")
    else:
        flash("No se pudo eliminar la finca.", "danger")
    return redirect(url_for('finca.listar'))
