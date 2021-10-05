class MustContainAtSymbolError(Exception):
    pass


class NameTooShortError(Exception):
    pass


class InvalidDomainError(Exception):
    pass


valid_domains = ["com", "bg", "net", "org"]
while True:
    command = input()
    if command == "End":
        break
    if "@" not in command:
        raise MustContainAtSymbolError("Email must contain @")
    emails_args = command.split("@")
    name = emails_args[0]
    if len(name) <= 4:
        raise NameTooShortError("Name must be more than 4 characters")

    domain = emails_args[1].split(".")[-1]
    if domain not in valid_domains:
        raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net")
    print("Email is valid")

