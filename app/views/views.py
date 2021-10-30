from flask import render_template, request, flash, jsonify
from flask.helpers import url_for
from werkzeug.utils import redirect
from datetime import datetime
from app.models import models
from app.controllers import LoginController, MedicoController
from app.esquemas import Schemas
from app import db
from app import session
import app

def loginView():
    return render_template('login.html')

def indexView():
    if request.method == "POST":
        userName = request.form["userName"]
        userPassword = request.form["userPassword"]

        res = LoginController.iniciarSesion(userName,userPassword)

        if(res!=None):
            return redirect(url_for('dashboard'))
        else:
            return redirect(url_for('index'))

def signoutView():
    res = LoginController.cerrarSesion()
    if(res):
        flash('Sesion Cerada correctamente', 'bg-success')
        return redirect(url_for('index'))
    else:
        flash('No hay ninguna sesion iniciada','bg-danger')
        return redirect(url_for('index'))

#Vistas de paciente-----------------------------------------
def formPaciente():
    return render_template('pacientes/form_paciente.html')

def createPaciente():
    if request.method == "POST":
        documento = request.form["inputDocumento"]
        nombres = request.form["inputNombres"]
        apellidos = request.form["inputApellidos"]
        correo = request.form["inputCorreo"]
        genero = request.form["selectGenero"]
        fecha_na = request.form["inputFecha"]
        estatura = request.form["inputEstatura"]
        tipo_sangre = request.form["selectSangre"]
        alergias = request.form["inputAlergias"]
        usuario = request.form["inputUsuario"]
        contrasena = request.form["inputContrasena"]

        new_usuario = models.Usuario(usuario,contrasena,3)
        db.session.add(new_usuario)
        db.session.commit()
        usuario_id = new_usuario.id

        new_paciente = models.Paciente(documento,nombres,apellidos,correo,genero,fecha_na,estatura,tipo_sangre,alergias,usuario_id)
        db.session.add(new_paciente)
        db.session.commit()

        print("Se ha registrado un paciente con exito")
        return render_template('login.html')

def dashboardPacienteView():
    _documento_id = session['documento_id']
    _citas = db.session.execute(f"""SELECT cita.id, cita.fecha, cita.medico_id, concat_ws(' ', medico.nombres, medico.apellidos) as Medico, cita.atencion, cita.comentario, cita.estado, cita.paciente_id FROM cita JOIN medico ON cita.medico_id = medico.documento_id WHERE cita.estado = 'ACEPTADA' AND cita.paciente_id={_documento_id}""")
    return render_template('pacientes/dashboard_paciente.html', _citas=_citas)
#-----------------------------------------------------------

#Vistas de medico-------------------------------------------
def formMedico():
    pass

def createMedico():
    pass

def dashboardMedicoView():
    _documento_id = session['documento_id']
    _fecha_hoy = datetime.now().strftime("%Y-%m-%d")
    _citas = db.session.execute(f"""SELECT cita.id, cita.fecha, cita.paciente_id, concat_ws(' ', paciente.nombres, paciente.apellidos) as paciente, cita.atencion, cita.comentario, cita.estado, cita.medico_id FROM cita JOIN paciente ON cita.paciente_id = paciente.documento_id WHERE cita.fecha = '{_fecha_hoy}' AND cita.medico_id={_documento_id} AND cita.estado = 'ACEPTADA'""")
    return render_template('medicos/dashboard_medico.html', _citas=_citas)



#Vistas del administrador-----------------------------------
def dashboardAdminView():
    return "Vista del administrador xd"

#Vistas de Citas--------------------------------------------
def formCita():
    _allMedicos = MedicoController.getMedicos()
    _medicos = Schemas.medicos_schema.dump(_allMedicos)
    print(_medicos)
    return render_template('citas/form_cita.html', _medicos=_medicos)

