from . import inscripciones
from flask import render_template, request, redirect, url_for
from models import db, Curso, Alumnos, Inscripcion

@inscripciones.route('/inscripciones', methods=['GET'])
def inscripcion():
    alumnos = Alumnos.query.all()
    return render_template('inscripciones/listaIns.html', alumnos=alumnos)

@inscripciones.route('/inscribir', methods=['GET', 'POST'])
def inscribir():
    if request.method == 'GET':
        id = request.args.get('id')
        alumno = db.session.query(Alumnos).filter(Alumnos.id == id).first()
        cursos = Curso.query.filter(~Curso.alumnos.any(id=alumno.id)).all()
        return render_template('inscripciones/inscribir.html', alumno=alumno, cursos=cursos)
    
    if request.method == 'POST':
        alumno_id = request.form.get('alumno_id')
        curso_id  = request.form.get('curso_id')
        curso  = db.session.query(Curso).filter(Curso.id == curso_id).first()
        alumno = db.session.query(Alumnos).filter(Alumnos.id == alumno_id).first()
        curso.alumnos.append(alumno)
        db.session.commit()
        return redirect(url_for('inscripciones.inscripcion'))

@inscripciones.route('/alumnosCurso', methods=['GET'])
def alumnosCurso():
    id = request.args.get('id')
    curso = db.session.query(Curso).filter(Curso.id == id).first()
    alumnos = curso.alumnos
    return render_template('inscripciones/cursosAlu.html', curso=curso, alumnos=alumnos)

@inscripciones.route('/cursosAlumno', methods=['GET'])
def cursosAlumno():
    id = request.args.get('id')
    alumno = db.session.query(Alumnos).filter(Alumnos.id == id).first()
    cursos = alumno.cursos
    return render_template('inscripciones/alumnosCur.html', alumno=alumno, cursos=cursos)

@inscripciones.route('/eliAlumnoCurso', methods=['GET', 'POST'])
def eliAlumnoCurso():
    if request.method == 'GET':
        curso_id  = request.args.get('curso_id')
        alumno_id = request.args.get('alumno_id')
        curso  = db.session.query(Curso).filter(Curso.id == curso_id).first()
        alumno = db.session.query(Alumnos).filter(Alumnos.id == alumno_id).first()
        return render_template('inscripciones/eliAlumnoCurso.html', curso=curso, alumno=alumno)
    
    if request.method == 'POST':
        curso_id  = request.form.get('curso_id')
        alumno_id = request.form.get('alumno_id')
        curso  = db.session.query(Curso).filter(Curso.id == curso_id).first()
        alumno = db.session.query(Alumnos).filter(Alumnos.id == alumno_id).first()
        curso.alumnos.remove(alumno) 
        db.session.commit()
        return redirect(url_for('inscripciones.alumnosCurso', id=curso_id))