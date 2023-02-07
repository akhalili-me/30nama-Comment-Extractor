from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException,NoSuchElementException

def get_movie_url(name):
    name = name.replace(' ', '+')
    url = 'https://30nama.com/search?q=' + name + '+'
    return url

def webdriver_option(browser):

    options = {
        'firefox': webdriver.FirefoxOptions,
        'chrome': webdriver.ChromeOptions,
        'edge': webdriver.EdgeOptions
    }
    
    option_class = options.get(browser, webdriver.FirefoxOptions)
    options = option_class()
    options.add_argument("--headless")
    driver_map = {
        'firefox': webdriver.Firefox,
        'chrome': webdriver.Chrome,
        'edge': webdriver.Edge
    }
    
    driver = driver_map.get(browser, webdriver.Firefox)(options=options)
    return driver

def url_to_bs4(url,browser):
    browser.get(url)
    return browser.page_source

def space(count):
    print('\n' * count)

def get_search_result(response):
    result = []
    soup = BeautifulSoup(response, 'html.parser')
    for link in soup.find_all('a'):
        if link.get('data-v-26f0bc8b') == '':
            result.append(link.get('href'))

    return result 

def click_more_comments(browser,url,count=1):
    browser.get(url)
    for i in range(count):
        try:
            element = browser.find_element(By.XPATH,"//div[@data-v-75ef1040='' and @data-v-7237fd26='']")
            browser.execute_script("arguments[0].scrollIntoView();", element)
            browser.execute_script("arguments[0].click();", element)
        except TimeoutException:
            break
        except NoSuchElementException:
            break

def check_comment(comment):
    return comment not in ['برای امتیاز‌دهی باید وارد شوید','۰','۱','۲','۳','۴','۵','۶','۷','۸','۹']

def extract_comments(response):
    result = []
    soup = BeautifulSoup(response, 'html.parser')
    for comment in soup.find_all('p'):
        if comment.get('data-v-0b757e80') == '':
            str_comment = str(comment.contents[0]).strip()
            if check_comment(str_comment):
                result.append(str_comment)
    
    return result

