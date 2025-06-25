# Create a dictionary and print all keys and values.
contact = {
    "Vegash":1234,
    "Jeeva":2345,
    "Kathir":5678
}
for key,values in contact.items():
    print(key,"-----",values)

for val in contact.values():
    print(val)

for key in contact.keys():
    print(key)

cd = contact.copy()
print(cd)

print(contact.pop("Vegash"))
print(contact)

print(contact.keys())
print(contact.values())

print(contact.get("vegash"))
