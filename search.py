from random import choice, choices, randint, shuffle, uniform
from time import sleep
import undetected_chromedriver as uc
from selenium import webdriver
from selenium.common.exceptions import (NoSuchElementException,
                                        WebDriverException)
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


keyword = "How to Make Money Online Via YouTube Ads by earny varny"
print('---')
driver = uc.Chrome()
print('-2222')



def type_keyword(driver, keyword, retry=False):
    if retry:
        for _ in range(30):
            try:
                driver.find_element(By.CSS_SELECTOR, 'input#search').click()
                break
            except WebDriverException:
                sleep(3)

    input_keyword = driver.find_element(By.CSS_SELECTOR, 'input#search')
    input_keyword.clear()
    for letter in keyword:
        input_keyword.send_keys(letter)
        sleep(uniform(.1, .4))

    method = randint(1, 2)
    if method == 1:
        input_keyword.send_keys(Keys.ENTER)
    else:
        icon = driver.find_element(
            By.XPATH, '//button[@id="search-icon-legacy"]')
        ensure_click(driver, icon)




def scroll_search(driver, video_title):
    try: 
        for i in range(1,11):
            video = driver.find_element(By.XPATH,f'/html/body/ytd-app/div[1]/ytd-page-manager/ytd-search/div[1]/ytd-two-column-search-results-renderer/div[2]/div/ytd-section-list-renderer/div[2]/ytd-item-section-renderer/div[3]/ytd-video-renderer[{i}]/div[1]/div/div[1]/div/h3/a/yt-formatted-string')
            if video.text == video_title:
                video.click()
                return True
    except Exception as e:...


def search_video(driver, keyword, video_title):
    try:
        type_keyword(driver, keyword)
    except WebDriverException:
        try:
            type_keyword(driver, keyword, retry=True)
        except WebDriverException:
            raise Exception(
                "Slow internet speed or Stuck at recaptcha! Can't perfrom search keyword")

    msg = scroll_search(driver, video_title)

    if msg == 'failed':
        filters = driver.find_element(By.CSS_SELECTOR, '#filter-menu a')
        driver.execute_script('arguments[0].scrollIntoViewIfNeeded()', filters)
        sleep(randint(1, 3))
        ensure_click(driver, filters)

        sleep(randint(1, 3))
        sort = WebDriverWait(driver, 30).until(EC.element_to_be_clickable(
            (By.XPATH, '//div[@title="Sort by upload date"]')))
        ensure_click(driver, sort)

        msg = scroll_search(driver, video_title)

    return msg

def ensure_click(driver, element):
    try:
        element.click()
    except WebDriverException:
        driver.execute_script("arguments[0].click();", element)


driver.get('https://www.youtube.com/')
search_video(driver,keyword,video_title=keyword)
input('Enter')