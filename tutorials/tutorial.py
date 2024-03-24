# Adapted from: https://rosettacode.org/wiki/Levenshtein_distance#Python
#
# Find the greatest common divisor (GCD) of two integers. Greatest common 
# divisor is also known as greatest common factor (gcf) and greatest 
# common measure. 
#
# @param u finite integer
# @param v finite integer
# @returns greatest common divisor of u, v
def gcd(u:int, v:int):
    return gcd(v, u % v) if v else abs(u)
