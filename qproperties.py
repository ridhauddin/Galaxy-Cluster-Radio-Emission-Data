import numpy as np
from scipy import constants
from qconstants import *
import os.path
import pandas as pd

############################## Choose a Cluster from list below ###############################################

cluster='A1664_1'

############################## List of Cluster ##################################################################

d1=pd.DataFrame.from_dict({
'A4038_1'  : ['A4038_1','RH',0.0282 ,131000,42.0,0.029,43,3.11,0.541,1.74,6.6,0.5,1000,158.41,7.7885e-22],
'A4038_2'  : ['A4038_2','RH',0.0282 ,131000,12.6,0.074,43,3.11,0.541,1.74,6.6,0.5,1000,158.41,7.7885e-22],
'A4038_3'  : ['A4038_3','RH',0.0282 ,131000,5.26,0.150,43,3.11,0.541,1.74,6.6,0.5,1000,158.41,7.7885e-22],
'A4038_4'  : ['A4038_4','RH',0.0282 ,131000,3.04,0.240,43,3.11,0.541,1.74,6.6,0.5,1000,158.41,7.7885e-22],
'A4038_5'  : ['A4038_5','RH',0.0282 ,131000,1.54,0.327,43,3.11,0.541,1.74,6.6,0.5,1000,158.41,7.7885e-22],
'A4038_6'  : ['A4038_6','RH',0.0282 ,131000,0.96,0.408,43,3.11,0.541,1.74,6.6,0.5,1000,158.41,7.7885e-22],
'A4038_7'  : ['A4038_7','RH',0.0282 ,131000,0.43,0.606,43,3.11,0.541,1.74,6.6,0.5,1000,158.41,7.7885e-22],
'A4038_8'  : ['A4038_8','RH',0.0282 ,131000,0.21,0.843,43,3.11,0.541,1.74,6.6,0.5,1000,158.41,7.7885e-22],
'A4038_9'  : ['A4038_9','RH',0.0282 ,131000,0.09,1.400,43,3.11,0.541,1.74,6.6,0.5,1000,158.41,7.7885e-22],
'A1664_1'  : ['A1664_1','RH',0.1280 ,626000,1.811,0.15,50,5,0.55,22.8,10,0.5,1030,278.70,4.6228e-22],
'A1664_2'  : ['A1664_2','RH',0.1280 ,626000,0.688,0.325,50,5,0.55,22.8,10,0.5,1030,278.70,4.6228e-22],
'A1664_3'  : ['A1664_3','RH',0.1280 ,626000,0.178,1.4,50,5,0.55,22.8,10,0.5,1030,278.70,4.6228e-22]},
orient='index',columns=['Label','type','redshift','DL','S_nu','Freq','r_c_dum','T_gas_dum','beta','n0','B_dum','eta','r','rs','rhos'])


############################# Set and decide the constants start ##################################################

#Hubble constants
h		=0.7		#little h.		unit :	-

#Critical density:
sigm		=0.3		#matter density.	unit :	-
sigl		=0.7		#dark energy density.	unit :	-
sig8		=0.829

#Properties of cluster:
redshift	=d1.loc[cluster,'redshift']
DL		=d1.loc[cluster,'DL']*kpc*100.0	# luminosity distance, in unit of cm.	z=0.0302
#DA		=100000*kpc*100.0
nuobs		=d1.loc[cluster,'Freq']        #Ghz
S_nu            =d1.loc[cluster,'S_nu']            #mJy
r_c_dum	=h*(d1.loc[cluster,'r_c_dum'])*50**-1*100.0		#Core radius.		unit :	h50^-1 kpc, where H0=50 kms^-1Mpc^-1
T_gas_dum	=d1.loc[cluster,'T_gas_dum']		#T_gas in unit of keV
beta		=d1.loc[cluster,'beta']		#Beta parameter.	unit :	-
n0		=d1.loc[cluster,'n0']		#Thermal electron central density	#unit :	cm^-3. A&A 540, A38 (2012)
B_dum		=d1.loc[cluster,'B_dum']	#central magnetic field.		#unit :	Gauss.  A&A 540, A38 (2012)
eta		=d1.loc[cluster,'eta']		#proportional coefficient related to magnetic field profile

#Temperature of CMB at any redshift z. (want ot know more? See http://www.cv.nrao.edu/course/astr534/CMB.html)
T		=T0*(1.0+redshift)

#conversion if necessary
B0	=B_dum*(10**-6)
H_0	=100.0*h				#hubble constant.	unit :	km s^-1 Mpc^-1
H_0m	=H_0/(1000.0*si_pc)			#hubble constant.	unit :	s^-1
Ez	=np.sqrt(sigm*(1.0+redshift)**3+sigl)
Hz	=H_0m*Ez				#H(z). 			unit :	s^-1
rho_crit=3.0*Hz**2/(8.0*constants.pi*si_G)	#critical density.	unit :	kg m^-3

T_gas	=T_gas_dum*1000.0*si_e/si_k		#T_gas in unit of Kelvin
r_c_dum2=r_c_dum*0.5/h				#Core radius.		unit :	kpc, where h=0.673
r_c	=r_c_dum2*1000.0*si_pc*100.0		#Core radius.		unit :	cm

############################# Particle upper-limit ################################################################
Relic_density_limit =3.0e-26
Calet=3.0e-24
Boudaud=1.0e-24
Ibarra=0.9e-25

############################# Set and decide the constants end ####################################################
############################# start: parameters for nfw profile ####################################################

#characteristic density in unit of kg m^-3 ##donot forget to convert because halodp in msun/kpc3###
rhos= (d1.loc[cluster,'rhos']/h**2)
#characteristic radius in unit of meter
rs= kpc*d1.loc[cluster,'rs']*h
r=d1.loc[cluster,'r']*kpc
############################# end: parameters for nfw profile ####################################################

