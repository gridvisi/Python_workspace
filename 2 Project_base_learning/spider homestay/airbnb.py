'''
https://www.dazhuanlan.com/2020/01/02/5e0d47250070e/
'''


from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
import time

caps = webdriver.DesiredCapabilities.FIREFOX
caps['marionette'] = False
binary = FirefoxBinary(r'/Applications/Firefox.app/Contents/MacOS/firefox')
fp = webdriver.FirefoxProfile()
fp = fp.set_preference("permissions.default.image", 2)
driver = webdriver.Firefox(firefox_binary=binary,firefox_profile=fp,capabilities=caps)
# driver = webdriver.Chrome()
count = 0

for i in range(17):
    driver.get("https://www.airbnb.cn/s/%E4%B8%AD%E5%9B%BD%E4%BA%91%E5%8D%97%E7%9C%81%E6%98%86%E6%98%8E%E5%B8%82/homes?refinement_paths%5B%5D=%2Fhomes&click_referer=t%3ASEE_ALL%7Csid%3Ae0edcf07-0d9d-4406-a56a-d858a9278ba6%7Cst%3AMAGAZINE_HOMES&query=%E4%B8%AD%E5%9B%BD%E4%BA%91%E5%8D%97%E7%9C%81%E6%98%86%E6%98%8E%E5%B8%82&place_id=ChIJy9MnEsOD0DYRNgpPmKTzscw&allow_override%5B%5D=&s_tag=dCTwosuy&section_offset=4&items_offset="+str(i*18))
    rent_list = driver.find_elements_by_css_selector("div._v72lrv")
    for each_house in rent_list:
        name = each_house.find_element_by_css_selector("div._190019zr")
        name = name.text
        price = each_house.find_element_by_css_selector("span._1sfeueqe")
        price = price.text[4:7]
        fangxin = each_house.find_element_by_tag_name('span')
        fangxin = fangxin.text
        comment = each_house.find_element_by_css_selector("span._1gvnvab")
        comment = comment.text
        count += 1
        # print(price+'元', fangxin, name ,' '+comment+'条评价'+"n")
        aLine = "{}t{:>5}元tt{:<20}t{:<60}t{:>4}条评价 n".format(str(count), price.strip(), fangxin, name, comment)

    with open('airbnb.txt', 'a+') as f:    	# a+、r+、w+区别
        f.write(aLine)
    f.close()