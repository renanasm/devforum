import dash
from dash import Dash, Input, Output, State, callback_context
import dash_bootstrap_components as dbc
from dash.dependencies import ALL
from dash import html, dcc
from flask import Flask
import pandas as pd
import datetime
import json
import os
from dash_table import DataTable
import calendar
from app import *
from index import *
import pdb

deploy = Flask(__name__)



@deploy.route("/calendario")
def homepage():
    return render_template("index.py")
app.run()