import re
def textm(text):
    patterns = 'a.*?b$'
    if re.search(patterns,  text):
        return ('Yes')
    else:
        return('No')
print(textm(input()))
