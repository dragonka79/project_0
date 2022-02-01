from flask import Flask


app = Flask(__name__)

import quokka.views.ui_views
# A fenti import azért kell az 'app' def alá, hogy a körkörös importot
# feloldjuk; ha az app fölött lenne, akkor a ui_views importjában az app-ot
# importálja de még azelőtt, hogy az app létre lett volna hívva.
# QFS-03 26-ik perc