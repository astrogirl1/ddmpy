import math
import natpy as nat


years = 55 * nat.yr
gyr = nat.convert(years, nat.Gyr)
print(gyr)

sec = nat.convert(gyr, nat.s)
print(sec)

km = 1*nat.km
km_over_Mpc = nat.convert(km, nat.Mpc)
print(km_over_Mpc)

gam_in_km_s = (sec**-1)*(km_over_Mpc)*km*nat.Mpc**-2
print(gam_in_km_s)

gam_gev = nat.convert(gyr**-1, nat.GeV)
print(gam_gev)