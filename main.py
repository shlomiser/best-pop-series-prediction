import csv
import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    driver = webdriver.Chrome('chromedriver.exe')
    driver.get("https://www.hobbydb.com/")
    driver.maximize_window()
    wait = WebDriverWait(driver, 7)
    time.sleep(5)
    print(driver.title)
    wait.until(EC.element_to_be_clickable((By.LINK_TEXT, 'Subjects'))).click()
    wait.until(EC.element_to_be_clickable((By.LINK_TEXT, 'Funko'))).click()
    time.sleep(5)
    driver.switch_to.window(driver.window_handles[1])
    driver.get("https://www.hobbydb.com/marketplaces/hobbydb/subjects/funko-brand")
    wait.until(EC.element_to_be_clickable((By.LINK_TEXT, 'Series'))).click()
    time.sleep(7)
    Names = []
    Types = []
    Brandes = []
    Serieses = []
    Scales = []
    Status = []
    Status_2 = []
    References = []
    Released_Dates = []
    Prices = []
    Ratings = []
    Final_Status = []
    names_pos = 0
    try:
        wait.until(EC.element_to_be_clickable((By.LINK_TEXT, 'Series'))).click()
        time.sleep(7)
    except:
        0
    i = 2
    for_data_base = 0
    elements = driver.find_elements(By.CLASS_NAME, 'col-md-4.ng-scope')
    for element in elements:
        #categories = element.find_element(By.CLASS_NAME, 'ng-binding.ng-scope')
        links = element.find_element(By.CLASS_NAME, 'ng-binding.ng-scope')
        links.click()
        time.sleep(7)
        driver.switch_to.window(driver.window_handles[i])

        last_height = driver.execute_script("return document.body.scrollHeight")
        scroll_counter = 0
        max_scrolls = 10
        while scroll_counter < max_scrolls:
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(7)
            new_height = driver.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                break
            else:
                last_height = new_height
            scroll_counter += 1
        last_height = driver.execute_script("return document.body.scrollHeight")
        scroll_counter = 0
        max_scrolls = 10
        while scroll_counter < max_scrolls:
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(7)
            new_height = driver.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                break
            else:
                last_height = new_height
            scroll_counter += 1
        last_height = driver.execute_script("return document.body.scrollHeight")
        scroll_counter = 0
        max_scrolls = 10
        while scroll_counter < max_scrolls:
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(7)
            new_height = driver.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                break
            else:
                last_height = new_height
            scroll_counter += 1
        last_height = driver.execute_script("return document.body.scrollHeight")
        scroll_counter = 0
        max_scrolls = 10
        while scroll_counter < max_scrolls:
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(7)
            new_height = driver.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                break
            else:
                last_height = new_height
            scroll_counter += 1
        last_height = driver.execute_script("return document.body.scrollHeight")
        scroll_counter = 0
        max_scrolls = 10
        while scroll_counter < max_scrolls:
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(7)
            new_height = driver.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                break
            else:
                last_height = new_height
            scroll_counter += 1

        items = driver.find_elements(By.CLASS_NAME, 'col-xs-12.col-md-8')
        for item in items:
            item_name = item.find_element(By.CLASS_NAME, 'catalog-item-name')
            Names.append(item_name.text)
            try:
                props = item.find_element(By.CSS_SELECTOR, 'ul.ng-scope')
                types = props.find_element(By.CSS_SELECTOR, 'a.ng-binding')
                Types.append(types.text)
            except:
                Types.append('0')
            try:
                brandes = props.find_element(By.CSS_SELECTOR, 'span.ng-scope')
                Brandes.append(brandes.text)
            except:
                Brandes.append('0')
            try:
                serieses = props.find_elements(By.CSS_SELECTOR, 'a.ng-binding')[2]
                Serieses.append(serieses.text)
            except:
                Serieses.append('0')
            try:
                scales = props.find_elements(By.CSS_SELECTOR, 'li.ng-scope')[2]

                if "Scale" in scales.text:
                    text = scales.text
                    key, value = text.split(": ")
                    Scales.append(value)
                else:
                    Scales.append('0')

                if "Production Status" in scales.text:
                    text = scales.text
                    key, value = text.split(": ")
                    Status.append(value)
                else:
                    Status.append('0')
            except:
                Scales.append('0')
            try:
                status = props.find_elements(By.CSS_SELECTOR, 'li.ng-scope')[3]
                if "Production Status" in status.text:
                    text = status.text
                    key, value = text.split(": ")
                    Status_2.append(value)
                else:
                    Status_2.append('0')

            except:
                Status_2.append('0')
            try:
                prices = item.find_element(By.CLASS_NAME, 'price-guide.col-md-3.col-xs-6')
                text_parts = prices.text.split("\n")
                estimated_value = text_parts[0]
                value = text_parts[1]
                Prices.append(value)
            except:
                Prices.append('0')
            try:
                ratings = item.find_element(By.CLASS_NAME, 'rating-guide')
                text_parts = ratings.text.split("\n")
                Member_Rated = text_parts[0]
                Rated = text_parts[1]
                Ratings.append(Rated)
            except:
                Ratings.append('0')

            for j in range(len(Status)):
                if Status[j] != '0':
                    Final_Status.append(Status[j])
                else:
                    Final_Status.append(Status_2[j])
        for_data_base += len(items)
        #driver.switch_to.window(driver.window_handles[+1])
        #items = driver.find_elements(By.CLASS_NAME, 'col-xs-12.col-md-8')
        #for item in items:
        #    item_name = item.find_element(By.CLASS_NAME, 'catalog-item-name')
        #    Names.append(item_name.text)
        time.sleep(7)
        driver.switch_to.window(driver.window_handles[1])
        i += 1

    print(Names)
    print(Types)
    print(Brandes)
    print(Serieses)
    print(Scales)
    print(Prices)
    print(Ratings)
    print(Final_Status)

    data = [['Name ','Type ','Brand ', 'Series ', 'Scale ', 'Status ', 'Rating ', 'Price ']]
    data_2 = [Names, Types ,Brandes, Serieses, Scales, Final_Status, Ratings, Prices]
    file_path = 'C:/Users/Asus/pythonProject3/Data_Base.csv'
    try:
        with open(file_path, mode='w', newline='') as csv_file:
            csv_writer = csv.writer(csv_file)
            for row in data:
                csv_writer.writerow(row)
            for k in range(for_data_base):
                try:
                    data_2 =[Names[k], Types[k], Brandes[k], Serieses[k], Scales[k],
                             Final_Status[k], Ratings[k], Prices[k]]
                    csv_writer.writerow(data_2)
                except:
                    continue
    except IOError:
        print("Error creating file or taking permissions")
    else:
        print("Data written successfully")
    finally:
        csv_file.close()


driver = webdriver.Chrome('chromedriver.exe')
driver.get("https://www.ad.co.il/nadlanrent")
wait = WebDriverWait(driver, 7)

elements = driver.find_elements(By.CLASS_NAME, 'card-block.hovered')
for element in elements:
    features = element.find_element(By.CLASS_NAME, 'card-body p-md-3')
    for feature in features:
        names = feature.find_element(By.CLASS_NAME, 'card-title.mb-0.mb-sm-1')
        print(names.text)
driver.quit()