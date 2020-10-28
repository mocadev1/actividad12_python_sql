import mysql.connector

def agregar_mascota(bd : mysql.connector.connect, cursor : mysql.connector.cursor) -> None :
    """
    Función para agregar una Mascota a la tabla 'mascota'
    """
    print('\nIngresa los datos de la mascota a registrar...')
    nombre = input('Nombre: ')
    raza = input('Raza: ')
    nacimiento = input('Fecha de Nacimiento en formato AAAA-MM-DD: ')
    rasgos = input('Ingresa los rasgos del animal: ')
    foto = input('Tienes el link a la foto? (S/N)')
    
    if foto == 's' or foto == 'S':
        foto = input('Ingresa el link: ')
    else:
        foto = 'NULL'
    
    if foto == 'NULL':
        consulta = ('INSERT INTO mascota (nombre, raza, nacimiento, rasgos)\n'
                   'VALUES (%s, %s, %s, %s)')
        cursor.execute(consulta, (nombre, raza, nacimiento, rasgos))
    else:
        consulta = ('INSERT INTO mascota (nombre, raza, nacimiento, rasgos, foto)\n'
                   'VALUES (%s, %s, %s, %s, %s)')
        cursor.execute(consulta, (nombre, raza, nacimiento, rasgos, foto))

    bd.commit()
    if cursor.rowcount:
        print('\nSe agregó la mascota\n')
    else:
        print('\nError agregando a la mascota\n')

    return


def mostrar_mascotas(cursor : mysql.connector.cursor) -> None :
    """
    Función que consulta todos los registros de la tabla 'mascota'
    """
    consulta = "SELECT * FROM mascota"
    cursor.execute(consulta)
    for row in cursor.fetchall():
        print(f'\nID: {row[0]}\n'
              f'Nombre: {row[1]}\n'
              f'Raza: {row[2]}\n'
              f'Nacimiento (YYYY-MM-DD): {row[3]}\n'
              f'Rasgos: {row[4]}\n'
              f'Foto(link): {row[5]}\n'
              f'QR: {row[6]}\n'
             )
    return