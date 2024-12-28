#learning regular expression(regx)

#find all the email from a email log file

import re

email_log = """email received june2 from user1@email.com, email received june2 from user2@email.com, email received june2 from user3@email.com"""

# Correct regular expression to match email addresses
emails = re.findall("\w+@\w+\.\w+", email_log)

# Print the found email addresses
print(emails)


re.findall("\w", "h32rb17")

re.findall("\d", "h32rb17")

re.findall("\d+", "h32rb17")

re.findall("\d*", "h32rb17")

re.findall("\d{2}", "h32rb17 k825t0m c2994eh")

re.findall("\d{1,3}", "h32rb17 k825t0m c2994eh")

pattern = "\w+:\s\d+"
employee_logins_string = "1001 bmoreno: 12 Marketing 1002 tshah: 7 Human Resources 1003 sgilmore: 5 Finance"
print(re.findall(pattern, employee_logins_string))