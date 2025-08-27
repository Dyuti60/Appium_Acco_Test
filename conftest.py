import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.options.ios import XCUITestOptions
from src.config.capabilities import get_android_caps, get_ios_caps

@pytest.fixture(scope='session')
def appium_service():
    """Start Appium service"""
    yield 'http://localhost:4723'

@pytest.fixture
def android_driver(appium_service):
    """Android driver fixture"""
    options = UiAutomator2Options()
    options.load_capabilities(get_android_caps())
    
    driver = webdriver.Remote(appium_service, options=options)
    yield driver
    driver.quit()

@pytest.fixture  
def ios_driver(appium_service):
    """iOS driver fixture"""
    options = XCUITestOptions()
    options.load_capabilities(get_ios_caps())
    
    driver = webdriver.Remote(appium_service, options=options)
    yield driver
    driver.quit()
