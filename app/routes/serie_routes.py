from flask import Blueprint
from app.controllers import create, series,select_by_id

bp_series = Blueprint("series", __name__)

bp_series.post("/series")(create)
bp_series.get("/series")(series)
bp_series.get("/series/<int:serie_id>")(select_by_id)