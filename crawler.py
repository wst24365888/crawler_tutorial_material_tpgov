from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.keys import Keys
from article_outline import ArticleOutline
from firebase_service import FirebaseService

def fetchArticleOutline(driver, index):
    global firebaseService

    title = WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.XPATH, f"/html/body/form/div[3]/div/div/div/div[3]/div/div/div/div[2]/div/div/div/div/div/div/div/div/div/div/div/div[3]/div/div/div/div[2]/div/div/div/table/tbody/tr[{index}]/td[2]/span/a")))

    link = WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.XPATH, f"/html/body/form/div[3]/div/div/div/div[3]/div/div/div/div[2]/div/div/div/div/div/div/div/div/div/div/div/div[3]/div/div/div/div[2]/div/div/div/table/tbody/tr[{index}]/td[2]/span/a")))

    date = WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.XPATH, f"/html/body/form/div[3]/div/div/div/div[3]/div/div/div/div[2]/div/div/div/div/div/div/div/div/div/div/div/div[3]/div/div/div/div[2]/div/div/div/table/tbody/tr[{index}]/td[3]/span")))

    org = WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.XPATH, f"/html/body/form/div[3]/div/div/div/div[3]/div/div/div/div[2]/div/div/div/div/div/div/div/div/div/div/div/div[3]/div/div/div/div[2]/div/div/div/table/tbody/tr[{index}]/td[4]/span")))

    articleOutline = ArticleOutline(title.text, link.get_attribute("href"), date.text, org.text)

    # articleOutline.printArticleOutline()

    firebaseService.addArticleOutline(articleOutline)


def crawl():
    chorme_options = webdriver.ChromeOptions()
    chorme_options.add_argument("--headless")
    chorme_options.add_experimental_option(
        "excludeSwitches", ["enable-logging"])

    driver = webdriver.Chrome(options=chorme_options)
    driver.get("https://www.gov.taipei/News.aspx?n=D0042A87C2F0270A&sms=78D644F2755ACCAA")

    for index in range(1, 11):
        fetchArticleOutline(driver, index)

    driver.quit()


if __name__ == "__main__":
    firebaseService = FirebaseService()
    # firebaseService.fetchData()

    crawl()
