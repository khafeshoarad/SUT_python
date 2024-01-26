def toBinary(n): 
    return "{:032b}".format(int(n))
rast = str(toBinary(int(str(input()))))
chap = str(toBinary(int(str(input()))))
dt = str(chap)+str(rast)
ns = []
for _ in range(int(input())):
    ns.append(int(input()))
for n in ns:
    # print(str(n) + ":" + shirzad[len(shirzad) - n - 1])
    if dt[-n-1] == "0":
        print("no")
    else:
        print("yes")

# list=[]
# for i in range(n):
#     m = int(input())
#     if dt[-m-1]=='0':
#         list.append('no')
#     else:
#         list.append('yes')
# for a in range(len(list)):
#     print(list[a]) 