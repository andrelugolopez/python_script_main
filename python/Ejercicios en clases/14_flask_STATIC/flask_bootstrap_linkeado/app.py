# -*- coding: utf-8 -*-
from flask import Flask, render_template, request, session, redirect, url_for


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')







app.run(debug = False, port=5000)

