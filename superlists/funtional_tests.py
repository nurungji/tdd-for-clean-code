from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

# http://blog.harveyk.me/post/selenium3-FireFox50-geckodriver-error-solve/

browser = webdriver.Firefox(executable_path=r'D:\_Dev\venv-34\Scripts\geckodriver.exe')
# browser.get('http://www.naver.com')
browser.get('http://localhost:8000')

assert 'Django' in browser.title
