#Output function
def format_name(f_name, l_name):
     formatted_f_name = f_name.title()
     formatted_l_name = l_name.title()
     return f"{formatted_f_name} {formatted_l_name}"

print(format_name("yeasir", "HUGAIS")) #output: Yeasir Hugais

#example of a built in output function
print(len("hello")) #output: 5