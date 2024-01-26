vorudi = input("Enter a space-separated string: ")
codes = vorudi.split()
codes.sort(key=lambda x: int(x[1:]))

result = "".join(item[0] for item in codes)
print(result)
