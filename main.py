import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By


class craigslist_crawler(object):
    def __init__(self, query, page_index):
        self.query = query
        self.url = f"https://www.lazada.vn/catalog/?page={page_index}&q={query}"
        self.driver = webdriver.Chrome("chromedriver.exe")
        self.delay = 5

    def load_page(self):
        driver = self.driver
        driver.get(self.url)
        all_data = driver.find_elements(
            By.CLASS_NAME, "buTCk")
        for data in all_data:
            with open("data.csv", mode="a", encoding="utf-8") as f:
                item = data.text.split("\n")
                f.write(str(item[0])+","+str(item[1])+"\n")
        driver.close()


query = "điện thoại"
num_page = 102
for page_index in range(num_page):
    crawler = craigslist_crawler(query, page_index)
    crawler.load_page()
