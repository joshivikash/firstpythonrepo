max_depth = 0
original_exp = ''
def depth(exp):
    """
    Compute the maximum nesting depth
    
    Argument:
        exp: string
    Return:
        result: integer
    """
    global max_depth
    global original_exp
    if len(exp) == 0:
        return 0
    if exp[0] == '(':
        if not original_exp:
            original_exp = exp 
        closing_brackets = abs(depth(exp[1:len(exp)]))
        if not max_depth:
            max_depth = closing_brackets
        elif closing_brackets > max_depth:
            max_depth = abs(closing_brackets)
        if exp == original_exp:
            return max_depth
        return 1 + (-closing_brackets)
    if exp[0] == ')':
        return -1 + depth(exp[1:len(exp)])
    
print(depth('(())(((())))'))