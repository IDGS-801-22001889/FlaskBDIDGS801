from wtforms import Form, validators
from flask_wtf import FlaskForm

from wtforms import StringField, IntegerField, EmailField, TextAreaField, SelectField

class UserFormAlumno(Form):
    id=IntegerField('id', [validators.number_range(min=1, max=20, message='valor no valido')])
    nombre=StringField('nombre', [validators.DataRequired(message='El nombre es requerido'),
                                  validators.length(min=4, max=20, message='requiere min=4 y max=20')])
    apellidos=StringField('apellidos', [validators.DataRequired(message='Los apellidos son requeridos')])
    email=EmailField('correo', [validators.DataRequired(message='El correo es requerido'),
                                validators.Email(message='Ingrese un correo valido')])
    telefono=StringField('telefono', [validators.DataRequired(message="El telefono es requerido"),
                                      validators.length(max=10, message='requiere max=10')])
    
class UserFormMaestro(Form):
    matricula=IntegerField('matricula', [validators.number_range(min=1, max=20, message='valor no valido')])
    nombre=StringField('nombre', [validators.DataRequired(message='El nombre es requerido'),
                                  validators.length(min=4, max=20, message='requiere min=4 y max=50')])
    apellidos=StringField('apellidos', [validators.DataRequired(message='Los apellidos son requeridos')])
    especialidad=StringField('especialidad', [validators.DataRequired(message='La especialidad son requeridos')])
    email=EmailField('correo', [validators.DataRequired(message='El correo es requerido'),
                                validators.Email(message='Ingrese un correo valido')])
    
class UserFormCurso(Form):
    id = IntegerField('id', [validators.number_range(min=1, max=20, message='Valor no valido')])
    nombre = StringField('nombre', [validators.DataRequired(message='El nombre es requerido'),
                                    validators.length(min=4, max=100, message='requiere min=4 y max=100')])
    descripcion = TextAreaField('descripcion', [validators.DataRequired(message='La descripcion es requerida')])
    maestro_id = IntegerField('maestro_id', [validators.optional()])