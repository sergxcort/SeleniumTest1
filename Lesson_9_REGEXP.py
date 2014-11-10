"""TST-10, Client is not 222-22-22 opening, Tester, Critical, TST-11
TST-11, Database issue, Test Analyst, Medium, None
TST-12, Spelling is email@me.com wrong, Test Manager, Low, None
TST-13, Server processing is slow on https://private.ru, Tester, Critical, TST-14
TST-14, Large data http://hosting.com processing issue, Tester, Low, None
TST-15, Unknown issue (044)2930212, Test Automator, Low, None
TST-16, Button is not showing, Tester, High, None
TST-17, Calculation form 0.0.0.1 should 192.168.0.1 not work, Test Mager, Medium, None"""

import re
str = __doc__
pattern_1 = r"(\d{3}-\d{2}-\d{2})"
pattern_2 = r"(\(\d{3}\)\d{7})"
email_pattern = r"(\w+@\w+\.\w+)"
match = re.search(pattern_1,str)
match2 = re.search(pattern_2,str)
match3 = re.search(email_pattern,str)

print match.groups()[0]
print match2.groups()[0]
print match3.groups()[0]
print match2.span()
