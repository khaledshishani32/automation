import shutil
import re
from faker import Faker

fake = Faker('en_US')

potential_contacts = ""


for i in range(100):

    email = fake.email()
    phone_number = fake.phone_number()
    potential_contacts += " " + email + " "
    potential_contacts += phone_number
    

    if i % 7 == 0:
        potential_contacts += " " + email + " "
        

    if i % 9 == 0: 
        potential_contacts += phone_number
        


   


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
