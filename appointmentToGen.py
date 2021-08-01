import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
from win10toast import ToastNotifier
import emailAlert as EA
from datetime import datetime


ChromePath = "C:\\Program Files (x86)\\chromeDriver.exe" # Need to download chromeDriver from selenium's website
chrome_options = Options()
# chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-gpu")

# This url is for Dr Eytan in Maccabi
url = "https://serguide.maccabi4u.co.il/heb/doctors/doctorssearchresults/doctorsinfopage/?ItemKeyIndex" \
      "=07A84FD6B9055C8460995CA9E9A5B4A6C44AEEBF93BCBA6C560940F038DE0184&RequestId=25e9a718-c267-8b05-584e" \
      "-daa37be8c0de&Source=SearchPageResults "
# TODO: Put the email you would like to notify here
email_address = "YourEmail@gmail.com"
tryNum = 1

currDate = ""
currDate_date = None

ans = input("Do you have an appointment? (y/n)\n")
if ans == "y" or ans == "Y":
    currDate = input("Enter your appointment date (d/m/Y)\n")
    currDate_date = datetime.strptime(currDate, '%d/%m/%Y')


while True:
    print("Try number %d\n" % tryNum)
    tryNum += 1
    driver = webdriver.Chrome(ChromePath, options=chrome_options)
    driver.get(url)
    details = driver.find_elements_by_class_name("contactDetailsAns")
    # for el in details:
    #     print(el.text)
    availableDate = details[3].text
    availableDate_date = datetime.strptime(availableDate, '%d/%m/%Y')
    if currDate == "":
        currDate = availableDate
        currDate_date = datetime.strptime(currDate, '%d/%m/%Y')
        print(currDate)
        driver.quit()

    if availableDate_date < currDate_date:
        currDate = availableDate
        currDate_date = availableDate_date
        now_date = datetime.now()
        toast = ToastNotifier()
        toast.show_toast("New Available for DR Eytan", currDate, duration=30)
        try:
            EA.email_alert("New Available for DR Eytan", f"Dr Eytan will be available at {currDate_date.strftime('%A')} {currDate}\n"
                                                         f"Its {(currDate_date - now_date).days+1} days from now.\n"
                                                         f"Try to make an appointment with this link:\n"
                                                         f"https://visit.maccabi4u.co.il/AppointmentsOrder/DanaInfo=.avjulxEshklkmuF8Os5R15+OrderCheckPatientEligibleForService.aspx?DoctorID=9B27E7672BF1A469F1CBDEE1BF656B98&FacilityId=77279&JobId=1&linkType=3&Service=1"
                                                         , email_address)
            print("email sent")
        except Exception as e:
            print("Didn't send mail\n", e)
        driver.quit()
    time.sleep(300)
