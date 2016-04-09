#/usr/bin/env python
# -*- coding:utf-8 -*-
from flask import Flask, request, abort, redirect
app = Flask(__name__)

@app.route('/coucou/')
def dire_coucou():
    return 'Coucou !'

@app.route('/')
def racine():
    return "Le chemin de 'racine' est : " + request.path

@app.route('/la')
def ici():
    return "Le chemin de 'ici' est : " + request.path

@app.route('/discussion/')
@app.route('/discussion/page/<int:num_page>')
def mon_chat(num_page = 1):
    num_page = int(num_page)
    premier_msg = 1 + 50 * (num_page - 1)
    dernier_msg = premier_msg + 50
    return 'affichage des messages {} à {}'.format(premier_msg, dernier_msg)

@app.route('/profil/')
def profil():
    if utilisateur_non_identifie:
        abort(401)
    return "Vous êtes bien identifié, voici la page demandée : ..."

@app.route('/test/')
def test():
    return "<h1>test</h1>"

@app.route('/google/')
def redirection_google():
    return redirect('http://www.google.fr')

if __name__ == '__main__':
    app.run()
