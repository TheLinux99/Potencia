"""
Programa diseñado para el curso de Procesamiento Electronico de Potencia EL4201
Instituto Tecnologico de Costa Rica

Desarrollado por:
José Alejandro Angulo Durán
Adrian Nuñez Reina
Carlos Carmona
Carlos Elizondo

Version de python utilizada: 3.8

Librerias nescesarias:

math
wget
json
os
numpy
matplotlib
pvlib

"""


from PlotFunctions import *

def Menu5Panel(latitude,longitude,Tilt):

    op = 0
    correct = False
    accept = False
    angle = 0
    print("\n================================================\n"
          "Menu Principal para Paneles \n"
          "================================================\n")
    print("\n------------------------------------------------\n"
          "Ingrese la inclinación del Panel"
          "\n------------------------------------------------\n \n")
    while(correct != True):
        try:
            angle = float(input("Ángulo de inclinación: "))
            correct = True
        except:
            print("Por favor ingrese un ángulo válido")
    correct = False

    while (accept == False):

        print("\n------------------------------------------------\n"
              "Seleccione la accion que desea realizar"
              "\n------------------------------------------------\n \n"
              "1-Grafica de irradiacion durante un dia especifico\n"
              "2-Grafica de irradiacion para el año\n"
              "3-Ingresar nueva ubicacion\n"
              "4-Salir\n")
        try:
            op = int(input("Opcion elegida: "))
        except:
            op == 0
        if (op == 1):

            """Grafica de radiacion durante un dia especifico"""

            print("\n================================================\n"
                  "Grafica de irradiacion durante un dia especifico \n"
                  "================================================\n")

            print("\n------------------------------------------------\n"
                  " Primeramente se deben ingresar algunos datos: "
                  "\n------------------------------------------------\n")

            # Limpia el archivo json de la nasa
            try:
                os.remove(ROOT_DIR + "/NasaData/DataSet.json")
                print("")
            except:
                print("")

            # Revisa que los meses y dias esten bien

            try:
                month = int(input("Ingrese el mes:"))
                day = int(input("Ingrese el dia:"))
                if (month > 12 or month < 0):
                    # Genera un error voluntariamente para saltar al except
                    int("Papas")
            except:
                print("Debe ingresar el mes y dia en formato numerico")
            # DayCount se utiliza para comprobar que le dia este bien
            daycount = GetDay(month, day)
            if (daycount != 0):
                RDDE(latitude, longitude,  day,month,[Tilt,Tilt,Tilt,Tilt + 90,Tilt + 90] ,tz = 'America/Costa_Rica',angle = [-angle,90,angle, -angle, angle])
            if (daycount == 0):
                print("El dia no es valido, este programa no toma en cuenta el 29 de febrero.")
        elif (op == 2):

            """Grafica de radiacion para el año"""

            print("\n================================================\n"
                  "Grafica de irradiacion para el año \n"
                  "================================================\n")

            RA(latitude, longitude, [Tilt,Tilt,Tilt,Tilt + 90,Tilt + 90] ,tz = 'America/Costa_Rica',angle = [-angle,90,angle, -angle, angle])

        elif (op == 3):

            Menu()
            accept = True

        elif (op == 4):

            """Salir"""

            accept = True
        else:
            print("Se debe seleccionar una opcion utilizando un numero del 1 al 4")

    return 0

