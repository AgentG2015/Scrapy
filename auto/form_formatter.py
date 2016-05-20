from mutils import *

raw_str = get_clipboard()

forms = []
strs = raw_str.split("&")
for str in strs:
    forms.append(str.split("="))

parsed_str = 'payload = {'
for form in forms:  
    parsed_str += "'%s': '%s'," % (form[0], form[1])
parsed_str += "}"

set_clipboard(parsed_str)