def remove_and_split(string, word):
    newStr = string.replace(word, "")
    return newStr.strip()
this = "    Aayush is a good boy.    "
n = remove_and_split(this, "Aayush")
print(n)