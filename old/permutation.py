"""
Permutation in String Problem
Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.

In other words, return true if one of s1's permutations is the substring of s2.

    Example Inputs and Outputs
    Example 1
    Input: s1 = "ab", s2 = "eidbaooo"
    Output: True

    Example 2
    Input: s1 = "ab", s2 = "eidboaoo"
    Output: False
"""

from collections import Counter

def perm(s1, s2):
    n = len(s1)
    s1_map = Counter(s1)
    for i in range(len(s2)):
        if s1_map == Counter(s2[i:n+i]):
          return True
    return False  

print(perm("ab","eidboaoo"))

