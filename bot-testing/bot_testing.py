from selenium.common.exceptions import NoSuchElementException
from selenium import webdriver
#from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import random
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC





# this is the session wide link
link = 'http://localhost:8000/join/vinibevo'

def build_driver():
    # Set up the driver
    return webdriver.Chrome()


def check_exists_by_xpath(driver, xpath):
    try:
        x = driver.find_element(By.XPATH, xpath)
        return x.is_displayed()
        
    except NoSuchElementException:
        return False


def wait_for_element(driver, by, locator, timeout=7):
    print(f"Waiting for element: {locator}")
    return WebDriverWait(driver, timeout).until(EC.presence_of_element_located((by, locator)))


def welcome_page(driver):
    try:
        # permission
        entry_question_id = driver.find_element(By.NAME, 'permission') 
        entry_question_id.send_keys("ok")
       # eligible
        eligible = driver.find_elements(By.NAME, 'eligible_question')
        if eligible:
            rand_selection = random.randint(0, len(eligible) - 1)
            eligible[rand_selection].click()

            if eligible[rand_selection].get_attribute("value") == "2":
               print("screened-eligibility question.")
               return False

        
        # next button
        next_button = wait_for_element(driver, By.XPATH, '//*[@id="form"]/div/button')
        next_button.click()
        return True

    except Exception as e:
        print(f"Error on the Welcome page: {e}")
        return False
        #driver.quit()



def demo_page(driver):
    try:
        
        # gender
        gender = driver.find_elements(By.NAME, 'gender')
        if gender:
            selected_gender = random.choice(gender)
            selected_gender.click()

        #age
        age_fill = wait_for_element(driver, By.XPATH, "//*[@id='id_age']")
        age = random.randint(1,110)
        age_fill.send_keys(str(age))
        if age > 40:
            print("Participant screened out due to age.")
            return False

        #education
        academic = driver.find_elements(By.NAME, 'Academic_status')
        if academic:
            selected_education = random.choice(academic)
            selected_education.click()
        #Marital field
        marital = driver.find_elements(By.NAME, 'Marital_status')
        if marital:
            selected_marital = random.choice(marital)
            selected_marital.click()
        
        #income
        income_fill = driver.find_element(By.NAME, 'Monthly_income')
        income = random.randint(1, 20000)  
        income_fill.send_keys(str(income))

        #life_satisfaction
        satisfaction_fill = driver.find_element(By.NAME, 'life_satisfaction_score')
        satisfaction = random.randint(1, 100)  
        satisfaction_fill.send_keys(str(satisfaction))
        
        # next button
        next_button = wait_for_element(driver, By.XPATH, '//*[@id="form"]/div/button')
        next_button.click()
        return True
    except Exception as e:
        print(f"Error on the Demo page: {e}")
        return False
        #driver.quit()
    
    
    
#def onlyOneGroup(driver):
    
    #driver.find_element(By.TAG_NAME, 'button').click()

def popout_page(driver):
    try:
        pic_options = driver.find_elements(By.NAME, 'pic')
        if pic_options:
            selected_pic = random.choice(pic_options)
            selected_pic.click()

            if selected_pic.get_attribute("value") == "pic-yes":
                text_input = driver.find_element(By.XPATH, '//*[@id="picYes"]')
                text_input.send_keys("Excellent. What is the most important factor affecting your life satisfaction?")
            else:
                text_input= driver.find_element(By.XPATH, '//*[@id="picNo"]')
                text_input.send_keys("Excellent. What is the most important factor affecting your life dissatisfaction?")

        # next button
        #next_button = driver.find_element(By.XPATH, '//*[@id ="form"]/div/button')
        next_button = wait_for_element(driver, By.XPATH, '//*[@id="form"]/div/button')
        next_button.click()
        return True
    except Exception as e:
        print(f"Error on the popout page: {e}")
        return False
        #driver.quit()
       

def end_page(driver):
    try:
        #next_button = driver.find_element(By.XPATH, '//*[@id = "form"]/div/button')
        next_button = wait_for_element(driver, By.XPATH, '//*[@id="form"]/div/button')
        next_button.click()
    except Exception as e:
        print(f"Error on the end page: {e}")
        #driver.quit()


def run_bots(no_times, link):
    driver = None
    try:
        driver = build_driver()
        for i in range(no_times):
            driver.get(link)  # Open the survey URL

            if not welcome_page(driver):
                continue

            if not demo_page(driver):
                continue

            if not popout_page(driver):
                continue

            end_page(driver)

        print("Bot completed successfully.")
    
    except Exception as e:
        print(f"Error :execution: {e}")

    finally:
        if driver:
            try:
                driver.quit()
            except Exception as e:
                print(f"Error: driver.quit: {e}")

run_bots(no_times=20, link=link)