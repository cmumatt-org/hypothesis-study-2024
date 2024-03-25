# Adapted from: https://rosettacode.org/wiki/Identity_matrix#Python
#
# This function returns an identity matrix of n x n size such that:
#   n = 1 => [[1]],
#   n = 2 => [[1,0],[0,1],
#   n = 3 => [[1,0,0],[0,1,0],[0,0,1]],
#   ... and so on ...
#
# @param n finite integer >=1
# @returns identity matrix of n x n size
def identity(n):
    matrix = [[0] * n] * n 
    for i in range(n):
        matrix[i][i] = 1

    return matrix

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