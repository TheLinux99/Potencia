import PySpice.Logging.Logging as Logging
logger = Logging.setup_logging()

from PySpice.Doc.ExampleTools import find_libraries
from PySpice.Probe.Plot import plot
from PySpice.Spice.Library import SpiceLibrary
from PySpice.Spice.Netlist import Circuit,SubCircuit,SubCircuitFactory
from PySpice.Unit import *

class DCDC(SubCircuitFactory):
    __name__ = 'DCDC'
    __nodes__ = ('','','')