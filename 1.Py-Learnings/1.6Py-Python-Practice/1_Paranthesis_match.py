def inValid(s):
    inp = []
    lookup = {")":"(","]":"["}

    for i in s:
        if i in lookup:
            if inp and inp[-1] == lookup[i]:
                inp.pop()
            else:
                return False
        else:
            inp.append(i)
    return not inp

print(inValid(")"))

