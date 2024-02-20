# def st_to_upper(function):
#     def innerfunc(msg):
#         func = function(msg)
#         upper = func.upper()
#         return upper
#     return innerfunc

# @st_to_upper
# def hello_func(msg):
#     return ("hello "+str(msg))


# print(hello_func('ram'))


def dict_add(function):
    def key_value(key,value):
        key = str(key).upper()
        value = str(value).capitalize()
        func = function(key,value)
        func[key] = value
        return func
    return key_value

d = {}

@dict_add
def add_to_dict(key,val):
    return d

add_to_dict('one','ram')
add_to_dict('two','shyam')
print(d)