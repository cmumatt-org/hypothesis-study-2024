# Adapted from: https://rosettacode.org/wiki/Levenshtein_distance#Python
#
# The Levenshtein distance is a metric for measuring the amount of difference
# between two sequences (i.e. an edit distance). The Levenshtein distance
# between two strings (`a` and `b`) is defined as the minimum number of edits
# needed to transform one string into the other, with the allowable edit
# operations being insertion, deletion, or substitution -- all of a single 
# character.
#
# @param str1 the original string
# @param str2 the final string after editing `str1`
# @returns the number of edits needed to transform `str1` to `str2`
def levenshteinDistance(str1, str2):
    m = len(str1)
    n = len(str2)
    d = [[i] for i in range(1, m + 1)]   # d matrix rows
    d.insert(0, list(range(0, n + 1)))   # d matrix columns
    for j in range(1, n + 1):
        for i in range(1, m + 1):
            if str1[i - 1] == str2[j - 1]:   # Python (string) is 0-based
                substitutionCost = 0
            else:
                substitutionCost = 1
            d[i].insert(j, min(d[i - 1][j],
                               d[i][j - 1] + 1,
                               d[i - 1][j - 1] + substitutionCost))
    return d[-1][-1]

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