import re
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d')
print(phoneNumRegex.findall('siema siema ffdsfdds 534-453-555, dsad 444-231-333'))
#print('Znaleziono nr tel ' +mo.group())