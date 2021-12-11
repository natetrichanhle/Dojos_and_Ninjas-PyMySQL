from flask import Flask, render_template, request, redirect

from flask_app import app

from flask_app.models import ninjamodel,dojomodel

@app.route('/ninjas')
def ninjas():
    return render_template('ninja.html',dojos = dojomodel.Dojo.get_all())

@app.post('/ninjas/create')
def ninjacreate():
    ninjamodel.Ninja.save(request.form)
    return redirect('/')