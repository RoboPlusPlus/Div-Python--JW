import json

#Dict som skal holde entries til Json-dokumentet
attrbutes_to_json = {}


#Dette blir nivå 1 av dict
user_names = ["Joachim", "harold", "Bob", "Laila"]


#Parametre til å fylle opp dictet med
sillyness = 1
active = True
other_attribute = "value"


#Fyller opp et dict
for name in user_names:
    user_settings = \
        {
            "Active": active,
            "Other_attribute": other_attribute,
            "Sillyness": sillyness

        }
    user_settings.update(hjk="io", kk="horse")

    attrbutes_to_json.update({name: user_settings})
    sillyness +=1
    active = True if active == False else False
    other_attribute = "{} extended".format( other_attribute)


#Dumper dict inn i Json-objekt
save_this_to_file = json.dumps(attrbutes_to_json, sort_keys=True, indent=4)


# Skriver Dict til Json fil
with open('Settings_file.json', 'w') as fh:
    fh.write(save_this_to_file)


#Leser fra Json-fil igjen
with open('Settings_file.json', encoding='utf-8') as data_file:
    data = json.loads(data_file.read())

#Printer
for name in user_names:
    print(name + ": ")
    print(data[name])
    print('\n')



