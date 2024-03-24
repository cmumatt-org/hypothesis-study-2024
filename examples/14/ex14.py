# Adapted from: https://rosettacode.org/wiki/Modular_inverse#Python
#
# The modular multiplicative inverse of an integer `a` modulo `m` is an
# integer 'x' such that:
#   `a x ≡ 1 ( mod m )`
# In other words, the remainder after dividing `ax` by the integer `m` is 1
#
# @param a finite integer > 0
# @param m finite integer > 0 (modulus)
# @returns a finite integer such that ax % m = 1
def modinv(a, m):
	g, x, y = extended_gcd(a, m)
	if g != 1:
		raise ValueError
	return x % m

def extended_gcd(a, b):
    lastremainder, remainder = abs(a), abs(b)
    x, lastx, y, lasty = 0, 1, 1, 0
    while remainder:
        lastremainder, (quotient, remainder) = remainder, divmod(lastremainder, remainder)
        x, lastx = lastx - quotient*x, x
        y, lasty = lasty - quotient*y, y
    return lastremainder, lastx * (-1 if a < 0 else 1), lasty * (-1 if b < 0 else 1)

# Post-Task Activity
# ------------------
# Please review the inputs you found, if any, where the program behaves 
# contrary to its specification.
#        
# 1. List the generalized inputs where the program behaves contrary
#    to its specification. If you found multiple inputs:
#     - Make as many entries as you need
#     - Feel free to use ranges if that's easier (e.g., a>=0)
#    If you found no inputs (the program is correct), indicate "none."
#    You do not need to explain any further.
# 
#   Input(s): 
# 
# 2. Please X the box that describes how confident you are that you 
#    accurately found all the inputs where the program behaves contrary
#    to its specification.
# 
#       1             2             3             4             5 
#   Not at all     Slightly      Somewhat      Moderately    Extremely
#   Confident      Confident     Confident     Confident     Confident
# |------------|--------------|-------------|-------------|-------------|
# |            |              |             |             |             |
# |------------|--------------|-------------|-------------|-------------|
# 
# 3. Please save this file, commit to the repo, and request the next task.