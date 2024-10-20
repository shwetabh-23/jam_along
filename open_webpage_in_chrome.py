from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager
import keyboard  # for detecting keypresses
from google_search import google_search

# Initialize the Chrome driver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

def get_website_content(val):
    wait = WebDriverWait(driver, 20)  # Increased timeout
    driver.get(val)

    # Wait for the page to load completely
    wait.until(lambda driver: driver.execute_script("return document.readyState") == "complete")

    print("Page loaded successfully!")
    # Keep the browser open until spacebar is pressed
    print("Press spacebar to close the browser.")
    # while True:
    #     if keyboard.is_pressed('space'):
    #         print("Spacebar pressed! Closing the browser...")
    #         break
    
    # Close the browser after spacebar is pressed
    # driver.quit()

def get_song_lyrics(song_name):
    websites = google_search(song_name + '' + 'lyrics')
    url = websites[0]
    get_website_content(url)

if __name__ == "__main__":
    websites = google_search('yuhin chala chal lyrics')
    url = websites[0]
    # url = "https://www.google.com"  # Replace with the website URL you want to open
    get_website_content(url)