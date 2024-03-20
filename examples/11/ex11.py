# Adapted from: https://rosettacode.org/wiki/Identity_matrix#Python
#
# This function returns an identity matrix of n x n size such that:
#   n = 1 => [1],
#   n = 2 => [[1,0],[0,1],
#   n = 3 => [[1,0,0],[0,1,0],[0,0,1]],
#   ... and so on ...
#
# @param n finite integer 1..n dimensions of identiy matrix to return
# @returns number[n][n] identity matrix of n x n size
def identity(size):
    matrix = [[0] * size] * size 

    if size == 1:
        return [1]
    
    for i in range(size):
        matrix[i][i] = 1

    return matrix

# Post-Task Activity
# ------------------
# Please review the test cases you saved where the program behaves
# contrary to its specification.
#        
# 1. List the generalized input values where the program behaves contrary
#    to its specification. If you found multiple inputs:
#     - Make as many entries as you need
#     - Feel free to use ranges if that's easier(e.g., when a>=0)
#     - If you found no inputs, indicate "none".
#     - You do not need to explain further.
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