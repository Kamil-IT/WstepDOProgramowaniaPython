import re

response = re.search('(.*)usun_to(.*)', "labpyt2019@gusun_tomail.pl")
print(response.group(1) + response.group(2))
