#_________________________________________________________

def desplegar_menu():
    print ("MENU")

    print("opcion 1 Agregar estudiante")
    print("opcion 2 Eliminar estudiante")
    print("opcion 3 Calcular promedio de estudiante")
    print("opcion 4 salir")
    
    opcion = int(input("seleccionar opcion: "))
    return opcion
#_________________________________________________________
def agregarEstudiante(listaEstudiantes):
    
    nombre = input("Nombre del alumno:  ")
    edad = input("Edad del alumno:  ")
    espanol = int (input( "Dame la calificacion de espanol: "))
    matematicas = int(input("Dame la calificacion de matematicas:  "))
    historia = int(input("Dame la calificacion de historia: "))
    quimica = int(input("Dame la calificacion de quimica:  "))
   
    materias = [
            {"nombre_materia": "matematicas", "calificacion": matematicas},
            {"nombre_materia": "espanol", "calificacion": espanol},
            {"nombre_materia": "historia", "calificacion": historia},
            {"nombre_materia": "quimica", "calificacion": quimica}
        ]
    estudiante = {
        "nombre": nombre,
        "edad": edad,
        "materias" : materias
    }
    listaEstudiantes.append(estudiante)
    print(estudiante)
    
#_________________________________________________________
def listarAlumnos(listaEstudiantes):
    print("\n")
    print("Lista de alumnos")

    for estudiante in listaEstudiantes:
        print(estudiante["nombre"])
    print("\n")
#_________________________________________________________

def eliminarEstudiante(nombre, lista):
    eliminado = False
    for i in range (0, len(lista) ,1):
        if lista[i]["nombre"] == nombre:
            lista.pop(i)
            eliminado = True
            break 
        
    if eliminado == True:
        print("El alumno " + nombre + " Ha sido eliminado")
    else: 
        print("Alumno no encontrado")

def calcularPromedio(listaEstudiante):
    
    for estudiante in listaEstudiante:       
        listaMateria = estudiante ["materias"]    
        calificacionM = 0
        for materia in listaMateria:              
            calificacionM += materia["calificacion"]
        promedio = calificacionM /4
        
        print("El promedio de " + estudiante["nombre"] + " es: " + str(promedio))
    

estudiantes = [
                {'nombre': 'jaime', 
                'edad': '40', 
                'materias': [
                                {'nombre_materia': 'matematicas','calificacion': 9}, 
                                {'nombre_materia': 'espanol', 'calificacion': 7}, 
                                {'nombre_materia': 'historia', 'calificacion': 9}, 
                                {'nombre_materia': 'quimica', 'calificacion': 9}
                            ]
                },
            {'nombre': 'oscar', 
                'edad': '36', 
                'materias': [{'nombre_materia': 'matematicas','calificacion': 9}, 
                             {'nombre_materia': 'espanol', 'calificacion': 7}, 
                             {'nombre_materia': 'historia', 'calificacion': 6}, 
                             {'nombre_materia': 'quimica', 'calificacion': 9}]},
            {'nombre': 'isabel', 
                'edad': '37', 
                'materias': [{'nombre_materia': 'matematicas','calificacion': 10}, 
                             {'nombre_materia': 'espanol', 'calificacion': 7}, 
                             {'nombre_materia': 'historia', 'calificacion': 6}, 
                             {'nombre_materia': 'quimica', 'calificacion': 10}]},            
                             ]

opcionSeleccionada = 0
while opcionSeleccionada != 4:
    opcionSeleccionada = desplegar_menu()

    if opcionSeleccionada == 1:
        agregarEstudiante(estudiantes)
        listarAlumnos(estudiantes)
        
    elif opcionSeleccionada == 2:
        listarAlumnos(estudiantes)
        alumnoSeleccionado = input("Ingersa el nombre del estudiante a eliminar: \n")
        eliminarEstudiante(alumnoSeleccionado, estudiantes)
        listarAlumnos(estudiantes)

    elif opcionSeleccionada == 3:
        calcularPromedio(estudiantes)
        
    
    
