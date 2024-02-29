
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from booking_steps import BookingSteps


driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

booking_steps = BookingSteps(driver)

# Run the tests
booking_steps.test_Browser()
booking_steps.test_searchBooking()
booking_steps.test_Calendar()
booking_steps.test_Search_Hotels()
booking_steps.test_Hotel_filters()
booking_steps.test_Hotel_details()
booking_steps.test_Hotel_ContactData()
