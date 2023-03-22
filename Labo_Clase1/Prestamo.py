
saldo = 500000.0
tasa = 0.05
pago_mensual = 2684.11
total_pagado = 0.0
while saldo > 0:
    saldo = saldo * (1+tasa/12) - pago_mensual  #Basicamente saco un prestamo con un saldo de 500.000 $ y cada mes debe pagar 2684.11 $.Cada mes se le aplica un recargo de 5%/12 al saldo correspondiente osea a lo que le falta pagar
    total_pagado = total_pagado + pago_mensual  #Es decir mientras mas grande o mas pagos mensaules haga, menor va a ser el saldo de la deuda, por lo que menos va a ser el ineteres aplicado a esta.   
#print('Total pagado', round(total_pagado, 2))   #Entonces si pagas un pago mensual mas grande, pagas menos interes al final

# PAgo de deuda modificado

saldo = 500000.0
tasa = 0.05
pago_mensual = 2684.11
total_pagado = 0.0
mes = 0
while saldo > 0:
    if mes < 12:
        saldo = saldo * (1+tasa/12) - (pago_mensual +1000) #Basicamente saco un prestamo con un saldo de 500.000 $ y cada mes debe pagar 2684.11 $.Cada mes se le aplica un recargo de 5%/12 al saldo correspondiente osea a lo que le falta pagar
        total_pagado = total_pagado + (pago_mensual + 1000)  #Es decir mientras mas grande o mas pagos mensaules haga, menor va a ser el saldo de la deuda, por lo que menos va a ser el ineteres aplicado a esta.       
        mes += 1
    else:
        saldo = saldo * (1+tasa/12) - pago_mensual  #Basicamente saco un prestamo con un saldo de 500.000 $ y cada mes debe pagar 2684.11 $.Cada mes se le aplica un recargo de 5%/12 al saldo correspondiente osea a lo que le falta pagar
        total_pagado = total_pagado + pago_mensual  #Es decir mientras mas grande o mas pagos mensaules haga, menor va a ser el saldo de la deuda, por lo que menos va a ser el ineteres aplicado a esta.   
        mes += 1
#print('Total pagado', round(total_pagado, 2), mes)   #Entonces si pagas un pago mensual mas grande, pagas menos interes al final

# PAgo de deuda modificadoa partir de sexto año

saldo = 500000.0
tasa = 0.05
pago_mensual = 2684.11
total_pagado = 0.0
mes = 0
pago_extra = 1000
while saldo > 0:
    if mes <= 108 and mes >= 61 :
        saldo = saldo * (1+tasa/12) - (pago_mensual +pago_extra) #Basicamente saco un prestamo con un saldo de 500.000 $ y cada mes debe pagar 2684.11 $.Cada mes se le aplica un recargo de 5%/12 al saldo correspondiente osea a lo que le falta pagar
        total_pagado = total_pagado + (pago_mensual + pago_extra)  #Es decir mientras mas grande o mas pagos mensaules haga, menor va a ser el saldo de la deuda, por lo que menos va a ser el ineteres aplicado a esta.       
        mes += 1
    else:
        saldo = saldo * (1+tasa/12) - pago_mensual  #Basicamente saco un prestamo con un saldo de 500.000 $ y cada mes debe pagar 2684.11 $.Cada mes se le aplica un recargo de 5%/12 al saldo correspondiente osea a lo que le falta pagar
        total_pagado = total_pagado + pago_mensual  #Es decir mientras mas grande o mas pagos mensaules haga, menor va a ser el saldo de la deuda, por lo que menos va a ser el ineteres aplicado a esta.   
        mes += 1
print('Total pagado', round(total_pagado, 2), mes)   #Entonces si pagas un pago mensual mas grande, pagas menos interes al final
