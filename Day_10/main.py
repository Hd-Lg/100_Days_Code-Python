def format_name(f_name, l_name):
    if f_name == '' or l_name == '':
        return "You didn't provide inputs"
    return f_name.title() + ' ' + l_name.title()


good_format = format_name("Jean", "dupont")
print(good_format)
