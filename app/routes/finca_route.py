# app/routes/finca_route.py

from flask import Blueprint, render_template, request, redirect, url_for, flash
from app.dao.finca_dao import FincaDao
from app.modelo.finca import Finca

# 1. Definimos el Blueprint para todas las rutas /finca
bp_finca = Blueprint('finca', __name__, url_prefix='/finca')

# 2. Instanciamos el DAO
dao = FincaDao()


# 3. LISTAR todas las fincas
@bp_finca.route('/listar')
def listar():
    fincas = dao.list_all()
    return render_template('finca_list.html', fincas=fincas)


# 4. FORMULARIO EN BLANCO para crear una finca nueva
@bp_finca.route('/nuevo', methods=['GET'])
def nuevo():
    return render_template('finca_form.html', finca=None)


# 5. PROCESAR CREACIÓN
@bp_finca.route('/crear', methods=['POST'])
def crear():
    d = request.form
    finca = Finca(
        nombre         = d['nombre'],
        propietario    = d['propietario'],
        direccion      = d['direccion'],
        hectareas      = float(d['hectareas']),
        num_potreros   = int(d['num_potreros']),
        marca1         = d.get('marca1') or None,
        marca2         = d.get('marca2') or None,
        marca3         = d.get('marca3') or None,
        nit            = d.get('nit') or None,
        email          = d.get('email') or None,
        edades_hembras = d.get('edades_hembras') or None,
        edades_machos  = d.get('edades_machos') or None
    )
    dao.insert(finca)
    flash(" Finca creada correctamente.", "success")
    return redirect(url_for('finca.listar'))


# 6. FORMULARIO PARA EDITAR (carga los datos existentes)
@bp_finca.route('/editar/<int:id>', methods=['GET'])
def editar(id):
    finca = dao.find_by_id(id)
    if not finca:
        flash("❌ Finca no encontrada.", "danger")
        return redirect(url_for('finca.listar'))
    return render_template('finca_form.html', finca=finca)


# 7. PROCESAR ACTUALIZACIÓN
@bp_finca.route('/editar/<int:id>', methods=['POST'])
def actualizar(id):
    d = request.form
    dij = Finca(
        id_finca       = id,
        nombre         = d['nombre'],
        propietario    = d['propietario'],
        direccion      = d['direccion'],
        hectareas      = float(d['hectareas']),
        num_potreros   = int(d['num_potreros']),
        marca1         = d.get('marca1') or None,
        marca2         = d.get('marca2') or None,
        marca3         = d.get('marca3') or None,
        nit            = d.get('nit') or None,
        email          = d.get('email') or None,
        edades_hembras = d.get('edades_hembras') or None,
        edades_machos  = d.get('edades_machos') or None
    )
    dao.update(fij)
    flash(" Finca actualizada correctamente.", "success")
    return redirect(url_for('finca.listar'))


# 8. ELIMINAR una finca
@bp_finca.route('/eliminar/<int:id>', methods=['POST'])
def eliminar(id):
    success = dao.delete(id)
    if success:
        flash(" Finca eliminada correctamente.", "success")
    else:
        flash(" No se pudo eliminar la finca.", "danger")
    return redirect(url_for('finca.listar'))
