import sys #line:1
sys .path .append ("..")#line:2
from services .Triangular import Triangular #line:4
from services .Medidas import Medidas #line:5
from services .Conversor import Conversor #line:6
from models .Temperatura_model import Temperatura_Model #line:7
class AltitudeModel (object ):#line:9
    def __init__ (O0OO0O000O0OO00OO ,OO00O0O000O000OOO ):#line:11
        O0OO0O000O0OO00OO .__OOOOOOOO0O00OO000 =OO00O0O000O000OOO #line:12
        O0OO0O000O0OO00OO .__OOOOOOOOO0O0O0OOO =0 #line:13
        O0OO0O000O0OO00OO .__O000OOO0O0O00OO0O =Medidas ()#line:14
        O0OO0O000O0OO00OO .__OO000OO000OO0O000 =Conversor ()#line:15
        O0OO0O000O0OO00OO .__OOO00O0OO00OO0OOO =Temperatura_Model (O0OO0O000O0OO00OO .__O000OO000000OOO0O ())#line:16
    def __O000OO000000OOO0O (O0O000O0O00O00OOO ):#line:18
        OOOO000OOO0OOO000 =((O0O000O0O00O00OOO .__OOOOOOOO0O00OO000 *0.3048 )*-2 )#line:19
        return OOOO000OOO0OOO000 #line:20
    def temperatura_atual (OO0OOOOOO00OO0OOO ):#line:22
        return OO0OOOOOO00OO0OOO .__OOO00O0OO00OO0OOO .valor_atual ()#line:23
    def calculo_fuzzy (OO00OO0OOO0O0OO0O ):#line:25
        O000OO000OOOOO0OO =Triangular (OO00OO0OOO0O0OO0O .__OOOOOOOO0O00OO000 ,OO00OO0OOO0O0OO0O .__O000OOO0O0O00OO0O .altitude ())#line:26
        OO00OO0OOO0O0OO0O .__OOOOOOOOO0O0O0OOO =100 *O000OO000OOOOO0OO .funcao_tringular ()#line:27
    @property #line:29
    def altitude_taxa (OOO0OO0O000OO0O0O ):#line:30
        return OOO0OO0O000OO0O0O .__OOOOOOOOO0O0O0OOO #line:31
teste =AltitudeModel (12000 )#line:34
print (teste .temperatura_atual ())#line:35