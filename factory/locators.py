from selenium.webdriver.common.by import By

class MainPageLocator(object):
    BROWSE_BTN = (By.CSS_SELECTOR, "#page-top > section > div > div > div > a:nth-child(4)")
    TITLE_LABEL = (By.CSS_SELECTOR, "#page-top > section > div > div > div > h4")

class SearchPageLocator(object):
    SEARCH_FIELD = (By.XPATH, "/html/body/div[1]/form/div/input")
    SEARCH_BTN = (By.CSS_SELECTOR, "#page-top > div:nth-child(2) > form > div > button")
    CHOOSE_BTN = (By.CSS_SELECTOR, "#type")

class BrowsePageLocator(object):
    ERROR_MSG = (By.XPATH, "/html/body/div[2]/div")
    VALID_QUESTION = (By.CSS_SELECTOR, "#page-top > div:nth-child(3) > table > tbody > tr > td:nth-child(5)")
    FIRST_ITEM_SEARCH = (By.XPATH, "/html/body/div[2]/table/tbody/tr[1]/td[2]")
    TWENTY_FIFTH_ITEM_SEARCH = (By.XPATH, "/html/body/div[2]/table/tbody/tr[25]/td[2]")
    PAGE_CONTROL = (By.XPATH, "/html/body/div[2]/center/ul")



