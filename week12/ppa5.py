def balanced(word):
    """
    Determine if a string is balanced
    Argument:
        word: string
    Return:
        result: bool
    """
    stack = []
    brackets_map = {'}':'{',']':'[',')':'('}
    for c in word:
        if c in '{[(':
            stack.append(c)
        if c in '}])' and (len(stack) == 0 or stack.pop() != brackets_map[c]):
            return False
    return True
print(balanced('()(())'))