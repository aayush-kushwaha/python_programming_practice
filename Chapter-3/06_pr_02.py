
# name = input(" Enter your name:\n")
# date = input(" Enter date in this format (yyyy/mm/dd):\n")
# print("Dear" + name + "," + " You are selected!" + date)
letter = '''Dear <|Name|>,
You are selected!

Date: <|Date|>
'''
name = input(" Enter your name:\n")
date = input(" Enter date in this format (yyyy/mm/dd):\n")
letter = letter.replace("<|Name|>", name)
letter = letter.replace("<|Date|>", date)
print(letter)