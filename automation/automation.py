import shutil
import re
from faker import Faker

fake = Faker('en_US')

potential_contacts = ""

# existing_contacts = ""

###########################
# [Optional] explain what range is doing under the hood
###########################

# range_gen = range(100)

# print(type(range_gen))

# iterator = iter(range_gen)

# print(type(iterator))

# while True:

#     try:
#         i = next(iterator)
#     except StopIteration:
#         break

###########################

for i in range(100):

    email = fake.email()
    phone_number = fake.phone_number()
    potential_contacts += " " + email + " "
    potential_contacts += phone_number
    

    if i % 7 == 0: # every now and then throw in a duplicate email
        potential_contacts += " " + email + " "
        potential_contacts + fake.sentence()

    if i % 9 == 0: # every now and then throw in a duplicate phone number
        potential_contacts += phone_number
        potential_contacts += fake.paragraph()


    # if i % 5 == 0: # keep track of some "existing contacts" for the stretch goal
    #     existing_contacts += email + "\n"
    #     existing_contacts += phone_number + "\n"


    potential_contacts += "\n"





with open("potential-contacts.txt", "w+") as f:
    f.write(potential_contacts)

phone_text = list(re.findall(r"\w{3}-\w{3}-\w{4}", potential_contacts))
email_text = list(re.findall(r'[\w\.-]+@[\w\.-]+', potential_contacts))


def join_phone(phone_text):
    
     return (('\n').join(phone_text))

final_phone_filter=join_phone(phone_text)

with open("phone.txt" , "w") as f:
    f.write(final_phone_filter)







def join_email(email_text):
    
     return (('\n').join(email_text))

final_email_filter=join_email(email_text)
    

with open("email.txt" , "w") as f:
    f.write(final_email_filter)

# shutil.copy('potential-contacts.txt', 'automation/test/potential-contacts.txt')

# # for stretch goal
# with open("existing-contacts.txt", "w+") as f:
#     f.write(existing_contacts)

# shutil.copy('existing-contacts.txt', 'existing-contacts.txt')