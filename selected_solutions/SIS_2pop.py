import matplotlib.pyplot as plt
alpha_m= 6e-6
alpha_f = 9e-7
gamma_f, gamma_m = 0.007, 0.05
Sf, Sm = 9000, 14000
If, Im = 1000, 1000
Sf_hist, If_hist, Sm_hist, Im_hist = [], [], [], []
for day in range(4000):
    Sf_hist.append(Sf)
    If_hist.append(If)
    Sm_hist.append(Sm)
    Im_hist.append(Im)
    delta_Sf=(-alpha_f*Sf*Im)+gamma_f*If
    delta_If=-delta_Sf
    delta_Sm=(-alpha_m*Sm*If)+gamma_m*Im
    delta_Im=-delta_Sm
    Sf+=delta_Sf
    If+=delta_If
    Sm+=delta_Sm
    Im+=delta_Im
    Sm, Im, Sf, If = max(Sm,0), max(Im,0), max(Sf,0), max(If,0)
#Plot S,I vs day
#print(Im)
plt.plot(Im_hist)
plt.plot(If_hist,color='red')
plt.show()
