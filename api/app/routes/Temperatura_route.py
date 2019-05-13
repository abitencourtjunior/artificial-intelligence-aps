from flask import request, Blueprint, abort
from ..services.Conversor import Conversor


temperatura = Blueprint('Temperatura', __name__, url_prefix="/temperatura")

@temperatura.route('/', methods=['GET'])
def index():
    return 'Teste'

@temperatura.route('/fuzzy', methods=['POST'])
def calcular_temperatura():
    data = request.json
    padrao_temperatura = data["type"]
    if(padrao_temperatura == "Celcius"):
        abort(400, "Rota com tipo de temperatura incorreta")


@temperatura.route('/fuzzy/celcius', methods=['POST'])
def calcular_temperatura_celcius():
    data = request.json
    padrao_temperatura = data["type"]
    if(padrao_temperatura == "Celcius"):
        temperatura = data["temperatura"]
        conversao = Conversor(temperatura)
        temperatura = conversao.celcius_kelvin()
    return temperatura