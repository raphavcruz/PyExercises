# f-sring syntax formatting

from email.mime import message


first_name = "Raphael"
last_name = "Cruz"
location = "Toronto"
profession = "Electronics Technician"
affiliation = "Sinclair Intrplntry by RL"

message = (
    f"Hi {first_name + last_name}! "
    f"You are a {profession}, living in {location}, "
    f"Working for {affiliation}"
)

print(message)