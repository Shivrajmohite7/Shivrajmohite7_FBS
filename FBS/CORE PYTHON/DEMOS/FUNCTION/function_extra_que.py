
# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']'
#  determine if the input string is valid.

def getData(paren):
    slow=[]
    pairs={
        "}":"{",
        ")":"(",
        "]":"["
    }
    for i in paren:
        if i in "{([":
            slow.append(i)
        else:
            if not slow or slow.pop()!=pairs[i]:
                return False
    return len(slow)==0

paren=input("enter:")
result=getData(paren)
print(result)
