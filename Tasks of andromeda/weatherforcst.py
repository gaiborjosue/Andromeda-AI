from selenium import webdriver

# if using chrome
driver = webdriver.Chrome()

# uncomment if using Firefox
# driver = webdriver.Firefox()

# Replace space from - For example new-york.
city = str(input("Enter the name of the city you want the weather forecast for: ")).replace(" ","-")

try:
    driver.get("https://www.weather-forecast.com/locations/"+city+"/forecasts/latest")
    print(driver.find_elements_by_class_name("b-forecast__table-description-content")[0].text)
except:
    print("Something went wrong")