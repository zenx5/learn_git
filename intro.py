
nombre = input('\n\n¿Cual es tu nombre?\n ')
print('Hola %s bienvenido a Python 3' % nombre)
edad = input('ahora %s, ¿puedes por favor decirme cuantos años tienes?\n ' % nombre )
resultado = 2022 - int(edad)
print('Ok %s, tu naciste en el año %i' % (nombre, resultado))
print('Gracias por participar')
