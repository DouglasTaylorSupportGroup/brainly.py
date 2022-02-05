from .parsers import cookieParser, pageParser
from . import requestPage

def answer(url, cookie, userAgent):
    cookieStr = cookieParser.parseCookie(cookie)
    htmlData = requestPage.requestWebsite(url, cookieStr, userAgent)
    data = pageParser.parsePage(htmlData)
    return data