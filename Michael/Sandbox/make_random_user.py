import random
import string
from names import first_name, last_name
from jobs import job

# name = first_name[random.randint(0, len(first_name))] + ' ' + last_name[random.randint(0, len(last_name))]

# username_extra = ''.join(random.choice(string.digits) for i in range(4))
# username = ''.join(random.choice(name) for i in range(6)) + username_extra
# username.replace(" ", "")

# chars = string.ascii_letters + string.digits + '!@#$%^&*()'
# password = ''.join(random.choice(chars) for i in range(8))

# email_extra = ''.join(random.choice(string.digits))
# email = name[:4].lower() + email_extra + '@yahoo.com'

# job = job[random.randint(0, len(job))]

# print('Name:', name, '| Username:', username, '| Password:',password, '| E-mail:',email, '| Job:',job)

def make_users():
    name = first_name[random.randint(0,len(first_name)-1)] + ' ' + last_name[random.randint(0,len(last_name)-1)]

    username_extra = ''.join(random.choice(string.digits) for i in range(4))
    username = ''.join(random.choice(name) for i in range(6)) + username_extra
    username.replace(" ", "")

    chars = string.ascii_letters + string.digits + '!@#$%^&*()'
    password = ''.join(random.choice(chars) for i in range(8))

    email_extra = ''.join(random.choice(string.digits))
    email = name[:4].lower() + email_extra + '@yahoo.com'

    jobb = job[random.randint(0,len(job)-1)]

    return ('Name:', name, '| Username:', username, '| Password:', password, '| E-mail:', email, '| Job:', jobb)

for i in range(20):
  print(make_users())