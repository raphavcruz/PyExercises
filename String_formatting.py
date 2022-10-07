# %-formatting
first_name = "Raphael"
last_name = "Cruz"
location = "Toronto"
profession = "Electronics Technician"
affiliation = "Sinclair Intrplntry by RL"

print(("Hello, {first_name} {last_name}. You are located in {location}. " + 
"You are a {profession}, working at {affiliation}.") \
.format(first_name=first_name, last_name=last_name, location=location, \
profession=profession, affiliation=affiliation))

