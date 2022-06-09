
from selenium import webdriver
from time import sleep
options = webdriver.ChromeOptions()
options.add_argument('disable-infobars')
driver = webdriver.Chrome(chrome_options=options)


with open('detail.txt',"a+") as f:
    for i in range(1,18):
        driver.get("http://sz.ziroom.com/z/nl/z2-d23008674-b611100954.html?p="+str(i))
        sleep(1)
        rent_list = driver.find_elements_by_css_selector('li.clearfix')
    for echo_house in rent_list:
        detail = echo_house.find_element_by_css_selector('div.detail')
        print(detail.text)
        price = echo_house.find_element_by_css_selector('div.priceDetail')
        print(price.text)
        f.write(detail.text)
        f.write(price.text)

f.close()
