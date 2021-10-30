from app import ma

class MedicoSchema(ma.Schema):
    class Meta:
        fields = ('documento_id', 'nombres', 'apellidos', 'genero', 'correo', 'fecha_nac', 'especialidad','sueldo','atencion_max','usuario_id')

class PacienteSchema(ma.Schema):
    class Meta:
        fields = ('documento_id', 'nombres', 'apellidos', 'genero', 'correo', 'fecha_nac', 'estatura', 'alergias','tipo_sangre','usuario_id')

class AdministradorSchema(ma.Schema):
    class Meta:
        fields = ('documento_id', 'nombres', 'apellidos', 'genero', 'correo', 'fecha_nac', 'usuario_id')

class UsuarioSchema(ma.Schema):
    class Meta:
        fields = ('id', 'usuario', 'contrasena', 'rol_id')

class RolSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'descripccion')

class CitaSchema(ma.Schema):
    class Meta:
        fields = ('id', 'medico_id', 'paciente_d', 'fecha', 'estado', 'comentario', 'atencion')


#Medico:
medico_schema = MedicoSchema()
medicos_schema = MedicoSchema(many=True)

#Paciente:
paciente_schema = PacienteSchema()
pacientes_schema = PacienteSchema(many=True)

#Administrador:
admin_schema = AdministradorSchema()
admins_schema = AdministradorSchema(many=True)

#Usuario:
usuario_schema = UsuarioSchema()
usuarios_schema = UsuarioSchema(many=True)

#Rol
rol_schema = RolSchema()
roles_schema = RolSchema(many=True)

#cita
cita_schema = RolSchema()
citas_schema = RolSchema(many=True)