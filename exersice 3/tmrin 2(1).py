number = int(input())
emails= []
for i in range(number):
    emails.append(input())

domain= []
for email in emails:
    for i in range(len(email)):
        if email[i] == '@':
            domain.append(email[i+1:])
res = sorted(set(domain))
for i in res:
    print(i)            