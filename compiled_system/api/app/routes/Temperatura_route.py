from flask import request ,Blueprint ,abort #line:1
from ..services .Conversor import Conversor #line:2
temperatura =Blueprint ('Temperatura',__name__ ,url_prefix ="/temperatura")#line:5
@temperatura .route ('/',methods =['GET'])#line:7
def index ():#line:8
    return 'Teste'#line:9
@temperatura .route ('/fuzzy',methods =['POST'])#line:11
def calcular_temperatura ():#line:12
    OOO0O000O000O000O =request .json #line:13
    OOOO0OO0OO0O00O00 =OOO0O000O000O000O ["type"]#line:14
    if (OOOO0OO0OO0O00O00 =="Celcius"):#line:15
        abort (400 ,"Rota com tipo de temperatura incorreta")#line:16
@temperatura .route ('/fuzzy/celcius',methods =['POST'])#line:19
def calcular_temperatura_celcius ():#line:20
    OOO0O00O000000OOO =request .json #line:21
    O0O00OOO0O00OO0O0 =OOO0O00O000000OOO ["type"]#line:22
    if (O0O00OOO0O00OO0O0 =="Celcius"):#line:23
        O0OOOO0OOOO0OO00O =OOO0O00O000000OOO ["temperatura"]#line:24
        OOOO0O0OO0O000O0O =Conversor (O0OOOO0OOOO0OO00O )#line:25
        O0OOOO0OOOO0OO00O =OOOO0O0OO0O000O0O .celcius_kelvin ()#line:26
    return O0OOOO0OOOO0OO00O


@temperatura.route('/fuzzy/celcius', methods=['POST'])
def calcular_temperatura_celcius():
    data = request.json
    padrao_temperatura = data["type"]
    if(padrao_temperatura == "Celcius"):
        temperatura = data["temperatura"]
        conversao = Conversor(temperatura)
        temperatura = conversao.celcius_kelvin()
    return temperatura