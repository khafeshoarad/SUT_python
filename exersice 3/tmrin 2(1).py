def get_unique_domains(emails):
    domains = set()
    for email in emails:
        at_index = email.find('@')
        if at_index != -1:
            domains.add(email[at_index + 1:])
    return sorted(domains)

def main():
    number = int(input("Enter the number of emails: "))
    emails = [input("Enter email: ") for _ in range(number)]

    unique_domains = get_unique_domains(emails)

    for domain in unique_domains:
        print(domain)

if __name__ == "__main__":
    main()
