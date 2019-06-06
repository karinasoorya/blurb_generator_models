from selenium import webdriver
from selenium.webdriver.common.by import By
import re

summary = []
all_links = []
browser = webdriver.Chrome(executable_path= '/Users/Karina/Downloads/chromedriver')
browser.get('https://www.goodreads.com/list/show/1.Best_Books_Ever')

outfile = open('outfile.txt', 'a')

for i in range(81, 101):
    browser.get('https://www.goodreads.com/list/show/1.Best_Books_Ever?page='+str(i))
    links = [x.get_attribute('href') for x in browser.find_elements_by_xpath("//*[contains(@class, 'bookTitle')]")]
    for link in links:
            try:
                browser.get(link)
                sum = browser.find_elements_by_xpath("//*[contains(@id, 'freeText')]")
                x = sum[0].get_attribute('innerHTML')
                y = sum[1].get_attribute('innerHTML')
                if x[:20] == y[:20]:
                    ans = sum[1].get_attribute('innerHTML')
                    ans = ans.encode("utf-8")
                    summary.append(ans)
                    print ans
                    outfile.write(ans + '\n\n')
            except:
                print("Problem!")

outfile.close()

outfile = open('outfile.txt', 'r')
with open('true_finished', 'w') as true:
    for line in outfile:
        new_line = re.sub('<[^<]+?>', '', line)
        true.write(new_line)
