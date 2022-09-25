
# myTuple = ('hello','-','world')

# print(''.join(myTuple))
# use group() or groups(0)
import re

# emailRegex = re.compile(r'([a-zA-Z0-9+-._%]+)(@)([a-zA-Z0-9.-]+)(\.[a-zA-Z]{2,4})')
# for groups in emailRegex.findall('dominica400@gmail.com and yes omah@yes.com'):
#     email = ''.join(groups)
#     print(email)

# mo = phoneNUmRegex.search('My phone number is 432-343-2345')
# phoneNUmRegex = re.compile(r'(\d{3}|\(\d{3}\))?(-|\s|\.)?(\d{3})(-|\s|\.)(\d{4})()?')
# for groups in phoneNUmRegex.findall('My phone number is 432-343-2345 and (321)-432-3453'):
#     phoneNum = ''.join(groups)
#     print(phoneNum)

# # for email in emailRegex.findall('dominica400@gmail.com is a good one and one34@yahoo.com'):
#     # print(email)

# nonGreedyRegex = re.compile(r'<.*?>')
# mo = nonGreedyRegex.search('<To serve man> for dinner.>')
# print(mo.group())

newLineRegex = re.compile(r'.*', re.DOTALL)
om = newLineRegex.search('Save the public\nHello World \nHope is still there')
print(om.group())
