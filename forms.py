from wtforms import Form, validators
from flask_wtf import FlaskForm

from wtforms import StringField, IntegerField, EmailField

class UserForm2(Form):
    id=IntegerField('id', [validators.number_range(min=1, max=20, message='valor no valido')])
    nombre=StringField('nombre', [validators.DataRequired(message='El nombre es requerido'),
                                  validators.length(min=4, max=20, message='requiere min=4 y max=20')])
    apellidos=StringField('apellidos', [validators.DataRequired(message='Los apellidos son requeridos')])
    email=EmailField('correo', [validators.DataRequired(message='El correo es requerido'),
                                validators.Email(message='Ingrese un correo valido')])
    telefono=StringField('telefono', [validators.DataRequired(message="El telefono es requerido"),
                                      validators.length(max=10, message='requiere max=10')])