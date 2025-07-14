import re


def startWidth(sub, data):
    return data.startswith(sub)


def mystartWidth(sub, data):
    regex_str = f'\A{sub}'
    result = re.findall(regex_str, data)
    for i in result:
        return True
    return False


def myEndWidth(sub, data):
    regex_str = f'{sub}\Z'
    result = re.findall(regex_str, data)
    for i in result:
        return True
    return False


if __name__ == "__main__":
    print(mystartWidth("123", "123456"))  # True
    print(mystartWidth("123", "456123"))  #
    print(myEndWidth("123", "456123"))  # True
    print(myEndWidth("123", "123456"))  # False
