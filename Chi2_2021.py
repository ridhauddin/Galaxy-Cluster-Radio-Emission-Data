from __future__ import division
from numpy import array, var
from lmfit import Model

import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np


#######Observed data A4038############
#xd = array([0.029,0.074,0.15,0.24,0.327,0.408,0.606,0.843,1.4])
#yd = array([32,12.45,5.16,2.96,1.44,0.91,0.38,0.17,0.06])
#y_err = array([7,1.5,0.11,0.06,0.15,0.11,0.057,0.03,0.004])

#######Observed data A1664############
xd = array([0.15,0.325,1.4])
yd = array([1.25,0.45,0.106])
y_err = array([0.125,0.03,0.04])



#########insitu model###########
def insitu(x,scr0,a,vs):
    return scr0*(xd)**(-a)*np.exp(-xd**(0.5)/vs**(0.5))

mod =Model(insitu)
params = mod.make_params(scr0=1, a=1, vs=1)
#params['scr0'].max = 23.5
#params['scr0'].min = 0.01
#params['a'].max = 1.0
#params['a'].min = 0.35
params['vs'].max = 10.5
params['vs'].min = 0.01
result1 = mod.fit(yd, params, x=xd, method='leastsq',weights=1+(y_err/yd))
rsq1 = 1 - result1.residual.var() / var(yd)
print(result1.fit_report())
print (rsq1)
#redchisqrt=result.redchi

##############primary model#############
#def primary(x,scr0,a,vs,g):
#    return scr0*(xd)**(-a)*((1+vs**g)/(1+(xd/vs)**g))

#mod1 =Model(primary)
#result2 = mod1.fit(yd, x=xd, scr0=17, a=0.39, vs=0.043, g=1, method='leastsq', weights=1+(y_err/yd))
#rsq2 = 1 - result2.residual.var() / var(yd)
#print(result2.fit_report())
#print (rsq2)
#redchisqrt=result.redchi

##############secondary model#############
#def secondary(x,scr0,vs,a):
#    return scr0*(xd/vs)**(-a)

#mod2 =Model(secondary)
#result3 = mod2.fit(yd, x=xd, scr0=17, a=0.39,vs=0.043, method='leastsq', weights=1+(y_err/yd))
#rsq3 = 1 - result3.residual.var() / var(yd)
#print(result3.fit_report())
#print (rsq3)
#redchisqrt=result.redchi

#############save

#########plotting##########
plt.scatter(xd, yd)#, label='Observed Radio Flux')
plt.errorbar(xd, yd,y_err,fmt='o',color='black', ecolor='gray', lw=2)
plt.plot(xd, result1.best_fit, 'r-')#, label='Insitu model')
#plt.plot(xd, result2.best_fit, 'g--', label='Primary model')
#plt.plot(xd, result3.best_fit, 'b--', label='Secondary model')

#print(result1.best_fit,result2.best_fit,result3.best_fit)


# turn to log
plt.xscale('log')
plt.yscale('log')
plt.xlabel("Frequency (Ghz)")
plt.ylabel("Radio relic emission (jy)")
plt.legend()
plt.show()
