# prime numbers using filter.
lst = (range(2500))

def isPrime(p):
    num1 = p
    b1 = True
    if p == 1:
        return 1
    elif p == 2:
        return 1
    else:
        for i in range(2, p):
            if p % i == 0:
                b1 = False
                break
    if b1:
        return p

lst2 = filter(isPrime,lst)
lst2 = list(lst2)
print(lst2)

#capitalize each word in a string in a list using lambda and map.
import string
a = ["hello everyone this is day 5 assignment","we have to solve 3 questions in it","and we also have to submit it."]
function1 = lambda a1 : string.capwords(a1)
a = map(function1,a)
a=list(a)
print(a)

# program for sublist in a list

def checklist():
    get = list(map(int,input().split(" ")))
    l=[1,1,5]
    g=[]
    count = 0
    for i in range(len(get)):
        if len(g)==3:
            break
        elif get[i] is 1 or get[i] is 5:
            if count <2 and get[i] is 1:
                g.append(get[i])
                count+=1
            elif count ==2:
                g.append(get[i])
    if g == 1:
        return True
    else:
        return False

print(checklist())
