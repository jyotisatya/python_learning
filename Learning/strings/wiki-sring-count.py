climate = """In coeat of @#@#@#The## testhe The."""


def clean_string(s):
    cleaned = ''
    for char in s:
        if char.isalnum() or char.isspace():
            cleaned += char
    return cleaned


climate_array = climate.split()
count = 0

for item in climate_array:
    count += 1 if clean_string(item).lower() == 'the' else 0

print(count)  

