import sys #line:1
sys .path .append ("..")#line:2
from services .Triangular import Triangular #line:4
from services .Medidas import Medidas #line:5
from services .Conversor import Conversor #line:6
class Temperatura_Model (object ):#line:8
    def __init__ (OO000000OOO0000O0 ,valor =None ):#line:10
        OO000000OOO0000O0 .__OO0OO00O0000O000O =valor #line:11
        OO000000OOO0000O0 .__OO00O000O0O0OO0O0 =0 #line:12
        OO000000OOO0000O0 .__OOO0OO00O0OOOOOO0 =Medidas ()#line:13
        OO000000OOO0000O0 .__O0O00O0O000000O00 =Conversor ()#line:14
    def calculo_fuzzy (OO0OO000OOOOO0000 ):#line:16
        OO0OO000OOOOO0000 .__OO0OO00O0000O000O =OO0OO000OOOOO0000 .__O0O00O0O000000O00 .celcius_kelvin (OO0OO000OOOOO0000 .__OO0OO00O0000O000O )#line:17
        O0O0000O0OO0O0OOO =Triangular (OO0OO000OOOOO0000 .__OO0OO00O0000O000O ,OO0OO000OOOOO0000 .__OOO0OO00O0OOOOOO0 .temperatura ())#line:18
        OO0OO000OOOOO0000 .__OO00O000O0O0OO0O0 =100 *O0O0000O0OO0O0OOO .funcao_tringular ()#line:19
    def defuzzificacao_temperatura (O0OOOO0O00O0000O0 ):#line:21
        if (O0OOOO0O00O0000O0 .__OO0OO00O0000O000O ==218 ):#line:22
            return f'Temperatura de Vôo: {O0OOOO0O00O0000O0.__conversao.kelvin_celcius(O0OOOO0O00O0000O0.__valor)} °C - {O0OOOO0O00O0000O0.taxa} %'#line:23
    @property #line:26
    def taxa (O0000OO0O0O00O00O ):#line:27
        return O0000OO0O0O00O00O .__OO00O000O0O0OO0O0 #line:28
    def valor_atual (O00O0OOO0OO0O0O00 ):#line:30
        return O00O0OOO0OO0O0O00 .__OO0OO00O0000O000O #line:31
teste =Temperatura_Model (-55 )#line:33
teste .calculo_fuzzy ()#line:34
print (teste .taxa )#line:35
print (teste .valor_atual ())#line:36
print (teste .defuzzificacao_temperatura ())