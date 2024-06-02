from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
import time
import random

browser = webdriver.Firefox()
browser.get("https://ru.wikipedia.org/wiki/%D0%A1%D0%BE%D0%BB%D0%BD%D0%B5%D1%87%D0%BD%D0%B0%D1%8F_%D1%81%D0%B8%D1%81%D1%82%D0%B5%D0%BC%D0%B0")

print("1)Листать параграфы страницы")
print("2)Перейти на одну из связанных страниц")
print("3)Закрыть браузер")
a = input("Введите число: ")
vybor = a
hatnotes = []
def search():
    if vybor == "1":
        paragraphs = browser.find_elements(By.TAG_NAME, "p")
        for paragraph in paragraphs:
            print(paragraph.text)
            input()
            if input() == "q":
                break
    elif vybor == "2":
        for element in browser.find_elements(By.TAG_NAME, "div"):
            cl = element.get_attribute("class")
            if cl == "hatnote navigation-not-searchable":
                hatnotes.append(element)

        hatnote = random.choice(hatnotes)
        link = hatnote.find_element(By.TAG_NAME, "a").get_attribute("href")
        browser.get(link)

    elif vybor == "3":
        browser.quit()

search()

