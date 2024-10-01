# ecef_to_sez.py
#
# Usage: python3 ecef_to_sez.py o_x_km o_y_km o_z_km x_km y_km z_km
#  Text explaining script usage
# Parameters:
#  o_x_km: x coordinate of ECEF vector to the origin of the SEZ frame
#  o_y_km: y coordinate of ECEF vector to the origin of the SEZ frame
#  o_z_km: z coordinate of ECEF vector to the origin of the SEZ frame
#  x_km: x coordinate in ECEF
#  y_km: y coordinate in ECEF
#  z_km: z coordinate in ECEF
#  
# Output:
#  s_km: south coordinate in SEZ frame
#  e_km: east coordinate in SEZ frame
#  z_km: zenith coordinate in SEZ frame
#  
# Written by Lee Wallenfang
# Other contributors: None

# import Python modules
import math # math module
import sys # argv
import numpy
# "constants"
R_E_KM = 6378.137

# helper functions

## function description
def ECEF_to_SEZ(lat,lon):
   return [[-1*math.sin(lat)*math.sin(lon) , -1*math.sin(lon)  , math.cos(lat)*math.cos(lon)],
           [-1*math.sin(lat)*math.sin(lon) , math.cos(lon) , math.cos(lat)*math.sin(lon)],
           [math.cos(lat) , 0 , math.sin(lat)]]

# initialize script arguments
o_x_km = '' # ECEF origin of the SEZ frame
o_y_km = '' # ECEF origin of the SEZ frame
o_z_km = '' # ECEF origin of the SEZ frame
x_km = '' # x coordinate in ECEF
y_km = '' # y coordinate in ECEF
z_km = '' # z coordinate in ECEF

# parse script arguments
if len(sys.argv)==7:
   o_x_km = float(sys.argv[1])
   o_y_km = float(sys.argv[2])
   o_z_km = float(sys.argv[3])
   x_km = float(sys.argv[4])
   y_km = float(sys.argv[5])
   z_km = float(sys.argv[6])
else:
   print(\
    'Usage: '\
    'python3 ecef_to_sez.py o_x_km o_y_km o_z_km x_km y_km z_km'\
   )
   exit()

lon = math.atan2(o_y_km,o_x_km)
lat = math.atan2(o_z_km,math.sqrt(o_x_km**2+o_y_km**2))
r_x_rel = x_km - o_x_km
r_y_rel = y_km - o_y_km
r_z_rel = z_km - o_z_km
r_rel = [r_x_rel,r_y_rel,r_z_rel]

[s_km,e_km,z_km] = numpy.matmul(ECEF_to_SEZ(lat,lon),r_rel)
print(s_km)
print(e_km)
print(z_km)