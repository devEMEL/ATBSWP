import re

#15/03/1999 or 5/4/2001 to 4:5:2002
dateRegex = re.compile(r'(\d{1,2})(/|-)(\d{1,2})(/|-)(\d{4})')

mo = dateRegex.sub(r'\1:\3:\5 ','3/14/2019, 03-14-2019, and 2015/3/19')
# mo = dateRegex.search('3/14/2019,03-14-2019, and 2015/3/19 and 4/12/2004')
print(mo)

