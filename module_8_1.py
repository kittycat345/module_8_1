def add_everything_up(a, b):
    try:
        return a+b
    except:
        return str(a)+str(b)
print(add_everything_up(123.456, 'строка'))