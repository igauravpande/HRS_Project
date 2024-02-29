from selenium.webdriver.support import expected_conditions as EC
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
import time

from selenium.webdriver.support.wait import WebDriverWait


class BookingSteps:
    def __init__(self, driver):
        self.driver = driver

        self.driver.implicitly_wait(10)

    def test_Browser(self):
        self.driver.get("https://www.hrs.com/")
        self.driver.maximize_window()
        # self.driver.delete_all_cookies()

    def test_searchBooking(self):
        try:

            search_destination = WebDriverWait(self.driver, 15).until(
                EC.element_to_be_clickable((By.XPATH, "//span[@title='Location, hotel, region, address, post code']"))
            )
            time.sleep(10)
            search_destination.click()

            search_destination_input = WebDriverWait(self.driver, 30).until(
                EC.visibility_of_element_located(
                    (By.XPATH, "//input[@id='DestinationSearchInput']"))
            )
            search_destination_input.send_keys("Barcelona")
            time.sleep(2)

            select_destination = self.driver.find_element(By.CSS_SELECTOR, "main[class='index_mainContainer__XY5Vr'] "
                                                                           "ul:nth-child(1) li:nth-child(2) "
                                                                           "div:nth-child(1)")
            time.sleep(2)
            select_destination.click()
            time.sleep(2)
        except NoSuchElementException as e:
            print("Element not found for Search Booking", e)

    def test_Calendar(self):
        try:
            add_arrivalDate = self.driver.find_element(By.XPATH, "//div[@class='DateRangeInputField_date__IAUhI']")
            add_arrivalDate.click()

            time.sleep(2)
            select_date = self.driver.find_element(By.XPATH, "//img[@alt='left']")
            select_date.click()

            time.sleep(2)
            select_date_1 = self.driver.find_element(By.XPATH, "(//img[@alt='left'])[2]")
            select_date_1.click()

            time.sleep(2)
            select_date_2 = self.driver.find_element(By.XPATH, "(//img[@alt='left'])[2]")
            select_date_2.click()

            time.sleep(2)
            select_date_3 = self.driver.find_element(By.XPATH, "(//img[@alt='left'])[2]")
            select_date_3.click()

            # June week days plan
            time.sleep(2)
            arrival_date = self.driver.find_element(By.XPATH, "//div[text()='21']")
            arrival_date.click()

            time.sleep(2)
            departure_date = self.driver.find_element(By.XPATH, "//div[text()='28']")
            departure_date.click()

        except NoSuchElementException as e:
            print("Element not found for adding Calendar dates", e)

    def test_Search_Hotels(self):
        try:
            time.sleep(3)
            search_button = self.driver.find_element(By.ID, 'SearchHotelsButton')
            search_button.click()
            time.sleep(20)

        except NoSuchElementException as e:
            print("Element not found for Search Hotels", e)

    def test_Hotel_filters(self):
        try:
            # scroll down to list
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

            # scroll up to list
            time.sleep(2)
            element = self.driver.find_element(By.XPATH, "//span[text()='Recommendations']")
            self.driver.execute_script("arguments[0].scrollIntoView();", element)

            time.sleep(2)
            select_price = self.driver.find_element(By.XPATH, "(//button[@type='button'])[8]")
            select_price.click()

            time.sleep(2)
            select_price_option = self.driver.find_element(By.XPATH, "(//div[@class='Row_row__RTK3K false'])[1]")
            select_price_option.click()

            time.sleep(2)
            select_distance = self.driver.find_element(By.XPATH, "(//button[@type='button'])[9]")
            select_distance.click()

            time.sleep(2)
            select_distance_option = self.driver.find_element(By.XPATH, "//span[text()='Destination']")
            select_distance_option.click()

            time.sleep(2)
            select_rating = self.driver.find_element(By.XPATH, "//span[text ()='Ratings']")
            select_rating.click()

            time.sleep(2)
            select_rating_option = self.driver.find_element(By.XPATH, "//span[text()='Business travelers']")
            select_rating_option.click()

        except NoSuchElementException as e:
            print("Element not found for Search filter Hotels", e)

    def test_Hotel_details(self):
        try:
            Hotel_details = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.ID, 'HotelDetailsButton_81992'))
            )
            Hotel_details.click()

            select_rooms = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.ID, 'SelectRoomButton'))
            )
            print("Select room clicked")
            select_rooms.click()

            time.sleep(2)
            # Scroll
            BookNow_Button = self.driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/main[1]/div[1]/div[4]/div[1]/div[4]/div[1]/div[2]/div[2]/div[1]/div[6]/div[1]/button[1]")
            self.driver.execute_script("arguments[0].scrollIntoView();", BookNow_Button)
            BookNow_Button.click()

        except NoSuchElementException as e:
            print("Element not found for Search filter Hotels", e)

    def test_Hotel_ContactData(self):
        try:
            time.sleep(2)
            Contact_FName = self.driver.find_element(By.ID, "given-name")
            Contact_FName.send_keys("John")

            time.sleep(2)
            Contact_LName = self.driver.find_element(By.ID, "family-name")
            Contact_LName.send_keys("Test")

            time.sleep(2)
            Country_code = self.driver.find_element(By.XPATH, "//span[text()='Spain (+34)']")
            Country_code.click()

            time.sleep(2)
            Phone_Num = self.driver.find_element(By.ID, "phone")
            Phone_Num.send_keys("8989898989")

            time.sleep(2)
            Email_ID = self.driver.find_element(By.ID, "phone")
            Email_ID.send_keys("johntest@gmail.com")

            time.sleep(2)
            Booking_button = self.driver.find_element(By.ID, "81992_bookBoxButton")
            Booking_button.click()

        except NoSuchElementException as e:
            print("Element not found for Complete Hotels Booking", e)
