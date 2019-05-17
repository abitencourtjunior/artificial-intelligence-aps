from flask import Flask #line:1
from .routes .Temperatura_route import temperatura #line:2
from .routes .Altitude_route import altitude #line:3
from .routes .Velocidade_route import velocidade #line:4
from .routes .Controle_de_voo_route import controle #line:5
app =Flask (__name__ )#line:7
app .register_blueprint (temperatura ,url_prefix ="/api/temperatura")#line:9
app .register_blueprint (altitude ,url_prefix ="/api/altitude")#line:10
app .register_blueprint (velocidade ,url_prefix ="/api/velocidade")#line:11
app .register_blueprint (controle ,url_prefix ="/api/controle")#line:12
@app .route ("/")#line:14
def index ():#line:15
    return "API - Controle de Vôo"#line:16
if __name__ =='__main__':#line:18
    app .run (debug =True )