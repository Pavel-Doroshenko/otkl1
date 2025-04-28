from flask import Flask, render_template, request, redirect, url_for
#from populate import DBSession
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Resource_shutdowns, Base

app = Flask(__name__)

engine = create_engine('sqlite:///shutdowns.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

#функция отображения всех записей на странице
@app.route('/')
def index():
    resource_shutdowns = session.query(Resource_shutdowns).all()
    return render_template('index.html', resource_shutdowns=resource_shutdowns)

#функия добавления записей
@app.route('/new', methods=['GET', 'POST'])
def new_form():
    if request.method == 'POST':
        recording_date = request.form['recording_date']
        adress = request.form['adress']
        type_of_resource = request.form['type_of_resource']
        shutdown_date = request.form['shutdown_date']
        renewal_date = request.form['renewal_date']

        record = Resource_shutdowns(recording_date=request.form['recording_date'], adress=request.form['adress'], type_of_resource=request.form['type_of_resource'], shutdown_date=request.form['shutdown_date'], renewal_date=request.form['renewal_date'])
        session.add(record)
        session.commit()
        return redirect(url_for('index'))
    return render_template('add_form.html')

@app.route('/<int:record_id>/delete/', methods=['GET', 'POST'])
def delete_record(record_id):
    del_record = session.query(Resource_shutdowns).filter_by(id=record_id).one()
    if request.method == 'POST':
        session.delete(del_record)
        session.commit()
        return redirect(url_for('index', record_id=record_id))
    return render_template('delete.html')

@app.route('/<int:record_id>/edit/', methods=['GET', 'POST'])
def edit_record(record_id):
    ed_record = session.query(Resource_shutdowns).filter_by(id=record_id).one()
    if request.method == 'POST':
        recording_date = request.form['recording_date']
        adress = request.form['adress']
        type_of_resource = request.form['type_of_resource']
        shutdown_date = request.form['shutdown_date']
        renewal_date = request.form['renewal_date']

        session.add(ed_record)
        session.commit()
        return redirect(url_for('index', record_id=record_id))
    return render_template('edit.html')


if __name__ == '__main__':
    app.run(debug=True)