from . import maestros
from flask import Flask, render_template, request, redirect, url_for
import forms
from flask_migrate import Migrate
from models import db
from models import  Maestros

@maestros.route("/maestros", methods=['GET', 'POST'])
def maestro():
    create_form=forms.UserFormMaestro(request.form)
    maestros = Maestros.query.all()
    return render_template("maestros/listadoMaes.html", form=create_form, maestros=maestros)

@maestros.route("/regMaestro", methods=['GET', 'POST'])
def regMaestro():
	create_form = forms.UserFormMaestro(request.form)
	if request.method=='POST':
		maestro=Maestros(nombre=create_form.nombre.data,
						apellidos=create_form.apellidos.data,
						especialidad=create_form.especialidad.data,
						email=create_form.email.data
						)
		db.session.add(maestro)
		db.session.commit()
		return redirect(url_for('maestros.maestro'))	
		
	return render_template("maestros/maestros.html", form=create_form)

@maestros.route("/detMaestro",  methods=['GET', 'POST'])
def detMaestro():
	create_form=forms.UserFormMaestro(request.form)
	if request.method=='GET':
		matricula=request.args.get('matricula')
		# select * from maestros where matricula == matricula
		mae1 = db.session.query(Maestros).filter(Maestros.matricula==matricula).first()
		matricula=request.args.get('matricula')
		nombre=mae1.nombre
		apellidos=mae1.apellidos
		especialidad=mae1.especialidad
		email=mae1.email

	return render_template("maestros/detMaestros.html", matricula=matricula, nombre=nombre, apellidos=apellidos,especialidad=especialidad, email=email)

@maestros.route("/modMaestro", methods=['GET', 'POST'])
def modMaestro():
	create_form=forms.UserFormMaestro(request.form)
	if request.method=='GET':
		matricula=request.args.get('matricula')

		mae1=db.session.query(Maestros).filter(Maestros.matricula==matricula).first()
		create_form.matricula.data=request.args.get('matricula')
		create_form.nombre.data=str.rstrip(mae1.nombre)
		create_form.apellidos.data=mae1.apellidos
		create_form.especialidad.data=mae1.especialidad
		create_form.email.data=mae1.email
	if request.method=='POST':
		matricula=create_form.matricula.data
		mae1=db.session.query(Maestros).filter(Maestros.matricula==matricula).first()
		mae1.matricula=matricula
		mae1.nombre=str.rstrip(create_form.nombre.data)
		mae1.apellidos=create_form.apellidos.data
		mae1.especialidad=create_form.especialidad.data
		mae1.email=create_form.email.data
		db.session.add(mae1)
		db.session.commit()
		return redirect(url_for('maestros.maestro'))
	return render_template('maestros/modMaestros.html', form=create_form)

@maestros.route("/eliMaestro", methods=['GET', 'POST'])
def eliMaestro():
	create_form = forms.UserFormMaestro(request.form)
	if request.method == 'GET':
		matricula = request.args.get('matricula')
		mae1 = db.session.query(Maestros).filter(Maestros.matricula == matricula).first()
		if mae1:
			create_form.matricula.data = mae1.matricula
			create_form.nombre.data = mae1.nombre
			create_form.apellidos.data = mae1.apellidos
			create_form.email.data = mae1.email
			create_form.especialidad.data = mae1.especialidad
			return render_template("maestros/eliMaestros.html", form=create_form)
		
	if request.method == 'POST':
			matricula = create_form.matricula.data
			mae = db.session.query(Maestros).filter(Maestros.matricula == matricula).first()
			if mae:
				db.session.delete(mae)
				db.session.commit()
			return redirect(url_for('maestros.maestro'))
		
	return render_template("maestros/eliMaestros.html", form=create_form)


@maestros.route('/perfil/<nombre>')
def perfil(nombre):
    return f"Perfil de {nombre}"

