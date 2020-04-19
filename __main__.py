import time

from secrets import passwd, user , cron_user , cron_pass
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import ui
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By


git_url = 'git repo url you want to clone' #change this
buildcommand = 'your custom build command for deployment' #change this
deploy_hook = ''

def main():
    #open ChromeDriver and login
    driver = webdriver.Chrome('directory where chromedriver is located its in the same folder as this file ') #change this
    driver.get('http://zeit.co/login')
    driver.find_element_by_xpath('//*[@id="__next"]/div/div/div[2]/div[1]/div[2]/div/div/div/button[1]').click();
    driver.find_element_by_xpath('//*[@id="login_field"]').send_keys(user)
    driver.find_element_by_xpath('//*[@id="password"]').send_keys(passwd)
    driver.find_element_by_xpath('//*[@id="login"]/form/div[3]/input[9]').click()
    time.sleep(3)

    try:
        driver.find_element_by_xpath('//*[@id="js-oauth-authorize-btn"]').click()
    except:
        print('No authorize button')
        
    #Import Project
    try:
        driver.find_element_by_xpath('//*[@id="__next"]/div/div/div[2]/div/div/div/div/div[1]/div/div/div/div/div[1]/span[1]/p/a').click()
    except:
        driver.find_element_by_xpath('//*[@id="__next"]/div/div/div[2]/div/header/div/span/a[2]/span').click()
        driver.find_element_by_xpath('//*[@id="__next"]/div/div/div/div/div/main/div/div/div/div[1]/div/div[2]/a').click()
        time.sleep(3)
        
    try:
        driver.find_element_by_xpath('//*[@id="__next"]/div/div/div/div/main/main/div[1]/div[2]/div[2]/div/div/button/span[2]').click()
        driver.find_element_by_xpath('//*[@id="js-pjax-container"]/div/div[2]/div/form/button').click()
        driver.find_element_by_xpath('//*[@id="__next"]/div/div/div/div/main/main/div[1]/div[2]/div[2]/div/div/button/span[2]').click()
        
      
    except:
       print('No install zeit button')
    try:
        time.sleep(3)
        driver.find_element_by_xpath('/html/body/reach-portal/div/div[2]/div/div[2]/div/div/div[2]/div/div/button').click()
        time.sleep(2)
        driver.find_element_by_xpath('(//*[text()="Import"])').click()
        time.sleep(10)
        driver.find_element_by_xpath('(//*[text()="Continue"])').click()
        driver.find_element_by_xpath('//*[@id="__next"]/div/div/div[2]/div/div/div/footer/div/div[2]/div/button').click()
        time.sleep(3)
        driver.find_element_by_xpath('//*[@id="__next"]/div/div/div[2]/div/div/div/div[3]/div[1]/div/input').send_keys(buildcommand)
        driver.find_element_by_xpath('(//*[text()="Deploy"])').click()
            
    except:
        print('project already imported')
        

    time.sleep(3)
    # Make Hook and Login to cronjob
    try:
        driver.find_element_by_xpath('//*[@id="__next"]/div/div/div[1]/nav/div/div/div/div[2]/a[3]').click()
        driver.find_element_by_xpath('//*[@id="__next"]/div/div/div[2]/div[2]/div/div[1]/div/a[3]').click()
        deploy_hook = driver.find_element_by_xpath('//*[@id="__next"]/div/div/div[2]/div[2]/div/div[2]/div[2]/div/div/div[2]/section/div/div/pre').text
        print(deploy_hook)
    except:   
        driver.find_element_by_xpath('//*[@id="__next"]/div/div/div[2]/div[2]/div/div[2]/div[2]/div/div/div[2]/form/div/div[1]/div/div/input').send_keys('mina')
        driver.find_element_by_xpath('//*[@id="__next"]/div/div/div[2]/div[2]/div/div[2]/div[2]/div/div/div[2]/form/div/div[2]/div/input').send_keys('master')
        time.sleep(3)
        driver.find_element_by_xpath('//*[@id="__next"]/div/div/div[2]/div[2]/div/div[2]/div[2]/div/div/div[2]/form/div/button/span').click()
        time.sleep(3)
        deploy_hook = driver.find_element_by_xpath('//*[@id="__next"]/div/div/div[2]/div[2]/div/div[2]/div[2]/div/div/div[2]/section/div/div/pre').text

    driver.execute_script("window.open('');")
    driver.switch_to.window(driver.window_handles[1])
    driver.get('https://cron-job.org/en/members/')
    driver.find_element_by_xpath('//*[@id="email"]').send_keys(cron_user)
    driver.find_element_by_xpath('//*[@id="pw"]').send_keys(cron_pass)
    driver.find_element_by_xpath('//*[@id="content"]/div/form/input[2]').click()
    driver.find_element_by_xpath('//*[@id="memberMenuLeft"]/a[2]').click()
    driver.find_element_by_xpath('//*[@id="content"]/button').click()
    driver.find_element_by_xpath('//*[@id="title"]').send_keys(user + ' cron')
    driver.find_element_by_xpath('//*[@id="url"]').clear()
    driver.find_element_by_xpath('//*[@id="url"]').send_keys(deploy_hook)
    driver.find_element_by_xpath('//*[@id="content"]/div/form/fieldset[3]/div[1]/select/option[6]').click()
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//input[@value=' Create cronjob ']"))).click()

    driver.exit()
    
if __name__ == "__main__":
    main()
