dystans =  250
pociag = 90  #250/165*60 
samochod = int ( input ( "Jak szybko chcesz jechać samochodem" ))
if  samochod > pociag :
    print ( "Samochód będzie szybszy" )
elif  samochod == pociag :
    print ('taki sam czas')

else:
    print ( "Pociąg będzie szybszy" )

