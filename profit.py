kapital = int(input('Podaj kapitał początkowy'))
wplywy = int(input('Podaj miesięczne wpływy'))
inwestycja = int(input('Podaj okres inwestowania w miesiącach'))
pozadana_wartosc = int(input('Podaj pożądaną wartość inwestycji'))

zysk=int(kapital+wplywy*inwestycja)+(kapital+wplywy*inwestycja)*0.02
if zysk > pozadana_wartosc:
    print('Twoja zainwestowana kwota będzie wyższa niż pożądana i wynosi',zysk)
else:
    print('Twoja zainwestowana kwota będzie niższa niż pożądana i wynosi',zysk)

