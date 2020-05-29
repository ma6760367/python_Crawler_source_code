from bs4 import BeautifulSoup
import re
from urllib.parse import unquote

htmlStr = ""
with open("hhtml.txt", "r+", encoding="utf-8") as mm:
    htmlStr = mm.read()


soup0 = BeautifulSoup(htmlStr, 'lxml')
aa = soup0.find_all('div', attrs={"class": "icon-label"})


wifiName, address, email, phone, passwd, number = "", "", "", "", "", ""
for item in aa:
    # print(item)
    className = item.i["class"][0]
    if className == "pin-icon":
        address = item.span.text.strip()
    elif not address.strip():
        address = "null"

    if className == "wifi-icon":
        wifiName = item.span.text.strip()
    elif not wifiName.strip():
        wifiName = "null"

    if className == "locationdetail-hotspots-icon":
        number = item.span.text.replace("个热点", "").strip()
    elif not number.strip():
        number = "null"

    if className == "phone-icon":
        phone = item.span.text.strip()
    elif not phone.strip():
        phone = "null"

    if className == "mail-icon":
        emailll = item.span.a.span["data-cfemail"]
        email_list = re.findall(r'.{2}', emailll)
        key= email_list[0]
        ll=[]
        for e in email_list[1:]:
            r = hex(int(key,16) ^ int(e, 16))
            ll.append(r)
        a = "".join(ll)
        email = unquote(a.replace("0x", "%"))
    elif not email.strip():
        email = "null"

    if className == "cert-icon":
        passwd = item.span.text.strip()
    elif not passwd.strip():
        passwd = "null"

print(wifiName, address, email, phone, passwd, number)