
#Docstring are a way to document your functions. Needs to be added exactly as shown below.
def format_name(f_name, l_name):
     """Take a first and last name then return the title case version of the name."""
     formatted_f_name = f_name.title()
     formatted_l_name = l_name.title()
     return f"{formatted_f_name} {formatted_l_name}"

print(format_name("yeasir", "HUGAIS")) #hint: Hover over function to see docstring notations.