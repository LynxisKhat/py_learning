person = {
    'name':'Lynxis',
    'age':'25'
}

print(person)

person['hair_color']="grey"

print(person)

print('name' in person)

if 'name' in person:
    print(person['name'])

person_keys = list(person.keys());

person_values = list(person.values());

print(person_keys)

print(person_values)