import math
import wget
import json
import os
from pvlib import location
from pvlib import irradiance
from pvlib import solarposition
import pandas as pd
import numpy as np
from CDCD import *

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

"""Obtener el numero de dia suministrando la fecha"""

def GetDay(month, day):
    year = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29,
           30, 31],
            [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28],
            [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29,
           30, 31],
            [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29,
           30],
            [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29,
           30, 31],
            [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29,
           30],
            [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29,
           30, 31],
            [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29,
           30, 31],
            [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29,
           30],
            [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29,
           30, 31],
            [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29,
           30],
            [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29,
           30, 31]]

    cont = 0;
    daycont = 0;

    while(cont < month-1):
        daycont += len(year[cont-1])
        cont += 1
    daycont += day

    if(day < 0 or day > year[month-1][-1]):
        daycont = 0

    return daycont

def get_location(lat, lon, tz):
    site = location.Location(lat,lon,tz=tz)
    return site

def get_irradiance(site_location, date, surface_azimuth, tilt,month,day,tz):
    tim = pd.DatetimeIndex(date,'60min',tz)
    azimuth = solarposition.solar_zenith_analytical(site_location.latitude,solarposition.hour_angle(tim, site_location.longitude,solarposition.equation_of_time_pvcdrom(GetDay(month,day))),solarposition.declination_spencer71(GetDay(month,day)))
    print(math.degrees(azimuth))
    print(tilt)
    surface_azimuth = math.degrees(azimuth) + surface_azimuth
    # Creates one day's worth of 10 min intervals
    times = pd.date_range(date[0], freq='60min', periods=24,
                          tz=site_location.tz)
    # Generate clearsky data using the Ineichen model, which is the default
    # The get_clearsky method returns a dataframe with values for GHI, DNI,
    # and DHI
    clearsky = site_location.get_clearsky(times)
    # Get solar azimuth and zenith to pass to the transposition function
    solar_position = site_location.get_solarposition(times=times)
    # Use the get_total_irradiance function to transpose the GHI to POA
    POA_irradiance = irradiance.get_total_irradiance(
        surface_tilt=tilt,
        surface_azimuth=surface_azimuth,
        dni=clearsky['dni'],
        ghi=clearsky['ghi'],
        dhi=clearsky['dhi'],
        solar_zenith=solar_position['apparent_zenith'],
        solar_azimuth=solar_position['azimuth'])
    return pd.DataFrame({'POA': POA_irradiance['poa_global']})

"""Direct Radiation Value"""

def radiation(latitude, longitude, month, day, tilt,angle = 0,tz = 'America/Costa_Rica'):
    if(month < 10):
        if(day < 10):
            timer = pd.date_range('2020-0'+ str(month) + '-0' + str(day), '2020-0'+ str(month) + '-0' + str(day)).strftime("%m-%d-%y")
        else:
            timer = pd.date_range('2020-0' + str(month) + '-' + str(day),'2020-0' + str(month) + '-' + str(day)).strftime("%m-%d-%y")
    else:
        timer = pd.date_range('2020-' + str(month) + '-' + str(day), '2020-' + str(month) + '-' + str(day)).strftime("%m-%d-%y")
    irr = get_irradiance(get_location(latitude, longitude, tz), timer,tilt,angle,month,day,tz)
    irrT = []
    for f in (irr['POA'].to_string()).split('\n'):
        s = str(f).split(' ')
        cont2 = 0
        for k in s:
            if(cont2 > 1):
                if(k != ''):
                    irrT.append(float(k)*pow((1/1000),2)*1470*1000)
            cont2 += 1
    print("Irradiacion: ", irrT)
    return irrT


def CombineData(latitude, longitude, month, day,tilt,tz, Angles = [0]):
    cont = 0
    TotalPower = []
    irr = []

    v = 0
    i = 0
    vdata = []
    idata = []
    while(cont < 5):
        if(cont < len(Angles)):
            voltages = []
            currents = []
            irr.append(radiation(latitude,longitude,month,day,tilt[cont],Angles[cont],tz))
            for i in irr[0]:
            	current = i/5.3
            	if(current > 42.9):
            		current = 42.9
            	v,i = GetOutput(current, 150)
            	v,i = Supercapacitor(v)
            	voltages.append(v)
            	currents.append(i)
            vdata.append(voltages)
            idata.append(currents)
        else:
            irr.append([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
            vdata.append([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
            idata.append([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
        cont += 1
    irr0 = np.array([irr[0], irr[1], irr[2], irr[3], irr[4]])
    vdata0 = np.array([vdata[0],vdata[1],vdata[2],vdata[3],vdata[4]])
    idata0 = np.array([idata[0],idata[1],idata[2],idata[3],idata[4]])
    TotalPower = np.sum(irr0,axis = 0)
    TotalVoltage = np.sum(vdata0,axis = 0)
    TotalCurrent = np.sum(idata0,axis = 0)
    return TotalPower, TotalVoltage, TotalCurrent


"""Obtener Data Irradiation de la Nasa"""

def GetNasaData(latitude, longitude, month, day):

    print("Obteniendo data de la Nasa")

    url = "https://power.larc.nasa.gov/api/temporal/hourly/point?		Time=LST&parameters=ALLSKY_SFC_UVA,ALLSKY_SFC_UVB,SZA,ALLSKY_KT,ALLSKY_SFC_SW_DWN,CLRSKY_SFC_SW_DWN&community=RE&longitude=" + str(longitude) + "&latitude="+ str(latitude) + "&start=2018" + str(month) + str(day) + "&end=2018" + str(month) + str(day) + "&format=JSON"

    print(url)

    wget.download(url, ROOT_DIR + "/NasaData/DataSet.json")

    print("Datos Obtenidos")

"""Obtener datos del Json descargado"""

def GetJsonArray(parameter):

    print("Leyendo datos del Json")

    array = []

    f = open(ROOT_DIR + "/NasaData/DataSet.json")
    data = json.loads(f.read())

    data = data['properties']
    data = data['parameter']
    data = data['ALLSKY_SFC_UVA']

    for i in data:
        array.append(data[i])

    f.close()

    return array
