from .parsers import cookieParser
from . import requestPage

async def answer(url, cookie, userAgent):
    cookieStr = cookieParser.parseCookie(cookie)
    htmlData = requestPage.requestWebsite(url, cookieStr, userAgent)
