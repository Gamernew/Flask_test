#! /usr/bin/python
# -*- coding:utf-8 -*-

from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def accueil():
    mots = ["Bonjour", "a", "toi", "visiteur."]
    return render_template('accueil.html', titre="Bienvenue", mots=mots)

@app.route('/date')
def date():
    d = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    return render_template('date.html', la_date=d)

if __name__ == '__main__':
    app.run(debug=True)