def Menu3Panel(latitude,longitude,Tilt):

    op = 0
    correct = False
    accept = False
    angle = 0
    print("\n================================================\n"
          "Menu Principal para Paneles \n"
          "================================================\n")
    print("\n------------------------------------------------\n"
          "Ingrese la inclinación del Panel"
          "\n------------------------------------------------\n \n")
    while(correct != True):
        try:
            angle = float(input("Ángulo de inclinación: "))
            correct = True
        except:
            print("Por favor ingrese un ángulo válido")
    correct = False

    while (accept == False):

        print("\n------------------------------------------------\n"
              "Seleccione la accion que desea realizar"
              "\n------------------------------------------------\n \n"
              "1-Grafica de irradiacion durante un dia especifico\n"
              "3-Grafica de irradiacion para el año\n"
              "3-Ingresar nueva ubicacion\n"
              "4-Salir\n")
        try:
            op = int(input("Opcion elegida: "))
        except:
            op == 0
        if (op == 1):

            """Grafica de radiacion durante un dia especifico"""

            print("\n================================================\n"
                  "Grafica de irradiacion durante un dia especifico \n"
                  "================================================\n")

            print("\n------------------------------------------------\n"
                  " Primeramente se deben ingresar algunos datos: "
                  "\n------------------------------------------------\n")

            # Limpia el archivo json de la nasa
            try:
                os.remove(ROOT_DIR + "/NasaData/DataSet.json")
                print("")
            except:
                print("")

            # Revisa que los meses y dias esten bien

            try:
                month = int(input("Ingrese el mes:"))
                day = int(input("Ingrese el dia:"))
                if (month > 12 or month < 0):
                    # Genera un error voluntariamente para saltar al except
                    int("Papas")
            except:
                print("Debe ingresar el mes y dia en formato numerico")
            # DayCount se utiliza para comprobar que le dia este bien
            daycount = GetDay(month, day)
            if (daycount != 0):
                RDDE(latitude, longitude,  day,month, [Tilt,Tilt,Tilt] ,tz = 'America/Costa_Rica',angle = [-angle,90,angle])
            if (daycount == 0):
                print("El dia no es valido, este programa no toma en cuenta el 29 de febrero.")
        elif (op == 2):

            """Grafica de radiacion para el año"""

            print("\n================================================\n"
                  "Grafica de irradiacion para el año \n"
                  "================================================\n")

            RA(latitude, longitude, [Tilt,Tilt,Tilt] ,tz = 'America/Costa_Rica',angle = [-angle,90,angle])

        elif (op == 3):

            Menu()
            accept = True

        elif (op == 4):

            """Salir"""

            accept = True
        else:
            print("Se debe seleccionar una opcion utilizando un numero del 1 al 4")

    return 0

def Menu1Panel(latitude,longitude,Tilt):

    op = 0
    correct = False
    accept = False
    angle = 0
    print("\n================================================\n"
          "Menu Principal para Paneles \n"
          "================================================\n")
    print("\n------------------------------------------------\n"
          "Ingrese la inclinación del Panel"
          "\n------------------------------------------------\n \n")
    while(correct != True):
        try:
            angle = float(input("Ángulo de inclinación: "))
            correct = True
        except:
            print("Por favor ingrese un ángulo válido")
    correct = False

    while (accept == False):

        print("\n------------------------------------------------\n"
              "Seleccione la accion que desea realizar"
              "\n------------------------------------------------\n \n"
              "1-Grafica de irradiacion durante un dia especifico\n"
              "2-Grafica de irradiacion para el año\n"
              "3-Ingresar nueva ubicacion\n"
              "4-Salir\n")
        try:
            op = int(input("Opcion elegida: "))
        except:
            op == 0

        if (op == 1):

            """Grafica de radiacion durante un dia especifico"""

            print("\n================================================\n"
                  "Grafica de irradiacion durante un dia especifico \n"
                  "================================================\n")

            print("\n------------------------------------------------\n"
                  " Primeramente se deben ingresar algunos datos: "
                  "\n------------------------------------------------\n")

            # Limpia el archivo json de la nasa
            try:
                os.remove(ROOT_DIR + "/NasaData/DataSet.json")
                print("")
            except:
                print("")

            # Revisa que los meses y dias esten bien

            try:
                month = int(input("Ingrese el mes:"))
                day = int(input("Ingrese el dia:"))
                if (month > 12 or month < 0):
                    # Genera un error voluntariamente para saltar al except
                    int("Papas")
            except:
                print("Debe ingresar el mes y dia en formato numerico")
            # DayCount se utiliza para comprobar que le dia este bien
            daycount = GetDay(month, day)
            if (daycount != 0):
                RDDE(latitude, longitude, day,month,[Tilt] ,tz = 'America/Costa_Rica',angle = [angle])
            if (daycount == 0):
                print("El dia no es valido, este programa no toma en cuenta el 29 de febrero.")
        elif (op == 2):

            """Grafica de radiacion para el año"""

            print("\n================================================\n"
                  "Grafica de irradiacion para el año \n"
                  "================================================\n")

            RA(latitude, longitude, [Tilt] ,tz = 'America/Costa_Rica',angle = [angle])

        elif (op == 3):

            Menu()
            accept = True

        elif (op == 4):

            """Salir"""

            accept = True
        else:
            print("Se debe seleccionar una opcion utilizando un numero del 1 al 4")



