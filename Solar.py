#!/usr/bin/python3
#! -*- coding:utf-8 -*-
import datetime
from pandas.core.frame import DataFrame
from pvlib import location
from pvlib import irradiance
from pvlib import solarposition
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np


tz = 'America/Costa_Rica'
lat, lon = 9.863970, -83.912914


site = location.Location(lat, lon, tz=tz)

def get_location(lat, lon, tz):
    site = location.Location(lat,lon,tz=tz)
    return site


# Calculate clear-sky GHI and transpose to plane of array
# Define a function so that we can re-use the sequence of operations with
# different locations

def get_irradiance(site_location, date, tilt, surface_azimuth):

    #obtengo el angulo Azimuth
    azimuth = solarposition.solar_zenith_analytical(site_location.latitude,solarposition.hour_angle(date,site_location.longitude,solarposition.equation_of_time_pvcdrom()),solarposition.declination_spencer71(date))
    print(azimuth)
    print(tilt,surface_azimuth)
    # Creates one day's worth of 10 min intervals
    times = pd.date_range(date, freq='10min', periods=6*24,
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
    irr = pd.DataFrame({'POA': POA_irradiance['poa_global']})
    for f in (irr['POA'].to_string()).split('\n'):
        s = str(f).split(' ')
        print(s)
    return irr


timer = pd.date_range('2020-01-01','2020-01-01').strftime("%m-%d-%y") 
Irr=[]
for i in timer:
    print(i)
    irradiancia=get_irradiance(site, i , 10, 90)
    Irr.append(irradiancia)
for i in Irr:
    i.index = i.index.strftime("%y%m%d %H%M")
npIrr=np.array(Irr)
###############preparacion de dato para el plot, se puede convertir en una funcion para mejor control
z=[]
for i in Irr:
    #print(i['GHI'].to_string())
    for f in (i['POA'].to_string()).split('\n'):
        s = str(f).split(' ')
        z.append([s[0],s[1], s[-1]])
z=np.array(z)

horas=[float(k) for k in z.T[0].tolist()]
fechas=[float(m) for m in z.T[1].tolist()]
datos=[float(i) for i in z.T[2].tolist()]
#print(datos)
#df = DataFrame (z,columns=[ 'fechas' , 'horas' , 'datos' ])
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
x =horas
y =fechas
z =datos
ax.scatter(x, y, z, c='r', marker='o')
ax.set_xlabel('Días')
ax.set_ylabel('Horas')
ax.set_zlabel('Irradiancia')
plt.show()

