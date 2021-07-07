from selenium import webdriver
options = webdriver.ChromeOptions()
options.headless = True
options.add_argument('window-size=1920x1050')
# User-agent 정보가 HeadlessChrome으로 뜨게하지 않기 위해 추가
options.add_argument('user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36')

browser = webdriver.Chrome(options=options)
browser.maximize_window()

url = "https://www.whatismybrowser.com/detect/what-is-my-user-agent"
browser.get(url)


# Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)
# AppleWebKit/537.36 (KHTML, like Gecko)
# Chrome/91.0.4472.114 Safari/537.36

detected_value = browser.find_element_by_id('detected_value')
print(detected_value.text)
browser.quit()

# Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)
# AppleWebKit/537.36 (KHTML, like Gecko)
# HeadlessChrome/91.0.4472.114 Safari/537.36
# -> HeadlessChrome이 headers에 포함되어 서버가 block할 가능성

# https://selenium-python.readthedocs.io/