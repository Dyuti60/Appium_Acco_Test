def get_android_caps():
    return {
        'platformName': 'Android',
        'automationName': 'UiAutomator2',
        'platformVersion': '11.0',
        'deviceName': 'Android Emulator',
        'app': '/path/to/your/app.apk',
        'appPackage': 'com.example.app',
        'appActivity': '.MainActivity',
        'noReset': True,
        'newCommandTimeout': 300
    }

def get_ios_caps():
    return {
        'platformName': 'iOS',
        'automationName': 'XCUITest',
        'platformVersion': '15.0',
        'deviceName': 'iPhone 13',
        'app': '/path/to/your/app.ipa',
        'bundleId': 'com.example.app',
        'noReset': True,
        'newCommandTimeout': 300
    }
