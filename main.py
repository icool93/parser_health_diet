# -*- coding: utf8 -*-
import re
from bs4 import BeautifulSoup

with open('blank/index.html') as file:
    scr = file.read()
# print(scr)

# scr.encoding = 'utf-8'
soup = BeautifulSoup(scr, 'lxml')

# title = soup.title
# print(title)
# # # print(title.text)
# # # print(title.string)
# page_h1 = soup.find('h1')
#
# print(page_h1)
#
# page_all_h1 = soup.find_all('h1')
# print(page_all_h1)
# for item in page_all_h1:
#      print(item.text)

# user_name = soup.find('div', class_='user__name')
# print(user_name.text.strip())
#
# user_name = soup.find('div', class_='user__name').find('span').text
# print(user_name)
# user_name = soup.find('div', {'class': 'user__name', 'id' : 'aaa'}).find('span').text
# print(user_name)
# find_all_spans_in_user_info = soup.find(class_='user__info').find_all('span')
# print(find_all_spans_in_user_info)
#
# for item in find_all_spans_in_user_info:
#     item.encoding = item.encode('ISO-8859-1')
#     print(item.text)

# social_links = soup.find(class_='social__networks').find('ul').find_all('a')
# print(social_links)
# all_a = soup.find_all('a')
# print(all_a)
#
# for item in all_a:
#     item_text = item.text
#     item_url = item.get('href')
#     print(f'{item_text}:{item_url}')

# .find.parent()  .find.parents()
# post_div = soup.find(class_='post__text').find_parent('div', 'user__post')
# # print(post_div)
# post_divs = soup.find(class_='post__text').find_parents()
# print(post_divs)
#  .next_element .previous_element
# next_el = soup.find(class_='post__title').next_element.next_element.text
# print(next_el)

# next_el = soup.find(class_='post__title').find_next().text
# print(next_el)
# next_sib = soup.find(class_='post__title').find_next_sibling()
# print(next_sib)
# next_sib = soup.find(class_='post__title').find_previous_sibling()
# print(next_sib)
# post_title = soup.find(class_='post__title').find_previous_sibling().find_next().text
# print(post_title)
# links = soup.find(class_='some__links').find_all('a')
# print(links)
# for link in links:
#     link_href_attr = link.get('href')
#     link_href_attr1 = link['href']
#     link_data_attr1 = link['data-attr']
#     link_data_attr = link.get('data-attr')
#     print(link_href_attr1)
#     print(link_data_attr1)

# find_a_by_text = soup.find('a', string="Одежда")
# print(find_a_by_text)
# find_a_by_text = soup.find('a', string="Одежда для взрослых")
# print(find_a_by_text)
# find_a_by_text = soup.find('a', text = re.compile("Одежда"))
# print(find_a_by_text)
find_all_clothes = soup.find_all(text=re.compile("([Оо]дежда)"))
print(find_all_clothes)