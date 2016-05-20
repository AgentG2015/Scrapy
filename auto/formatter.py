from mutils import *

parsed_str = ""
parsed_str += get_header()
parsed_str += "\n\n"
parsed_str += get_cookie()
parsed_str += "\n\n"
parsed_str += get_url()

set_clipboard(parsed_str)
