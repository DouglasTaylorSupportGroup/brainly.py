from bs4 import BeautifulSoup as bs

def parsePage(data):
    html = bs(data, "html.parser")
    answerRaw = html.find_all("div", attrs={"data-testid":"answer_box_text"})
    
    return answerRaw