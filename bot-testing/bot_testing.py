from selenium.common.exceptions import NoSuchElementException
from selenium import webdriver
#from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import random
import string
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import sys
sys.path.append('E:/Neuer Ordner/konstany study/winter 24.25/online survey/tutorial/seminar/online_survey/tavakol_5272/otree-example/survey_example_appfolder')
#from survey_example_appfolder.HelperFunctions import  detect_quota
#from .models import Constants, Player




# this is the session wide link
link = 'http://localhost:8000/join/babinopa'

def build_driver():
    # Set up the driver
    return webdriver.Chrome()


def check_exists_by_xpath(driver, xpath):
    try:
        x = driver.find_element(By.XPATH, xpath)
        if x.is_displayed():
            return True
    except Exception as e:
        print(f"Error on check exist: {e}")
    return False


def wait_for_element(driver, by, locator, timeout=10):
    print(f"Waiting for element: {locator}")
    return WebDriverWait(driver, timeout).until(EC.presence_of_element_located((by, locator)))


def welcome_page(driver):
    try:
        # permission
        entry_question_id = driver.find_element(By.ID, 'permission') 
        entry_question_id.send_keys("ok")
       # eligible
        eligible = driver.find_elements(By.NAME, 'eligible_question')
        if eligible:
            rand_selection = random.randint(0, len(eligible) - 1)
            eligible[rand_selection].click()

        if rand_selection == 2:  # Assuming `2` triggers screenout
            print("Participant screened out due to eligibility question.")
            return
        
        # next button
        next_button = wait_for_element(driver, By.XPATH, '//*[@id="form"]/div/button')
        next_button.click()
    except Exception as e:
        print(f"Error on the Welcome page: {e}")
        #driver.quit()



def demo_page(driver):
    try:
        
        # gender field
        gender = driver.find_elements(By.NAME, 'gender')
        if gender:
            rand_selection = random.randint(0, len(gender) - 1)
            gender[rand_selection].click()

        #age
        age_fill = wait_for_element(driver, By.XPATH, "//*[@id='id_age']")
        age = random.randint(1,110)
        age_fill.send_keys(str(age))
        if age > 40:
            print("Participant screened out due to age.")
            return
        #education
        academic_fill = driver.find_elements(By.NAME, 'Academic_status')
        if academic_fill:
            random.choice(academic_fill).click()
        #Marital field
        marital_fill = driver.find_elements(By.NAME, 'Marital_status')
        if marital_fill:
            random.choice(marital_fill).click()
        
        #income
        income_fill = driver.find_element(By.NAME, 'Monthly_income')
        income = random.randint(1, 20000)  
        income_fill.send_keys(str(income))

        #life_satisfaction
        satisfaction_fill = driver.find_element(By.NAME, 'life_satisfaction_score')
        satisfaction = random.randint(1, 100)  
        satisfaction_fill.send_keys(str(satisfaction))
        
        # next button
        next_button = wait_for_element(driver, By.XPATH, '//*[@id ="form"]/div/button')
        next_button.click()
    except Exception as e:
        print(f"Error on the Demo page: {e}")
        #driver.quit()
    
    
    
def onlyOneGroup(driver):
    #Find the element by its tag
    driver.find_element(By.TAG_NAME, 'button').click()

def popout_page(driver):
    try:

        # Select a random picture
        pic_options = driver.find_elements(By.NAME, 'pic')
        if pic_options:
            satis_pic = random.choice(pic_options)
            satis_pic.click()

            if satis_pic.get_attribute("value") == "pic-yes":
                reason = driver.find_element(By.XPATH, '//*[@id="divYes"]/input')
                reason.send_keys("I am satisfied")
            else:
                reason= driver.find_element(By.XPATH, '//*[@id="divNo"]/input')
                reason.send_keys("I am dissatisfied")

        # next button
        next_button = driver.find_element(By.XPATH, '//*[@id ="form"]/div/button')
        next_button.click()
    except Exception as e:
        print(f"Error on the popout page: {e}")
        driver.quit()
       

def end_page(driver):
    try:
        next_button = driver.find_element(By.XPATH, '//*[@id = "form"]/div/button')
        next_button.click()
    except Exception as e:
        print(f"Error on the end page: {e}")
        driver.quit()


def run_bots(no_times, link):
    for i in range(no_times):
        driver = build_driver()  # Initialize the driver
        try:
            driver.get(link)  # Open the survey URL
            
            # Welcome page
            if check_exists_by_xpath(driver, "//*[@id='id_permission']") == 1:
                welcome_page(driver)
            
            # Detect screenout after Welcome page
            if check_exists_by_xpath(driver, "//*[contains(text(), 'Screenout')]"):
                print("Participant screened out after Welcome page.")
                continue
            
            # Demo page
            demo_page(driver)
            
            # Detect quota redirect after Demo page
            if check_exists_by_xpath(driver, "//*[contains(text(), 'Quota Full')]"):
                print("Participant redirected due to full quota.")
                continue
            
            # Popout page
            popout_page(driver)
            
            # End page
            end_page(driver)
            print("complete successfully")
        
        except Exception as e:
              print(f"Error on the popout page: {e}")
        finally:
              driver.quit()  
    print("Success!")


run_bots(no_times=5, link=link)