class ControleDeVoo (object ):#line:1
    def __init__ (O0OO0OOO00O0O0O0O ,O0OO0O0O0O0OO0000 ,O00O0OO0OOO00OOOO ,O0OOO0O0O0OO00O00 ,O0OOO00OOO0000OO0 ):#line:3
        if O0OO0OOO00O0O0O0O .verifica_ternario (O0OO0O0O0O0OO0000 ):#line:4
            if O0OO0OOO00O0O0O0O .verifica_ternario (O00O0OO0OOO00OOOO ):#line:5
                if O0OO0OOO00O0O0O0O .verifica_ternario (O0OOO0O0O0OO00O00 ):#line:6
                    if O0OO0OOO00O0O0O0O .verifica_ternario (O0OOO00OOO0000OO0 ):#line:7
                        O0OO0OOO00O0O0O0O .__O0O0OOOOO000OO0O0 =O0OO0O0O0O0OO0000 #line:8
                        O0OO0OOO00O0O0O0O .__O0OOO0000OOOO0O00 =O0OOO0O0O0OO00O00 #line:9
                        O0OO0OOO00O0O0O0O .__O0O000OO000OOO0OO =O00O0OO0OOO00OOOO #line:10
                        O0OO0OOO00O0O0O0O .__OO0OOO00000O000OO =O0OOO00OOO0000OO0 #line:11
                    else :#line:12
                        O0OO0OOO00O0O0O0O .mensagen_erro ('Velocidade')#line:13
                else :#line:14
                    O0OO0OOO00O0O0O0O .mensagen_erro ('Temperatura')#line:15
            else :#line:16
                O0OO0OOO00O0O0O0O .mensagen_erro ('Pressão')#line:17
        else :#line:18
            O0OO0OOO00O0O0O0O .mensagen_erro ('Altitude')#line:19
    def get_altitude (O00OOO0O000O0O0OO ):#line:21
        return O00OOO0O000O0O0OO .__O0O0OOOOO000OO0O0 #line:22
    def get_pressao (OO000O000O0OOOOO0 ):#line:24
        return OO000O000O0OOOOO0 .__O0O000OO000OOO0OO #line:25
    def get_velocidade (OO00O0O00OO0OOO0O ):#line:27
        return OO00O0O00OO0OOO0O .__OO0OOO00000O000OO #line:28
    def get_temperatura (O000O0OO000OO000O ):#line:30
        return O000O0OO000OO000O .__O0OOO0000OOOO0O00 #line:31
    def set_altitude (O0OOO0OOOO00000O0 ,O00OO00OOOOO0OO0O ):#line:33
        if O0OOO0OOOO00000O0 .verifica_ternario (O00OO00OOOOO0OO0O ):#line:34
            O0OOO0OOOO00000O0 .__O0O0OOOOO000OO0O0 =O00OO00OOOOO0OO0O #line:35
        else :#line:36
            O0OOO0OOOO00000O0 .mensagen_erro ('altitude')#line:37
    def set_velocidade (OOO00OOOOOO000000 ,O0OO0OO000O0OO00O ):#line:39
        if OOO00OOOOOO000000 .verifica_ternario (O0OO0OO000O0OO00O ):#line:40
            OOO00OOOOOO000000 .__OO0OOO00000O000OO =O0OO0OO000O0OO00O #line:41
        else :#line:42
            OOO00OOOOOO000000 .mensagen_erro ('velocidade')#line:43
    def set_pressao (O0000OOO0O0OOO0OO ,O000OOO0OO0OO000O ):#line:45
        if O0000OOO0O0OOO0OO .verifica_ternario (O000OOO0OO0OO000O ):#line:46
            O0000OOO0O0OOO0OO .__O0O000OO000OOO0OO =O000OOO0OO0OO000O #line:47
        else :#line:48
            O0000OOO0O0OOO0OO .mensagen_erro ('pressao')#line:49
    def set_temperatura (OOOO0OOOOOO00000O ,OO0OOO000O000OO00 ):#line:51
        if OOOO0OOOOOO00000O .verifica_ternario (OO0OOO000O000OO00 ):#line:52
            OOOO0OOOOOO00000O .__O0OOO0000OOOO0O00 =OO0OOO000O000OO00 #line:53
        else :#line:54
            OOOO0OOOOOO00000O .mensagen_erro ('temperatura')#line:55
    def verifica_nao_numero (O0O0O0O00O0O0O000 ,O0OO00O0O0OO000O0 ):#line:57
        if type (O0OO00O0O0OO000O0 )==int or type (O0OO00O0O0OO000O0 )==float :#line:58
            return True #line:59
        else :#line:60
            return False #line:61
    def verifica_ternario (O0OOO00OOOO0OOO0O ,O00O0O0000O0OOO00 ):#line:63
        if O0OOO00OOOO0OOO0O .verifica_nao_numero (O00O0O0000O0OOO00 ):#line:64
            if O00O0O0000O0OOO00 >=O0OOO00OOOO0OOO0O .__OO0O000000OOO0O0O :#line:65
                return True #line:66
            else :#line:67
                return False #line:68
        else :#line:69
            return False #line:70
    def mensagen_erro (O0O0OOO00O000OO0O ,O00000OO0OOO0O00O ):#line:72
        OOOOO000O0O0OOO0O =O00000OO0OOO0O00O +' incorreta! Favor inserir o dado correto!'#line:73
        print (OOOOO000O0O0OOO0O )#line:74
        return False