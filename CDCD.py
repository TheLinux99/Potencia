#r# This example depicts half and full wave rectification.

####################################################################################################

import matplotlib.pyplot as plt
import numpy as np

####################################################################################################

import PySpice.Logging.Logging as Logging
logger = Logging.setup_logging()

####################################################################################################

from PySpice.Doc.ExampleTools import find_libraries
from PySpice.Probe.Plot import plot
from PySpice.Spice.Library import SpiceLibrary
from PySpice.Spice.Netlist import Circuit
from PySpice.Unit import *

####################################################################################################

libraries_path = find_libraries()
print(libraries_path)
spice_library = SpiceLibrary(libraries_path)


####################################################################################################


def GetOutput(current, resistance):

	I = current
	circuit = Circuit('DCDC')

	circuit.include(spice_library['szmm3z5v6st1g'])

	circuit.I(1,circuit.gnd,'inp', current@u_mA)
	circuit.X('Z','szmm3z5v6st1g',circuit.gnd,'inp')
	circuit.L(1,'inp','out',37.52@u_mH)
	circuit.C(1,'out',circuit.gnd,0.1875@u_mF)
	circuit.R(1,'out',circuit.gnd,resistance@u_Ω)


	simulator = circuit.simulator(temperature=25, nominal_temperature=25)
	analysis = simulator.operating_point()

	#print(circuit)
	
	for node in analysis.nodes.values():
		#print(str(node))
		#print(float(node))
		#print("Current:",float(node)/resistance)
		#print("Potencia: ",(float(node)**2)/resistance)
		if(str(node) == "out"):
			voltage = float(node)
			current = (float(node)**2)/resistance
	#print("Voltage = ", voltage, "Current = ", current)
	return voltage, current

def Supercapacitor(voltage):

	V = voltage
	circuit = Circuit('Super')

	circuit.V(1,'inp',circuit.gnd, voltage@u_V)
	circuit.C(1,'inp',circuit.gnd,25@u_F)
	circuit.R(1, 'inp', circuit.gnd, 150@u_Ω)
	simulator = circuit.simulator(temperature=25, nominal_temperature=25)
	analysis = simulator.operating_point()
	ocurrent = 0
	ovoltage = 0
	#print(circuit)
	
	for node in analysis.nodes.values():
		#print(str(node))
		#print(float(node))
		#print("Current:",float(node)/resistance)
		#print("Potencia: ",(float(node)**2)/resistance)
		if(str(node) == "inp"):
			ovoltage = float(node)
			ocurrent = (float(node)**2)/150
	#print("Voltage = ", voltage, "Current = ", current)
	return ovoltage, ocurrent

#print("\n Array de Voltaje y Corriente \n", GetOutput(30,150))
