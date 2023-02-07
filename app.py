from src import *

#Build movie/serie URL
name = input("Please Enter the movie's/serie's name: ")
url = get_movie_url(name)


# Search for movie/serie on 30nama
browser = webdriver_option('firefox')
response = url_to_bs4(url,browser)
search_result = get_search_result(response)

space(1)


# choose between searched movies/series
print('----- Please choose your desired movie/serie link -----')
for idx,result in enumerate(search_result):
    print(str(idx) + ': ' + result)
selected = int(input('Your choice:'))
selected_url = 'https://30nama.com' + search_result[selected] + '?section=comments'



#click on more button to show all comments
click_more_comments(browser,selected_url,2)


#Extracting comments
comments = extract_comments(browser.page_source)

#Printing the result 
for item in comments:
    print('-----')
    print(item)
