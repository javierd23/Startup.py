#This is how we get a most repeating word from a file.
file = open('words.txt')
email = {}


for lines in file:
    if lines.startswith('From '):
        words = lines.split()
        if words[1] not in email:
            email[words[1]] = email.get(words[1], 0) + 1


kemail = None
vemail = None

for keys,values in email.items():
    if kemail is None:
        kemail = values
    elif values > kemail:
        kemail = values
    if vemail is None:
        vemail = keys
    elif keys > vemail:
        vemail = keys


print(vemail, kemail)