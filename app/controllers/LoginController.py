from app.models import models
from app.esquemas import Schemas
import app

def iniciarSesion(_username,_password):
                                        
    _usuario = models.Usuario.query.filter(models.Usuario.usuario == _username).first()
    print("------------------")
    print(_usuario)
    
    if(_usuario != None):
        if(_usuario.contrasena == _password):
            #Registrando datos de sesión.
            if _usuario.rol_id==1: 
                rest = models.Administrador.query.filter(models.Administrador.usuario_id==_usuario.id).first()
                restfull = Schemas.admin_schema.dump(rest)
            elif _usuario.rol_id==2: 
                rest = models.Medico.query.filter(models.Medico.usuario_id==_usuario.id).first()
                restfull = Schemas.medico_schema.dump(rest)
            else: 
                rest = models.Paciente.query.filter(models.Paciente.usuario_id==_usuario.id).first()
                restfull = Schemas.paciente_schema.dump(rest)

            app.session['id'] = _usuario.id
            app.session['documento_id'] = rest.documento_id
            app.session['nombres'] = rest.nombres
            app.session['username'] = _usuario.usuario
            app.session['id_rol'] = _usuario.rol_id

            #print("VARIABLES DE SESION:")
            #print(f'id: {_usuario.id}')
            #print(f'documento_id: {rest.documento_id}')
            #print(f'username: {_usuario.usuario}')
            #print(f'rol: {_usuario.rol_id}')
            return "ok"
        else:
            app.flash('Contraseña incorrecta', 'bg-danger')
            print('Contraseña incorrecta')
            return None
    else:
        app.flash('¡El usuario no existe!', 'bg-danger')
        print('El usuario no existe')
        return None


def cerrarSesion():
    if(app.session):
        app.session.clear()
        return True
    else:
        return False


