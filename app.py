from bs4 import BeautifulSoup
from selenium import webdriver
from src import *


name = input("Please Enter the movie's/serie's name: ")
url = 'https://30nama.com/search?q=' + name

# Search for movie/serie on 30nama
browser = webdriver_option('chrome')
response = url_to_bs4(url,browser)
search_result = get_search_result(response)

space(2)

# choose between searched movies/series
print('----- Please choose your desired movie/serie link -----')
for idx,result in enumerate(search_result):
    print(str(idx) + ': ' + result)
selected = int(input('Your choice:'))

selected_url = 'https://30nama.com' + search_result[selected] + '?section=comments'


#click on more to show all comments
click_more_comments(browser,selected_url)



response = browser.page_source
res = extract_comments(browser.page_source)
k

for item in res:
    print('-----')
    print(item)

   





# result = []
# soup = BeautifulSoup(response, 'html.parser')
# for comment in soup.find_all('p'):
#     if comment.get('data-v-0b757e80') == '':
#         print(comment.contents)
#         # result.append(comment.contents)



# print(response)