import re

text ="aa"

pattern = r"a^.*a$"

phoneReg = r"^[07, 01]\d{8}$"

print(re.search(pattern, text))