def MenuPaneles(latitude,longitude,Tilt):

    op = 0
    correct = False
    accept = False

    while (accept == False):
        print("\n================================================\n"
              "Menu Principal para Paneles \n"
              "================================================\n")

        print("\n------------------------------------------------\n"
              "Que configuración desea utilizar"
              "\n------------------------------------------------\n \n"
              "1-Un único panel\n"
              "2-Tres paneles siguiendo configuración del RCO\n"
              "3-Cinco paneles siguiendo configuración del RCO\n"
              "4-Salir\n")

        try:
            op = int(input("Opcion elegida: "))
        except:
            op == 0

        if(op == 1):
            Menu1Panel(latitude,longitude,Tilt)
        elif(op == 2):
            Menu3Panel(latitude,longitude,Tilt)
        elif (op == 3):
            Menu5Panel(latitude, longitude, Tilt)
        elif (op == 4):
            break
        else:
            break


    return 0

def Menu():

    """Se escribe el menu del programa"""

    "Variable para realizar las pruebas"

    correct = False
    accept = False

    print("\n================================================\n"
          "Cálculo de la irradiacion solar en un sector \n"
          "================================================\n"
          "\n------------------------------------------------\n"
          " Primeramente se deben ingresar algunos datos: "
          "\n------------------------------------------------\n"
          "\n 1-Definir Ubicación \n"
          "\n"
          )
    while(accept == False):
        while(correct == False):
            try:
                longitude = float(input("Longitud: "))
                latitude = float(input("Latitud: "))
                correct = True
            except:
                print("Se debe ingresar la Longitud y Latitud como un numero y utilizar \" . \" para separar los decimales.")

        print("Usted ha ingresado la longitud:",longitude, "y latitud:", latitude)
        correct = False
        while (correct == False):
            a = input("Es esto correcto (Y/N): ")
            if(a.upper() == "Y"):
                correct = True
                accept = True
            elif(a.upper() == "N"):
                correct = True
            else:
                print("Por favor responder unicamente utilizando \"Y\" para si y \"N\" para no")
        correct = False

    correct =  False

    print("\n 2-Definir Zona Horaria UTC \n "
          "\n Nota: En caso de tenerlo incluir el negativo \n")
    while(correct == False):
        try:
            Tilt = float(input("Definir inclinación hacia el sur del panel: "))
            correct = True
        except:
            print("La inclinación debe ser un numero incluido el negativo de ser nescesario")

    correct = False


    accept = False

    while(accept == False):

        print("\n================================================\n"
              "Menu Principal \n"
              "================================================\n")

        print("\n------------------------------------------------\n"
              "Seleccione la accion que desea realizar"
              "\n------------------------------------------------\n \n"
              "1-Grafica de irradiacion durante un dia especifico\n"
              "2-Grafica de irradiacion para el año\n"
              "3-Menú para paneles inclinados \n"
              "4-Ingresar nueva ubicacion\n"
              "5-Salir\n")

        try:
            op = int(input("Opcion elegida: "))
        except:
            op == 0
        if(op == 1):

            """Grafica de radiacion durante un dia especifico"""

            print("\n================================================\n"
                  "Grafica de irradiacion durante un dia especifico \n"
                  "================================================\n")

            print("\n------------------------------------------------\n"
                  " Primeramente se deben ingresar algunos datos: "
                  "\n------------------------------------------------\n")

            #Limpia el archivo json de la nasa
            try:
                os.remove(ROOT_DIR+ "/NasaData/DataSet.json")
                print("")
            except:
                print("")

            #Revisa que los meses y dias esten bien

            try:
                month = int(input("Ingrese el mes:"))
                day = int(input("Ingrese el dia:"))
                if(month > 12 or month < 0):
                    #Genera un error voluntariamente para saltar al except
                    int("Papas")
            except:
                print("Debe ingresar el mes y dia en formato numerico")
            #DayCount se utiliza para comprobar que le dia este bien
            daycount = GetDay(month,day)
            if(daycount != 0):
                RDDE(latitude, longitude, day,month,[Tilt] ,tz = 'America/Costa_Rica',angle = [0])
            if(daycount == 0):
                print("El dia no es valido, este programa no toma en cuenta el 29 de febrero.")
        elif(op == 2):

            """Grafica de radiacion para el año"""

            print("\n================================================\n"
                  "Grafica de irradiacion para el año \n"
                  "================================================\n")

            RA(latitude, longitude, [Tilt] ,tz = 'America/Costa_Rica',angle = [0])

        elif (op == 3):

            MenuPaneles(latitude,longitude,Tilt)
            accept = True

        elif (op == 4):

            Menu()
            accept = True

        elif(op == 5):

            """Salir"""

            accept = True
        else:
            print("Se debe seleccionar una opcion utilizando un numero del 1 al 4")

Menu()