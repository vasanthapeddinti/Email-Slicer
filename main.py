# The program inputs an email address and returns the username 
# and domain name

import re

user_email_address = input("Please input your email address: ")

pattern = r'^(/w)($@)(/w)($.)([a-z])'
 if re.serach(user_email_address, pattern):
     pass
else:
    print("Invaild email address")

list1 = user_email_address.split("@")
list2 = list1[1].split(".")

print(f"The username is {list1[0]}")
print(f"The domain name is {list2[0]}")

