"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
"""

def valid_parenthesis(s):
    """
    :type s: str
    :rtype: bool
    """
    stack = []
    op = "({["
    close = ")}]"
    for el in s:
        if el in op:
            stack.append(el)
        else:
            if(len(stack) > 0):  
                rem = stack.pop()
                if op.index(rem) != close.index(el):
                    return False
            else:
                return False
    return True if len(stack) == 0 else False