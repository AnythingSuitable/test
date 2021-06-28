from selenium import webdriver
import time
import os
#from LocList import Return_Different_Locations

CLICKS = 0
FAILS = 0

url = 'https://ouo.io/g5XEuw'
print(f'Hitting : {url}\n')

def Hit_Clicks(url):

	#RandomLocation = Return_Different_Locations()
	#os.system(f'sudo windscribe connect {RandomLocation} > demo.txt')

	chrome_options = webdriver.ChromeOptions()
	chrome_options.add_argument('--no-sandbox')
	chrome_options.add_argument("--incognito")
	chrome_options.add_argument('--headless')
	
	chrome_options.add_argument('--disable-dev-shm-usage')
	chrome_options.add_argument("--disable-notifications")

	driver = webdriver.Chrome(options=chrome_options)
	driver.get(url)

	main_window = driver.current_window_handle

	time.sleep(5) 

	driver.find_element_by_css_selector('.btn.btn-main').click()
	  
	try:
		windows = driver.window_handles
		driver.switch_to.window(windows[1])

		time.sleep(2)

		# Close current window
		driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + 'w')

		# Put focus back on main window
		driver.switch_to.window(main_window)
		time.sleep(2)

	except Exception as e:
		time.sleep(4)

	driver.find_element_by_css_selector('.btn.btn-main').click()
	driver.switch_to.window(main_window)
	time.sleep(1)

	if driver.title == 'lag3rl0f Reserved': pass

	else:

		try:
			driver.switch_to.window(main_window)
			driver.find_element_by_css_selector('.btn.btn-main').click()
			driver.switch_to.window(main_window)
			time.sleep(2)

		except Exception as e:

			Hit_Clicks(url)
			return False
	driver.quit()
	time.sleep(1)
	return True

while True:

	try:

		print(f'Hits Done : {CLICKS}, Failed : {FAILS}', end='\r')
		try:
			CURRENT_STAT = Hit_Clicks(url)

		except Exception as e:
			CURRENT_STAT = False

		if CURRENT_STAT == True:
			CLICKS = CLICKS +1
		else:
			FAILS = FAILS + 1

	except KeyboardInterrupt:

		print(f'Total Hits Done : {CLICKS}')
		#os.system('sudo windscribe disconnect > demo.txt')
		exit()
