

import re

# ? PATTERN MATCHING WITH REGULAR EXPRESSIONS

'''
#  ! 415-555-4242

# def isPhoneNumber(text):
#     if len(text) != 12:
#         return False

#     for i in range(12):
#         if i == 3 or i == 7:
#             if text[i] != '-':
#                 return False
#             else:
#                 continue
#         if not text[i].isdecimal:
#             return False

#     return True


# print(isPhoneNumber('415-555-4244'))

#  ! 415-555-4242

phoneNUmRegex = re.compile(r'\d{3}-\d{3}-\d{4}')

mo = phoneNUmRegex.search("My phone number is 415-473-3289. ")
print('Phone number found: {}'.format(mo.group()))


# * GROUPING PARENTHESIS

phoneNUmRegex = re.compile(r'(\d{3})-(\d{3}-\d{4})')

mo = phoneNUmRegex.search("My phone number is 415-473-3289. ")
print('Phone number found: {}'.format(mo.group()))
print('Group 0: {}'.format(mo.group(0)))
print('Group 1: {}'.format(mo.group(1)))
print('Group 2: {}'.format(mo.group(2)))
print('All groups: {}'.format(mo.groups()))

areaCode, mainNUmber = mo.groups()
print(areaCode)
print(mainNUmber)


# heroRegex = re.compile(r'Batman|Batmobile|Batcopter|Batbat') # ! Same as heroRegex = re.compile(r'Bat(man|mobile|copter|bat)')
# heroMo = heroRegex.search('Batmobile lost a wheel')
# print(heroMo.group(0))
# # print(heroMo.group(1))
'''

# # ? OPTIONAL MAPPING WITH THE QUESTION MARK

# batRegex = re.compile

# # ! MATCHING EVERYTHING WITH DOT STAR

# nameRegex = re.compile(r'First name: (.*) Last name: (.*)')

# mo = nameRegex.search('First name: AI Last name: Sweigart')
# print(mo.groups())

# # ! MATCHING EVERYTHING WITH DOT STAR QUESTION MARK

# nonGreedyRegex = re.compile(r'<.*?>')
# mo = nonGreedyRegex.search('<To serve man> for dinner.>')
# print(mo.group())


# nameRegex = re.compile(r'(Agent) (\w)(\w*)')
# mo = nameRegex.sub(r'\1\2\3', 'Agent Alice gave the secret to Agent Bob and Agent Pandas')
# print(mo)


# * MANAGING COMPLEX REGEX

# phoneNUmRegex = re.compile(r'''()''', re.VERBOSE)
phoneNUmRegex = re.compile(r'(\d{3}|\(\d{3}\))?(-|\s|\.)?(\d{3})(-|\s|\.)(\d{4})()?')

# phoneNUmRegex = re.compile(r'''(
    
#     (\d{3})?  # Area code
#     (-|\s|\.)?  # Separator
#     (\d{3})  # First 3 digits
#     (-|\s|\.)  # Separator
#     (\d{4})  # Last 4 digits
#     ()?  # Extension
    
    
#     )''', re.VERBOSE)

matches = []
mo = phoneNUmRegex.search('My phone number is 432-343-2345')
for groups in phoneNUmRegex.findall('My phone number is 432-343-2345 and (321)-432-3453'):
    print(groups)
    # phoneNum = ''.join(groups)
    # matches.append(phoneNum)


# print(matches)

    


















