# WAP TO CHECK NUMBER IS PALLINDORME OR NOT RETURN TRUE IF PALLINDORME AND RETURN FALSE IF NOT PALLINORME

def pallindrome(num):
    temp=num
    rev=0
    while(temp>0):
        d=temp%10
        temp=temp//10

        rev=rev*10+d
    if(num==rev):
        return True
    else:
        return False


# n=121
n=int(input("enter number:"))
print(pallindrome(n))


