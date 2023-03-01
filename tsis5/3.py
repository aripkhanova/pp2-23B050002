import re
def textm(text):
        patterns = '^[a-z]+_[a-z]+$'
        if re.search(patterns,  text):
                return ('Yes')
        else:
                return('No')

print(textm(input()))

