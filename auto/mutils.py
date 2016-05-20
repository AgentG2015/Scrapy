import os

def get_filename(filename):
    return os.path.basename(filename)[:-3]


def get_hostname(url):
    from urlparse import urlparse
    parsed_uri = urlparse(url)
    domain = '{uri.scheme}://{uri.netloc}/'.format(uri=parsed_uri)
    return domain


def get_clipboard():
    import win32clipboard
    win32clipboard.OpenClipboard()
    ret = win32clipboard.GetClipboardData()
    win32clipboard.CloseClipboard()
    return ret


def set_clipboard(data):
    import win32clipboard
    win32clipboard.OpenClipboard()
    # important, must empty clipboard first, otherwise it won't work
    win32clipboard.EmptyClipboard()
    win32clipboard.SetClipboardText(data)
    win32clipboard.CloseClipboard()


def get_strlist():
    raw_str = get_clipboard()
    return raw_str.split("\r\n")


def get_header():
    strlist = get_strlist()
    header_strs = strlist[1:-3]
    ret = "HEADERS = {\n"
    count = len(header_strs)
    i = 0
    for str in header_strs:
        i += 1
        index = str.find(":")
        key = str[:index]
        value = str[index+2:]
        end_str = ",\n"
        if i == count:
            end_str = "\n"
        ret += "    '%s': '%s'%s" % (key, value, end_str)
    ret += "}"
    return ret


def get_cookie():
    strlist = get_strlist()
    cookie_str = strlist[-3]
    ret = "COOKIES = {\n"
    cookie_str = cookie_str[8:]
    splited_strs = cookie_str.split("; ")
    count = len(splited_strs)
    i = 0
    for str in splited_strs:
        index = str.find("=")
        key = str[:index]
        value = str[index+1:] 
        i += 1
        end_str = ",\n"
        if i == count:
            end_str = "\n"
        ret += "    '%s': '%s'%s" % (key, value, end_str)
    ret += "}"
    return ret


def get_url():
    strlist = get_strlist()
    hostname = "http://" + strlist[1].split(": ")[1]
    lindex = strlist[0].find(" ")
    rindex = strlist[0].rfind(" ")
    return "url = '%s'" % (hostname + strlist[0][lindex+1:rindex])


def rename_ext(f, src_ext, dest_ext):
    rindex = f.rfind('.')
    if rindex < 0:
        print 'error: ' + f
        return
    base = f[:rindex]
    ext = f[rindex+1:]
    if ext == src_ext:
        os.rename(f, base + '.' + dest_ext)