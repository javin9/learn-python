import re

text = 'Today is 11/27/2012. PyCon starts 3/13/2013.'

# 'Today is 2012-11-27. PyCon starts 2013-3-13.'
new_text = re.sub(r'(\d+)/(\d+)/(\d+)', r"\3-\1-\2", text)
print(new_text)  # Today is 2012-11-27. PyCon starts 2013-3-13.

text = 'UPPER PYTHON, lower python, Mixed Python'

print(re.findall(r'python', text, flags=re.IGNORECASE))
print(re.sub(r'python', 'snake', text, flags=re.IGNORECASE))


def handler(m):
    print(m.group())
    return m.group().upper()


re.sub(r'python', handler, text, flags=re.IGNORECASE)


def matchcase(word):

    def replace(m):
        text = m.group()
        if text.isupper():
            return word.upper()
        elif text.islower():
            return word.lower()
        elif text[0].isupper():
            return word.capitalize()
        else:
            return word

    return replace
