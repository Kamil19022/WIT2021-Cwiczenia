Logowanie = True
while Logowanie:
    ussername = input("Podaj login: ")
    password  =  input ( "Podaj hasło:" )
    if ussername == 'Admin' and password == '1234':
        break
print("Zalogowano poprawnie")
