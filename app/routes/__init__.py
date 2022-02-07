from flask import Flask, Blueprint
from app.routes.serie_routes import bp_series 

def init_app(app: Flask):
    app.register_blueprint(bp_series)