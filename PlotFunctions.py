from Functions import *
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator

year = [[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31],
        [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29],
        [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31],
        [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,30],
        [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31],
        [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,30],
        [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31],
        [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31],
        [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,30],
        [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31],
        [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,30],
        [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31]]

"""radiacion durante un dia especifico"""


def RDDE(latitude, longitude, day,month, tilt = [10],tz = 'America/Costa_Rica',angle = [0]):

    #Obtener los datos de radiacion solicitados
    data = []
    days = []

    #Se obtienen los datos de irradiancia para le año
    cont = 1
    hours = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24]
    r = CombineData(latitude, longitude, month, day,tilt,tz, angle)
    medianData = []
    #Realizar el grafico

    #Eliminar 0s para no afectar la media

    cont = 0
    while(cont < len(r)):
        if(r[cont] != 0):
            medianData.append(r[cont])
        cont += 1


    print(medianData)

    plt.figure(1)
    datanp = np.array(r)
    daysnp = np.array(hours)
    media = np.median(medianData)

    print("====================================\n")
    print("            MEDIA:" + str(media) + "           \n")
    print("====================================\n")


    plt.plot(daysnp.transpose(),datanp.transpose())
    plt.title("Grafico Estimado")
    plt.xlabel("Hora")
    plt.ylabel("Irradiancia")

    """
    #Comparar con datos de la Nasa

    GetNasaData(latitude, longitude, month, day)

    nasaData = GetJsonArray('ALLSKY_SFC_UVA')

    print(nasaData)

    #procesando datos de la Nasa

    nData = []
    nHours = []

    cont = 0
    for x in nasaData:
        if(x != 0):
            nHours.append(cont)
            nData.append(x)
        cont += 1

    nDatanp = np.array(nData)
    nHoursnp = np.array(nHours)

    #Realizar el grafico con datos de la nasa

    print("Imprimiendo grafico 2")

    plt.figure(2)

    plt.plot(nHoursnp,nDatanp)
    plt.title("Grafico de la Nasa")
    plt.xlabel("Hora")
    plt.ylabel("Irradiancia")

    print("Imprimiendo grafico 3")

    plt.figure(3)

    plt.plot(nHoursnp, nDatanp, label="Nasa")
    plt.plot(daysnp.transpose(), datanp.transpose(), label="Simulado")
    plt.title("Grafico Comparativo")
    plt.xlabel("Hora")
    plt.ylabel("Irradiancia")
    """

    plt.show()

    return 0


"""radiacion para el año"""


def RA(latitude, longitude,tilt = [10],tz = 'America/Costa_Rica', angle = [90]):

    print(angle)
    #Obtener los datos de radiacion solicitados
    data = []
    days = []

    #Se obtienen los datos de irradiancia para le año
    cont = 1
    day = 0
    hours = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24]
    medianData = []

    print("====================================\n")
    print("       Inicio Toma de Datos         \n")
    print("====================================\n")

    for x in year:
        for y in x:
            day += 1
            r = CombineData(latitude, longitude, cont, y,tilt,tz, angle)
            data.append(r)
            days.append(day)
            cont2 = 0
            while (cont2 < len(r)):
                if (r[cont2] != 0):
                    medianData.append(r[cont2])
                cont2 += 1

        cont += 1

    print("====================================\n")
    print("       Fin Toma de Datos         \n")
    print("====================================\n")

    print("Graficando")
    hoursnp = np.array(hours)
    daysnp = np.array(days)
    datanp = np.array(data)
    media = np.median(medianData)

    print("====================================\n")
    print("            MEDIA:" + str(media) + "           \n")
    print("====================================\n")

    #Se preparan los datos para el grafico 3D

    X, Y = np.meshgrid(hoursnp, daysnp)
    Z = datanp.reshape(X.shape)

    #Se realiza la grafica

    fig = plt.figure()
    RAplot = fig.add_subplot(111, projection='3d')
    RAplot.plot_surface(X,Y,Z,cmap=cm.coolwarm,
                       linewidth=0, antialiased=False)
    RAplot.set_xlabel("Horas")
    RAplot.set_ylabel("Dias")
    RAplot.set_zlabel("irradiacion")
    plt.show()


    return 0
