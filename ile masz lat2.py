print('Ile masz lat?')
wiek=int(input())
if (wiek>=21):
    print('Możesz prowadzić samochód oraz głosować w wyborach')
elif (wiek<=20 and wiek>=17):
        print('Możesz prowadzić samochód')
else:
        print('Nie możesz głosować ani prowadzić samochodu')