def solicitarCita():
    if request.method == "POST":
        medico_id = request.form["listMedicos"]
        usuario_id = app.session['id']
        print(f'id de usuario: {usuario_id}')
        paciente = models.Paciente.query.filter(models.Paciente.usuario_id==usuario_id).first()
        _paciente = Schemas.paciente_schema.dump(paciente)
        print(_paciente)
        pacienteid = _paciente['documento_id']
        estado = "SIN ACEPTAR"

        new_cita = models.Cita(medico_id,pacienteid,estado)
        db.session.add(new_cita)
        db.session.commit()

        app.flash('Solicitud de cita realzada con exito','bg-success')
        return redirect(url_for('form_cita'))

def citasView():
    if session['id_rol']==1:
        _result = db.session.execute("""SELECT cita.id, cita.paciente_id, cita.fecha, cita.estado, cita.comentario, cita.atencion, concat_ws(' ', medico.nombres, medico.apellidos) as Medico FROM cita JOIN medico ON cita.medico_id = medico.documento_id WHERE cita.estado = 'SIN ACEPTAR'""")
        return render_template('citas/cita_admins.html', _result=_result)
    elif session['id_rol']==2:
        _documento_id = session['documento_id']
        _citas = db.session.execute(f"""SELECT cita.id, cita.fecha, cita.paciente_id, concat_ws(' ', paciente.nombres, paciente.apellidos) as Paciente, cita.atencion, cita.comentario, cita.estado, cita.medico_id FROM cita JOIN paciente ON cita.paciente_id = paciente.documento_id WHERE cita.medico_id={_documento_id}""")
        return render_template('citas/cita_medicos.html')
    elif session['id_rol']==3:
        _documento_id = session['documento_id']
        _citas = db.session.execute(f"""SELECT cita.id, cita.fecha, cita.medico_id, concat_ws(' ', medico.nombres, medico.apellidos) as Medico, cita.atencion, cita.comentario, cita.estado, cita.paciente_id FROM cita JOIN medico ON cita.medico_id = medico.documento_id WHERE cita.paciente_id={_documento_id}""")
        return render_template('citas/cita_pacientes.html', _citas=_citas)
    else:
        return "Inicio se sesión desconocido. Por favor Inicie sesión a través del formulario"

def formCitaUpdate(id):
    _cita = db.session.execute(f"""SELECT cita.id, cita.fecha, cita.paciente_id, concat_ws(' ', paciente.nombres, paciente.apellidos) as Paciente, cita.atencion, cita.comentario, cita.estado, cita.medico_id FROM cita JOIN paciente ON cita.paciente_id = paciente.documento_id WHERE cita.id={id}""")    
    return render_template("citas/edit_cita.html", _cita=_cita)

def updateCita():
    idCita = int(request.form["id_cita"])
    fecha = request.form['inputFecha']
    comentario = request.form['inputComentario']
    estado = request.form['listEstado']

    cita = models.Cita.query.get(idCita)
    
    if cita != None:
        cita.fecha = fecha
        cita.comentario = comentario
        cita.estado = estado
        db.session.commit()
        app.flash('Detalles de cita actualizados con exito!','bg-danger')
        return redirect(url_for('form_cita'))
    else:
        app.flash('No se pudo encontrar la cita a actualizar','bg-danger')
        return redirect(url_for('form_cita'))
    

def cancelarCita():
    id = request.form['idCita']
   
    cita = models.Cita.query.get(id)
    id_resp = cita.id
    est = cita.estado
    print(f"id cita: {id_resp}")
    print(f"estado cita: {est}")

    if cita != None:
        try:
            cita.estado = "CANCELADA"
            db.session.commit()
            return jsonify({'success':'Cita cancelada con exito'})
        except:
            return jsonify({'error':'Error: No se pudo cancelar la cita'})
    else:
        return jsonify({'others_error':'No se encontró la cita destino.'})
#-----------------------------------------------------------


#Pruebas----------------------------------------------------
def testView():
    return 'it works!'
#-----------------------------------------------------------