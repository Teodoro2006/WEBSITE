from flask import Flask, render_template
import tkinter as tk
from tkinter import messagebox


app = Flask(__name__)

from views import *

if __name__ == '__main__':
    app.run(debug=True, port= 8000)


#Servidor de heroku