from FWI import *
'''BUI(dmc,dc)
FWI(ISI,BUI)'''
ffmc=int(FFMC(26.57,91,9.648,0,85))
dmc=int(DMC(26.57,91,0,6,13,11))
dc=int(DC(26.57,0,15,13,11))
bui=int(BUI(dmc,dc))
isi=int(ISI(9.648,81))
fwi=int(FWI(isi,bui))
print("BUI :",bui)
print("FFMC :",ffmc)
print("ISI:",isi)
print("FWI:",fwi)

