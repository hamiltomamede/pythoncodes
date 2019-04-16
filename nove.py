km=float(input('Quantos km rodados?'))
dia=int(input('Quantos dias?'))
v_dia=60
v_km=0.15
total = float((dia*v_dia)+(km*v_km))
print ('O valor total e: R$ %.2f reais' %total)