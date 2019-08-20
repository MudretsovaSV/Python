import DzModuliFarengeit

celsius=float(raw_input("Vvedite temperaturu v gradusah celsia: "))
from DzModuliFarengeit import c_to_f
fahrengeit=c_to_f(celsius)
print "Eto", fahrengeit, "gradusov farengeita"

