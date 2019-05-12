from flask import request, Blueprint, abort
from ..service.Conversor import Conversor

altitude = Blueprint('Altitude', __name__, url_prefix="/altitude")

@altitude.route('/', methods=['GET'])
def index():
    return 'Teste'