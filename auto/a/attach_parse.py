# -*- coding=UTF-8 -*-

import re
import base64
import win32clipboard

def get_hostname(url):
    from urlparse import urlparse
    parsed_uri = urlparse(url)
    domain = '{uri.scheme}://{uri.netloc}/'.format(uri=parsed_uri)
    return domain

#get url_attachpay from windows clipboard
win32clipboard.OpenClipboard()
url_attachpay = win32clipboard.GetClipboardData()
win32clipboard.CloseClipboard()

#if "aid=\d+" then only one group: the whole match, if "aid=(\d+)" then two groups, first being the whole match, second the string in between braces
aid = re.search("aid=(\d+)", url_attachpay).group(1)
tid = re.search("tid=(\d+)", url_attachpay).group(1)

aid_unencrypted = "%s|37aad6a9|1432140672|1|%s" % (aid, tid)
aid_encrypted = base64.b64encode(aid_unencrypted)

url = r"%sforum.php?mod=attachment&aid=%s" % (get_hostname(url_attachpay), aid_encrypted)

#set url to windows clipboard
win32clipboard.OpenClipboard()
#important, must empty clipboard first, otherwise it won't work
win32clipboard.EmptyClipboard()
win32clipboard.SetClipboardText(url)
win32clipboard.CloseClipboard()
