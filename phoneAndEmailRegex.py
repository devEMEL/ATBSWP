
# ! THIS PROGRAMS FINDS ALL THE PHONE NUMBERS AND EMAIL ADDRESSES IN A PAGE

import pyperclip, re

# TODO 1: Create phone number regex
phoneNUmRegex = re.compile(r'(\d{3}|\(\d{3}\))?(\s|\.|-)?(\d{3})(-|\s|\.)(\d{4})')

# TODO 2: CReate email regex
emailRegex = re.compile(r'([a-zA-Z0-9+-._%]+)(@)([a-zA-Z0-9.-]+)(\.[a-zA-Z]{2,4})')


# TODO 3: Find matches in the clipboard text

text = str(pyperclip.paste())

matches = []
for groups in phoneNUmRegex.findall(text):
    phoneNum = ''.join(groups)
    matches.append(phoneNum)

for groups in emailRegex.findall(text):
    email = ''.join(groups)
    matches.append(email)

# TODO 4: Copy result the clipboard

if len(matches) > 0:
    result = '\n'.join(matches)
    pyperclip.copy(result)
    print('Copied to clipboard:')
    print('\n'.join(matches))
else:
    print('No phone numbers or email addresses found.')

