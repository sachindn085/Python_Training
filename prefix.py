s= ["door", "done", "dog"]
def comman_brackets(str):
    if not str:
        return ""
    
    # Sort the list of strings
    str.sort()
    
    # The longest common prefix will be between the first and the last string
    first = str[0]
    last = str[-1]
    i = 0
    
    # Compare characters until they differ
    while    first[i] == last[i]:
        i += 1
    
    return first[:i]
print(comman_brackets(s)) 