from app.models import models
from app.esquemas import Schemas
import app

def getMedicos():
    medicos = models.Medico.query.all()
    return medicos