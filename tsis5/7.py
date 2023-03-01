import re
def to_camel_case(snake_str):
    titleCase =  snake_str.title().replace("_", "")
    camelCase = titleCase[0].lower() + titleCase[1:]
    return camelCase
print(to_camel_case(input()))
