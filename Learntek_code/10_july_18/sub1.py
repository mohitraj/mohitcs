import re
file = "12%^333*$%"

file = re.sub(r'[^a-zA-Z0-9]', '-', file)

print file