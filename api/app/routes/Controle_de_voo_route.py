from flask import request, Blueprint, abort
from ..services.Conversor import Conversor
from api.app.models.ControleDeVoo_model import ControleDeVoo

controle = Blueprint('Controle', __name__, url_prefix="/controle")

@controle.route('/', methods=['GET'])
def index():
    return 'API - Controle de Voo'

@controle.route('/fuzzy', methods=['POST'])
def controle_de_voo_calcular():
    data = request.json
    print(data)
    padrao_temperatura = int(data["temperatura"])
    padrao_altitude = int(data["altitude"])
    padrao_velocidade = int(data["velocidade"])
    Controle = ControleDeVoo(padrao_altitude, padrao_temperatura, padrao_velocidade)
    Controle.fuzzificacao_controle()
    retorno = str(Controle.defuzificacao_controle())
    return retorno
