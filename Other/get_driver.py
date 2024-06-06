from selenium.webdriver.firefox.options import Options
from selenium import webdriver
import undetected_chromedriver as uc
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options


def new_Chrome_DR():
    chrome_options = uc.ChromeOptions()
    caps = DesiredCapabilities().CHROME
    caps["pageLoadStrategy"] = "eager"  # normal - full_load
    chrome_options.add_argument("--single-process")
    chrome_options.headless = False
    driver = uc.Chrome(options=chrome_options, desired_capabilities=caps)
    return driver


def new_FireFox_DR():
    firefox_profile = webdriver.FirefoxProfile()
    caps = DesiredCapabilities().FIREFOX
    options = Options()
    options.binary_location = r'c:\Program Files\Mozilla Firefox\firefox.exe'
    # options.add_argument("-headless")
    options.set_capability('cloud:options', caps)
    firefox_profile.set_preference('permissions.default.image', 2)
    firefox_profile.set_preference('dom.ipc.plugins.enabled.libflashplayer.so', 'false')
    options.profile = firefox_profile
    driver = webdriver.Firefox(options=options)
    return driver


def new_Brave_DR():
    brave_path = "C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe"
    chromedriver_path = "d:/python/chromedriver"

    chrome_options = uc.ChromeOptions()
    chrome_options.binary_location = brave_path
    caps = DesiredCapabilities().CHROME
    caps["pageLoadStrategy"] = "eager"  # normal - full_load
    chrome_options.add_argument("--single-process")
    chrome_options.headless = False
    service = Service(chromedriver_path)
    driver = uc.Chrome(service=service, options=chrome_options, desired_capabilities=caps)
    return driver
