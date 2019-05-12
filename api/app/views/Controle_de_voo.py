from flask import request, Blueprint, abort
from ..service.Conversor import Conversor

controle = Blueprint('Controle', __name__, url_prefix="/controle")

@controle.route('/', methods=['GET'])
def index():
    return 'Teste'