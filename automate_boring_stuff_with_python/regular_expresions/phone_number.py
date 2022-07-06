import pyperclip, re

phoneRegex = re.compile(r'''(
    (\+?\d{2})?
    (\s|-|\.)?
    (\d{3})                           
    (\s|-|\.)?
    (\d{3})                           
    (\s|-|\.)?
    (\d{3})                           
)''',re.VERBOSE)

mailRegex = re.compile(r'''(
    [a-zA-Z0-9._%+-]+
    @
    [a-zA-Z0-9.-]+
    (\.[a-zA-Z]{2,4})
)''',re.VERBOSE)

text = str(pyperclip.paste())
matches =[]
for groups in phoneRegex.findall(text):
    if groups[1]:
        phoneNum = "-".join([groups[1], groups[3], groups[5], groups[7]])
    else:
        phoneNum = "-".join([groups[3], groups[5], groups[7]])
    matches.append(phoneNum)


for groups in mailRegex.findall(text):
    matches.append(groups[0])

if len(matches)>0:
    pyperclip.copy('\n'.join(matches))
    print("Skopiowano do schowka: ")
    print("\n".join(matches))
else:
    print("Nie znaleziono żadnego numeru telefonu lub adresu e-mail")

