from app import db
#---------------Clases modelo SQLAlchemy--------------
class Medico(db.Model):
    __tablename__='medico'
    documento_id = db.Column(db.BIGINT, primary_key=True, nullable=False)
    nombres = db.Column(db.String(255), nullable=False)
    apellidos = db.Column(db.String(255), nullable=False)
    genero = db.Column(db.String(50), nullable=False)
    correo = db.Column(db.String(50), nullable=False)
    fecha_nac = db.Column(db.Date, nullable=False)
    especialidad = db.Column(db.String(255), nullable=False)
    sueldo = db.Column(db.Float, nullable=True)
    atencion_max = db.Column(db.Integer, nullable=True)

    #CLAVE FORANEA DE USUARIO---------------------------------------------------
    usuario_id = db.Column(db.BIGINT, db.ForeignKey('usuario.id'), nullable=False)
    #-----------------------------------------------------------------------

    #Relacion con Cita
    citas = db.relationship("Cita")

    def __init__(self,documento_id,nombres,apellidos,genero,correo,fecha_nac,especialidad,sueldo,atencion_max,usuario_id):
        self.documento_id = documento_id
        self.nombres = nombres
        self.apellidos = apellidos
        self.genero = genero
        self.correo = correo
        self.fecha_nac = fecha_nac
        self.especialidad = especialidad
        self.sueldo = sueldo
        self.atencion_max = atencion_max
        self.usuario_id = usuario_id
    
    def __repr__(self):
        return f'{self.documento_id}'

class Paciente(db.Model):
    __tablename__='paciente'
    documento_id = db.Column(db.BIGINT, primary_key=True, nullable=False)
    nombres = db.Column(db.String(255), nullable=False)
    apellidos = db.Column(db.String(255), nullable=False)
    genero = db.Column(db.String(50), nullable=False)
    correo = db.Column(db.String(50), nullable=False)
    fecha_nac = db.Column(db.Date, nullable=False)
    estatura = db.Column(db.Float, nullable=True)
    alergias = db.Column(db.String(255), nullable=False)
    tipo_sangre = db.Column(db.String(255), nullable=False)
    
    #CLAVE FORANEA DE USUARIO---------------------------------------------------
    usuario_id = db.Column(db.BIGINT, db.ForeignKey('usuario.id'), nullable=False)
    #-----------------------------------------------------------------------

    #Relacion con Cita
    citas = db.relationship("Cita")

    def __init__(self,documento_id,nombres,apellidos,genero,correo,fecha_nac,estatura,alergias,tipo_sangre,usuario_id):
        self.documento_id = documento_id
        self.nombres = nombres
        self.apellidos = apellidos
        self.genero = genero
        self.correo = correo
        self.fecha_nac = fecha_nac
        self.estatura = estatura
        self.alergias = alergias
        self.tipo_sangre = tipo_sangre
        self.usuario_id = usuario_id
    
    def __repr__(self):
        return f'{self.documento_id}'

class Administrador(db.Model):
    __tablename__='administrador'
    documento_id = db.Column(db.BIGINT, primary_key=True, nullable=False)
    nombres = db.Column(db.String(255), nullable=False)
    apellidos = db.Column(db.String(255), nullable=False)
    genero = db.Column(db.String(50), nullable=False)
    correo = db.Column(db.String(50), nullable=False)
    fecha_nac = db.Column(db.Date, nullable=False)

    #CLAVE FORANEA DE USUARIO---------------------------------------------------
    usuario_id = db.Column(db.BIGINT, db.ForeignKey('usuario.id'), nullable=False)
    #-----------------------------------------------------------------------

    def __init__(self,documento_id,nombres,apellidos,genero,correo,fecha_nac):
        self.documento_id = documento_id
        self.nombres = nombres
        self.apellidos = apellidos
        self.genero = genero
        self.correo = correo
        self.fecha_nac = fecha_nac
    
    def __repr__(self):
        return f'{self.documento_id}'

class Rol(db.Model):
    __tablename__ = 'rol'
    id = db.Column(db.BIGINT, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    descripccion = db.Column(db.Text, nullable=False)

    #RELACION CON USUARIOS
    users = db.relationship("Usuario")

    def __init__(self, name, description):
        self.name = name
        self.description = description


    def __repr__(self):
        return f'{self.id}'

class Usuario(db.Model):
    __tablename__ = 'usuario'
    id = db.Column(db.BIGINT, primary_key=True)
    usuario = db.Column(db.String(80), unique=True, nullable=False)
    contrasena = db.Column(db.String(255), nullable=False)
    db.UniqueConstraint('usuario', name='uix_1')

    #CLAVE FORANEA DE ROL---------------------------------------------------
    rol_id = db.Column(db.BIGINT, db.ForeignKey('rol.id'), nullable=False)
    #-----------------------------------------------------------------------

    #Relacion con Medico--------------------------------------------------
    medicos = db.relationship("Medico")
    #---------------------------------------------------------------------


    def __init__(self, usuario, contrasena, rol_id):
        self.usuario = usuario
        self.contrasena = contrasena
        self.rol_id = rol_id

    def __repr__(self):
        return f'{self.usuario}'

class Cita(db.Model):
    __tablename__='cita'
    id = db.Column(db.BIGINT, primary_key=True, nullable=False)

    #CLAVE FORANEA DE MEDICO---------------------------------------------------
    medico_id = db.Column(db.BIGINT, db.ForeignKey('medico.documento_id'), nullable=False)
    #-----------------------------------------------------------------------

    #CLAVE FORANEA DE PACIENTE---------------------------------------------------
    paciente_id = db.Column(db.BIGINT, db.ForeignKey('paciente.documento_id'), nullable=False)
    #-----------------------------------------------------------------------

    fecha = db.Column(db.Date, nullable=True)
    estado = db.Column(db.String(50), nullable=False)
    comentario = db.Column(db.String(50), nullable=True)
    atencion = db.Column(db.String(50), nullable=True)

    def __init__(self,medico_id,paciente_id,estado):
        self.medico_id = medico_id
        self.paciente_id = paciente_id
        self.estado = estado
    
    def __repr__(self):
        return f'{self.id}'