import numpy as np
#trigonometry
x = np.array([10,20,30,40])
tan_value = np.tan(x)

cos_value = np.cos(x)

sin_value = np.sin(x)

#by default sin,cos, tan takes values in radian

#we can convert the values rad to deg and deg to rad
deg_con = np.rad2deg(x)
#for deg to rad use np.deg2rad

#log 
x = np.array([10,20,30,40])

log_base_10 = np.log10(x)

log_base_2 = np.log2(x)


#sqrt function
sqrt = np.sqrt(x)

#cumulative sum
s = np.cumulative_sum(x)
