from . import alumnos
from flask import Flask, render_template, request, redirect, url_for
import forms
from flask_migrate import Migrate
from models import db
from models import Alumnos

@alumnos.route('/alumnos', methods=['GET', 'POST'])
def alumno():
    create_form=forms.UserFormAlumno(request.form)
    alumnos = Alumnos.query.all()
    return render_template('alumnos/index.html', form=create_form, alumnos=alumnos)

@alumnos.route("/regAlumnos", methods=['GET', 'POST'])
def regAlumnos():
	create_form = forms.UserFormAlumno(request.form)
	if request.method=='POST':
		alumno=Alumnos(nombre=create_form.nombre.data,
						apellidos=create_form.apellidos.data,
						email=create_form.email.data,
						telefono=create_form.telefono.data
						)
		db.session.add(alumno)
		db.session.commit()
		return redirect(url_for('alumnos.alumno'))	
		
	return render_template("alumnos/alumnos.html", form=create_form)

@alumnos.route("/detAlumno",  methods=['GET', 'POST'])
def detAlumno():
	create_form=forms.UserFormAlumno(request.form)
	if request.method=='GET':
		id=request.args.get('id')
		# select * from alumnos where id == id
		alum1 = db.session.query(Alumnos).filter(Alumnos.id==id).first()
		id=request.args.get('id')
		nombre=alum1.nombre
		apellidos=alum1.apellidos
		email=alum1.email
		telefono=alum1.telefono

	return render_template("alumnos/detalles.html", id=id, nombre=nombre, apellidos=apellidos, email=email, telefono=telefono)

@alumnos.route("/modAlumno", methods=['GET', 'POST'])
def modAlumno():
	create_form=forms.UserFormAlumno(request.form)
	if request.method=='GET':
		id=request.args.get('id')

		alum1=db.session.query(Alumnos).filter(Alumnos.id==id).first()
		create_form.id.data=request.args.get('id')
		create_form.nombre.data=str.rstrip(alum1.nombre)
		create_form.apellidos.data=alum1.apellidos
		create_form.email.data=alum1.email
		create_form.telefono.data=alum1.telefono
	if request.method=='POST':
		id=create_form.id.data
		alum1=db.session.query(Alumnos).filter(Alumnos.id==id).first()
		alum1.id=id
		alum1.nombre=str.rstrip(create_form.nombre.data)
		alum1.apellidos=create_form.apellidos.data
		alum1.email=create_form.email.data
		alum1.telefono=create_form.telefono.data
		db.session.add(alum1)
		db.session.commit()
		return redirect(url_for('alumnos.alumno'))
	return render_template('alumnos/modificar.html', form=create_form)

@alumnos.route("/eliAlumno", methods=['GET', 'POST'])
def eliAlumno():
	create_form = forms.UserFormAlumno(request.form)
	if request.method == 'GET':
		id = request.args.get('id')
		alum1 = db.session.query(Alumnos).filter(Alumnos.id == id).first()
		if alum1:
			create_form.id.data = alum1.id
			create_form.nombre.data = alum1.nombre
			create_form.apellidos.data = alum1.apellidos
			create_form.email.data = alum1.email
			create_form.telefono.data = alum1.telefono
			return render_template("alumnos/eliminar.html", form=create_form)
		
	if request.method == 'POST':
			id = create_form.id.data
			alum = db.session.query(Alumnos).filter(Alumnos.id == id).first()
			if alum:
				db.session.delete(alum)
				db.session.commit()
			return redirect(url_for('alumnos.alumno'))
		
	return render_template("alumnos/eliminar.html", form=create_form)

@alumnos.route('/perfil/<nombre>')
def perfil(nombre):
	return f'Perfil de {nombre}'