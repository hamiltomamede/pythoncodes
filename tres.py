dia =float(input('digite os dias:'))
hora=float(input('digite as horas:'))
minuto=float(input('digite os minutos:'))
segundo=1
dia = dia*segundo*86400
hora=hora*segundo*3600
minuto=minuto*segundo*60
segundos=float(input('digite os segundos:'))
total=dia+hora+minuto+segundos 
print ('total %f segundos'%total)