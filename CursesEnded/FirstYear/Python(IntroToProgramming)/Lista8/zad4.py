import re

response = re.compile('(.*)-(.*)-(.*)').match("600-700-8001")
print(f"('{response.group(1)}' '{response.group(2)}' '{response.group(3)}')")