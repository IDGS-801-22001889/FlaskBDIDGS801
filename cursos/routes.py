from . import cursos
from flask import render_template, request, redirect, url_for
import forms
from models import db, Curso, Maestros

@cursos.route('/cursos', methods=['GET', 'POST'])
def curso():
    create_form = forms.UserFormCurso(request.form)
    cursos = Curso.query.all()
    return render_template('cursos/listadoCur.html', form=create_form, cursos=cursos)

@cursos.route('/regCurso', methods=['GET', 'POST'])
def regCurso():
    create_form = forms.UserFormCurso(request.form)
    maestros = Maestros.query.all()
    if request.method == 'POST':
        nuevo = Curso(
            nombre=create_form.nombre.data,
            descripcion=create_form.descripcion.data,
            maestro_id=request.form.get('maestro_id')
        )
        db.session.add(nuevo)
        db.session.commit()
        return redirect(url_for('cursos.curso'))
    return render_template('cursos/cursos.html', form=create_form, maestros=maestros)

@cursos.route('/detCurso', methods=['GET', 'POST'])
def detCurso():
    create_form = forms.UserFormCurso(request.form)
    if request.method == 'GET':
        id = request.args.get('id')
        cur1 = db.session.query(Curso).filter(Curso.id == id).first()
        nombre = cur1.nombre
        descripcion = cur1.descripcion
        maestro = cur1.maestro                        
        matricula_mae = cur1.maestro.matricula        
        nombre_mae = cur1.maestro.nombre              
        apellidos_mae = cur1.maestro.apellidos        
    return render_template('cursos/detCursos.html', id=id, nombre=nombre, descripcion=descripcion, maestro=maestro, matricula_mae=matricula_mae, nombre_mae=nombre_mae, apellidos_mae=apellidos_mae                   
    )

@cursos.route('/modCurso', methods=['GET', 'POST'])
def modCurso():
    create_form = forms.UserFormCurso(request.form)
    maestros = Maestros.query.all()
    if request.method == 'GET':
        id = request.args.get('id')
        cur1 = db.session.query(Curso).filter(Curso.id == id).first()
        create_form.id.data = cur1.id
        create_form.nombre.data = cur1.nombre
        create_form.descripcion.data = cur1.descripcion
        create_form.maestro_id.data = cur1.maestro_id  
    if request.method == 'POST':
        id = create_form.id.data
        cur1 = db.session.query(Curso).filter(Curso.id == id).first()
        cur1.nombre = create_form.nombre.data
        cur1.descripcion = create_form.descripcion.data
        cur1.maestro_id = request.form.get('maestro_id')
        db.session.add(cur1)
        db.session.commit()
        return redirect(url_for('cursos.curso'))
    return render_template('cursos/modCursos.html', form=create_form, maestros=maestros)

@cursos.route('/eliCurso', methods=['GET', 'POST'])
def eliCurso():
    create_form = forms.UserFormCurso(request.form)
    if request.method == 'GET':
        id = request.args.get('id')
        cur1 = db.session.query(Curso).filter(Curso.id == id).first()
        if cur1:
            create_form.id.data = cur1.id
            create_form.nombre.data = cur1.nombre
            create_form.descripcion.data = cur1.descripcion
            create_form.maestro_id.data = cur1.maestro_id      
            return render_template('cursos/eliCursos.html',
                form=create_form,
                nombre_mae=cur1.maestro.nombre,                
                apellidos_mae=cur1.maestro.apellidos           
            )
    if request.method == 'POST':
        id = create_form.id.data
        cur1 = db.session.query(Curso).filter(Curso.id == id).first()
        if cur1:
            db.session.delete(cur1)
            db.session.commit()
        return redirect(url_for('cursos.curso'))
    return render_template('cursos/eliCursos.html', form=create_form)