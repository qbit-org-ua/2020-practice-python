import requests

"""
r = requests.get("http://q-bit.dots.org.ua")
print(r.status_code)
r.encoding = "utf-8"
page_text = r.text
print(page_text[100:200])
print("<title>" in page_text)
print(page_text.find("</title>"))

print(
    page_text[page_text.find("<title>") + len("<title>") : page_text.find("</title>")]
)
"""

session = requests.Session()
login_form = {
    "from": "",
    "username": "test",
    "password": "test",
    "token": "bNqUGu0z4hT0PlCD",
}
r = session.post("http://q-bit.dots.org.ua/login", data=login_form)
# print(r.status_code)
# print(r.cookies)
# login_cookies = r.cookies

# r = requests.get("http://q-bit.dots.org.ua/contests", cookies=login_cookies)
r = session.get("http://q-bit.dots.org.ua/contests")
# print("Contests:", r.status_code)
r.encoding = "utf-8"
# print("Contests:", "недостаточно прав" in r.text)
# print("Contests:", r.text)

contests_page = r.text
contests_page = contests_page[contests_page.find('<a href="contests?id') :]
while contests_page.find('<a href="contests?id') != -1:
    print(contests_page[0 : contests_page.find("</a>")])
    contests_page = contests_page[contests_page.find('<a href="contests?id', 1) :]

contest_id = input("Введите ID турнира: ")

# r = requests.get("http://q-bit.dots.org.ua/contests?login=603", cookies=login_cookies)
r = session.get(f"http://q-bit.dots.org.ua/contests?login={contest_id}")
# print("Contests:", r.status_code)
# r.encoding = "utf-8"
# print("Contests:", r.text)

problem_id = input("Введите ID задачи [например, 1001]: ")
lang_id = input("Введите ID языка программирования [Python - 12]: ")
source_code = input("Введите исходный код решения: ")

solution_form = {
    "new": "2",
    "MAX_FILE_SIZE": "2097152",
    "pid": problem_id,
    "lang": lang_id,
    "ctype": "F",
    "source": source_code,
}
# r = requests.post(
#     "http://q-bit.dots.org.ua/solutions", data=solution_form, cookies=login_cookies
# )
r = session.post("http://q-bit.dots.org.ua/solutions", data=solution_form)
print("Solution POST status", r.status_code)
r.encoding = "utf-8"
# print(r.text)
