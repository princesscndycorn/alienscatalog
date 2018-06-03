from flask import Flask, render_template, request, redirect, jsonify, url_for
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from databaseSetup import Categorys, Base, CatItems

engine = create_engine('sqlite:///waylandDatabase.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

app = Flask(__name__)


@app.route('/')
def homePage():
    categorys = session.query(Categorys).all()
    output = ''
    for n in categorys:
        output += '<br>'
        output += n.name
        output += '<br>'
    return output

@app.route('/Catalog/<int:cat_name>/')
def showCat(cat_name):
    return "To be completed later"

@app.route('/edit/')
def editPage():
    return render_template('edit.html')

@app.route('/delete/')
def deletePage():
    return render_template('delete.html')

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
