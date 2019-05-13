from flask import Flask
from .routes.Temperatura_route import temperatura
from .routes.Altitude_route import altitude
from .routes.Velocidade_route import velocidade
from .routes.Controle_de_voo_route import controle

app = Flask(__name__)

app.register_blueprint(temperatura, url_prefix="/api/temperatura")
app.register_blueprint(altitude, url_prefix="/api/altitude")
app.register_blueprint(velocidade, url_prefix="/api/velocidade")
app.register_blueprint(controle, url_prefix="/api/controle")

@app.route("/")
def index():
    return "API - Controle de Vôo"

if __name__ == '__main__':
    app.run(debug=True)