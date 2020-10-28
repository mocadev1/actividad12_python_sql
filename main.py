import mysql.connector
import functions

bd = mysql.connector.connect(user = 'admin',
                             password = 'ETm2020',
                             database = 'encuentra_tu_mascota')

cursor = bd.cursor()

menu = {}
menu['1'] = 'Agregar Mascota.'
menu['2'] = 'Mostrar Mascotas.'
menu['0'] = 'Salir.'

while True: 
    opciones = menu.keys()
#   options.sort()
    for entrada in opciones: 
        print(f'{entrada}) {menu[entrada]}')

    op  = input('\nSelecciona una opción: ')
    if op == '1':
        functions.agregar_mascota(bd, cursor)
    elif op == '2':
        functions.mostrar_mascotas(cursor)
    elif op == '0':
        break
    else:
        print('Opción Inválida, por favor intenta nuevamente :).')




