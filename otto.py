


import math
import matplotlib.pyplot as plt

def engine_kinem(bore, stroke, con_rod, compres_rat, crank_start, crank_end):
	a = stroke/2 #crank radius
	R=con_rod/a
	v_swept = math.pi*(1/4)*pow(bore,2)*stroke
	v_clear = v_swept/(compres_rat-1)
	sc = math.radians(crank_start)
	ec = math.radians(crank_end)
	num_values = 60
	dtheta = (ec-sc)/(num_values-1)
	V=[]
	for i in range(0,num_values):
		theta = sc+i*dtheta
		term1 = 0.5*(compres_rat-1)
		term2 = R+1-math.cos(theta)
		term3 = pow(R,2)-pow(math.sin(theta),2)
		term3=pow(term3,0.5)
		V.append((1+term1*(term2-term3))*v_clear)
	return V
		
    

# Inputs
p1=101325 #Pa
t1=500 #kelvin
gamma=1.4  
t3=2300
bore=0.1 #cm
stroke = 0.1 #cm
con_rod = 0.15 #cm
compres_rat = 8
# Volume computation
v_swept = (math.pi/4)*pow(bore,2)*stroke
v_clear = v_swept/(compres_rat-1)
v1 = v_swept+v_clear
 # state point 2
v2= v_clear
p2=p1*pow(v1,gamma)/pow(v2,gamma)
rhs = p1*v1/t1
t2=p2*v2/rhs
V_compression=engine_kinem(bore,stroke,con_rod,compres_rat,180,0)
constant = p1*pow(v1,gamma)
P_compression = []
for v in V_compression:
	P_compression.append(constant/pow(v,gamma))

# state point 3
v3=v2
rhs = p2*v2/t2
p3=rhs*t3/v3
V_expansion=engine_kinem(bore,stroke,con_rod,compres_rat,0,180)
constant = p3*pow(v3,gamma)
P_expansion = []
for v in V_expansion:
	P_expansion.append(constant/pow(v,gamma))
effiiency = (1-(1/pow(compres_rat,gamma-1)))*100
print(effiiency)

# state point 4
v4=v1
p4=p3*pow(v3,gamma)/pow(v4,gamma)
t4=p4*v4/rhs

plt.plot([v2,v3],[p2,p3])
plt.plot(V_compression,P_compression)
plt.plot(V_expansion,P_expansion)
plt.plot([v4,v1],[p4,p1])
plt.show()