import os .path #line:1
class ArquivoOut (object ):#line:3
    __O0OO00OOO000OOO0O ='terminal'#line:5
    def get_saida (OO00O0OO0O0O00O0O ):#line:7
        return OO00O0OO0O0O00O0O .__O0OO00OOO000OOO0O #line:8
    def set_saida (OO0O0OOO0OO0O0O00 ,OOO00OOOO0O0O0OO0 ):#line:10
        if OOO00OOOO0O0O0OO0 =="terminal"or OOO00OOOO0O0O0OO0 =="txt":#line:11
            OO0O0OOO0OO0O0O00 .__O0OO00OOO000OOO0O =OOO00OOOO0O0O0OO0 #line:12
        else :#line:13
            print ("tipo de saida nao reconhecida")#line:14
            return False #line:15
    def output (O0OOO0O0OO0OOOO00 ,saida =None ):#line:17
        if O0OOO0O0OO0OOOO00 .__O0OO00OOO000OOO0O =="txt":#line:18
            if os .path .isfile ('./output.txt'):#line:19
                OOO0O000O0OOO0O0O =open ('log.txt','r')#line:20
                O0000000O000O0OOO =OOO0O000O0OOO0O0O .readlines ()#line:21
                O0000000O000O0OOO .append (saida )#line:22
                OOO0O000O0OOO0O0O =open ('log.txt','w')#line:23
                OOO0O000O0OOO0O0O .writelines (O0000000O000O0OOO )#line:24
                OOO0O000O0OOO0O0O .close ()#line:25
            else :#line:26
                pass #line:27
        elif O0OOO0O0OO0OOOO00 .__O0OO00OOO000OOO0O =="terminal":#line:28
            print (saida )#line:29
        else :#line:30
            print ("tipo de saida nao reconhecida")#line:31
            return False