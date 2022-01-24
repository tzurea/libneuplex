import requests
import json
from bs4 import BeautifulSoup as bs
import sqlite3
from datetime import date

con = sqlite3.connect('/home/azine/dist/scripts/enentrance/peadailycap/qn.db')
cur = con.cursor()
if __name__ == "__main__":
    headers = {
    'Connection': 'keep-alive',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="96"',
    'Accept': 'application/json, text/plain, */*',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36',
    'sec-ch-ua-mobile': '?0',
    'Authorization': 'Bearer jAAFi7LEEkR4n6sq7ekNGwP7dAdsydgIAfAj7S1V4oyoxmhd4ermiX7cVPCz',
    'sec-ch-ua-platform': '"Linux"',
    'Content-Type': 'application/json',
    'Origin': 'https://engineeringdote.com',
    'Sec-Fetch-Site': 'same-site',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Dest': 'empty',
    'Referer': 'https://engineeringdote.com/',
    'Accept-Language': 'en-US,en;q=0.9',
}
    data = '{"university":"ioe"}'

    response = json.loads(requests.post('https://api.engineeringdote.com/daily-test/start-exam', headers=headers, data=data).text)
    print(response)
    sessionID = response["examSessionId"]

    questionIDs = ""
    qnlist = response["questions"]
    for iqn in qnlist:
        questionIDs = questionIDs + str(iqn) + ","
    questionIDs = questionIDs[:-1]
    print(questionIDs)
    data = {

        "sessionID":sessionID,
        "questionIDs":questionIDs
        }

    response = json.loads(requests.post('https://api.engineeringdote.com/exam/questions', headers=headers, data=json.dumps(data)).text)

    for index,value in enumerate(response):
        value = value["questionData"]
        id = value['id']
        marks = value['marks']
        unit_id = value['unit_id']
        subject_id = value['subject_id']
        quest_title = bs(value['quest_title'],features="html5lib").get_text()
        ans1_txt = bs(value['ans1_txt'],features="html5lib").get_text()
        ans2_txt = bs(value['ans2_txt'],features="html5lib").get_text()
        ans3_txt = bs(value['ans3_txt'],features="html5lib").get_text()
        ans4_txt = bs(value['ans4_txt'],features="html5lib").get_text()
        cur.execute("""INSERT INTO qn(id,marks,unit_id,subject_id,quest_title,ans1_txt,ans2_txt,ans3_txt,ans4_txt) VALUES (?,?,?,?,?,?,?,?,?);""",(id,marks,unit_id,subject_id,quest_title,ans1_txt,ans2_txt,ans3_txt,ans4_txt))

    cur.execute("""INSERT INTO dtable(sessionID,qnlist) VALUES (?,?);""",(str(date.today()),str(qnlist)))
    con.commit()
    con.close()


 
