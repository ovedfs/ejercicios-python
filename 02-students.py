# Registro de estudiantes:

## Crea un programa que permita al usuario ingresar nombres y calificaciones de estudiantes.
## Utiliza un diccionario para almacenar los datos, donde las claves son los nombres de los estudiantes y los valores son las calificaciones.
## Implementa funciones para agregar estudiantes, eliminar estudiantes y mostrar la lista de estudiantes junto con sus calificaciones.

students = {}

def get_info():
    name = input('Nombre del estudiante: ')
    scores = input('Calificaciones (separadas por comas): ')
    scores = scores.split(',')

    return name, scores

def delete_student():
    name = input('Ingresa el nombre del alumno a eliminar: ')
    
    if name in students:
        del students[name]
        print('Estudiante eliminado')
        input()
    else:
        print('No hay registro de este estudiante')
        input()

def show_students():
    for student, scores in students.items():
        print(f"{student}: {scores}")


def menu():
    return '''
        1) Registrar calificaciones de un alumno
        2) Mostrar calificaciones de todos
        3) Eliminar estudiante
        4) Salir

        Elija una opción: 
    '''

while True:
    option = input(menu())

    if option == '1':
        name, scores = get_info()
        students[name] = scores
    elif option == '2':
        show_students()
    elif option == '3':
        delete_student()
    elif option == '4':
        break
    else:
        print('Respuesta no valida')


print('Programa finalizado...')

