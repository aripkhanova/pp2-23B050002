import re
def capital_words(str):
  return re.sub(r"(\w)([A-Z])", r"\1 \2", str)

print(capital_words(input()))

