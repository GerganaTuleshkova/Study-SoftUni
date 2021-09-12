import re

text = input()

pattern = r"(^|\s)[a-zA-Z0-9]+([-_\.][a-zA-Z0-9]+)*@[a-zA-Z]+(-[a-zA-Z]+)*(\.[a-zA-Z]+(-[a-zA-Z]+)*)+"

found_valid_mails_list = re.finditer(pattern, text)

mails = [mail.group() for mail in found_valid_mails_list]
print("\n".join(mails))
