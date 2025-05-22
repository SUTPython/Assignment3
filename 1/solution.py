number_of_entry = int(input())
entry = []
for _ in range(number_of_entry):
    income = eval(input())
    if type(income) is tuple:
        entry.append(income)
    else:
        pass
latitude = 0
longitude = 0
code = 0
secret_words = []
def filltering(tu):
    s = 0
    if (tu[0] + tu[1]) % 5 == 0:
        s += 1
    if tu[3][0].upper() == tu[3][0] and len(tu[3]) >= 3:
        s += 1
    if s == 2:
        return tu
valid_entry = list(filter(filltering, entry))
for er in valid_entry:
    latitude += er[0]
    longitude += er[1]
    code += er[2]
    secret_words.append(er[3])
secret_words.sort(key=len)
secret_string = ""
for word in secret_words:
    secret_string += word
latitude /= len(secret_words)
longitude /= len(secret_words)
latitude = round(latitude, 2)
longitude = round(longitude, 2)
final_gps = (latitude, longitude)
print(code)
print(secret_string)
print(final_gps)