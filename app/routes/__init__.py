from app.views import views
from app import session, app

#Login-----------------------------------
@app.route("/", methods=["GET"])
def index():
    return views.loginView()

@app.route('/login', methods=['POST'])
def login():
    return views.indexView()

@app.route('/signout', methods=['GET'])
def signout():
    return views.signoutView()
#--------------------------------------

#Dashboard-----------------------------
@app.route('/dasboard', methods=['GET'])
def dashboard():
    if(session['id_rol']==3):
        return views.dashboardPacienteView()
    elif(session['id_rol']==2):
        return views.dashboardMedicoView()
    elif(session['id_rol']==1):
        return views.dashboardAdminView()
    else:
        return "No se ha podido validar la sesión del usuario. Por favor inicie sesion."
    
#Citas----------------------------------
@app.route('/form_cita', methods=['GET'])
def form_cita():
    return views.formCita()

@app.route('/citas', methods=['GET'])
def citas():
    return views.citasView()

@app.route('/solicitar_cita', methods=['POST'])
def solicitar_cita():
    return views.solicitarCita()

@app.route('/form_editCita/<int:id>', methods=['GET'])
def form_editCita(id):
    return views.formCitaUpdate(id)

@app.route('/update_cita', methods=['POST'])
def update_cita():
    return views.updateCita()

@app.route('/cancelar_cita', methods=['POST'])
def cancelar_cita():
    return views.cancelarCita()
#---------------------------------------


@app.route('/form_paciente', methods=['GET'])
def form_paciente():
    return views.formPaciente()

@app.route('/create_paciente', methods=['POST'])
def create_paciente():
    return views.createPaciente()


#Pruebas------------------------------------------
@app.route('/test', methods=['GET'])
def test():
    return views.testView()
#-------------------------------------------------