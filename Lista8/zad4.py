import re

res = re.match(r'(60*)-.*(70*)-.*(8001)', "600-700-8001")
print(res.groups())
