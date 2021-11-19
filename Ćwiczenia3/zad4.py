dane_logowania = {'Admin': '1234'}

not_authenticated = True

while not_authenticated:
    login  =  input ( "Podaj login:" )
    Password  =  input ( "Podaj hasło:" )     
    if  Password == dane_logowania . get ( login ):
        print ( "Logowanie poprawne" )
        not_authenticated=False
    else:
        print ( "Niepoprawne logowanie" )  
