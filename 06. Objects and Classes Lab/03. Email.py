class Email:

    def __init__(self, sender, receiver, content):
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.is_sent = False

    def send(self):
        self.is_sent = True

    def get_info(self):
        return f"{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_sent}"


given_info = input()
emails = []

while not given_info == "Stop":
    sender, receiver, content = given_info.split()
    emails.append(Email(sender, receiver, content))
    given_info = input()


sent_mails =[int(i) for i in input().split(", ")]
for i in sent_mails:
    emails[i].send()

for mail in emails:
    print(mail.get_info())