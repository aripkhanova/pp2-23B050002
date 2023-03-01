import re
def textm(text):
        patterns = 'ab{2,3}'
        if re.search(patterns,  text):
                return ('Yes')
        else:
                return('No')
print(textm(input()))