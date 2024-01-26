vorudi = str(input())
code = vorudi.split(" ")
code.sort(key = lambda x: int(x[1:]))
for i in code:
    print (i[0],end="")

