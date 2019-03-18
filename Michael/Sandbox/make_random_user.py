import random
import string
from names import first_name, last_name
from jobs import job

name = first_name[random.randint(0,len(first_name))] + ' ' + last_name[random.randint(0,len(last_name))]

chars = string.ascii_letters + string.digits + '!@#$%^&*()'
password = ''.join(random.choice(chars) for i in range(8))

email_extra = ''.join(random.choice(string.digits))
email = name[:4].lower() + email_extra + '@yahoo.com'

job = job[random.randint(0,len(job))]

print('Name:', name, 'Password:',password, 'E-mail:',email, 'Job:',job)

