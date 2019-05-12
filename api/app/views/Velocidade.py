from flask import request, Blueprint, abort
from ..service.Conversor import Conversor

velocidade = Blueprint('Velocidade', __name__, url_prefix="/velocidade")

@velocidade.route('/', methods=['GET'])
def index():
    return 'Teste'

