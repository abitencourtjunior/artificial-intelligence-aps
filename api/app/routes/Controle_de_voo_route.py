from flask import request, Blueprint, abort
from ..services.Conversor import Conversor

controle = Blueprint('Controle', __name__, url_prefix="/controle")

@controle.route('/', methods=['GET'])
def index():
    return 'Teste'