from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time

print('Welcome to Tpot-tcg auto collect')

driver = webdriver.Chrome()
driver.get("https://tpot-tcg.com/login.html")
driver.set_window_size(800,600)

# Register / Login // Need to implement error handling iff incorrect username/passsword
def login():
    a = input('Do you have an account?(y/n): ')

    login_username = input('What is your username: ')
    login_password = input('What is your password: ')

    time.sleep(2)
    username = driver.find_element(By.ID, "username")
    password = driver.find_element(By.ID, "password")

    username.send_keys(f'{login_username}')
    time.sleep(1)
    password.send_keys(f'{login_password}')
    time.sleep(1)
    
    if a == 'y':
        login = driver.find_element(By.ID, "login-button")
        login.click()
        time.sleep(2)
        print('You have been logged in')
    
    elif a == 'n':
        register = driver.find_element(By.ID, "register-button")
        register.click()
        time.sleep(2)
        print('Congrats you are registered!')

    else:
        print("Invalid input enter 'y" or 'n')

# Check Balance
def check_balance():
    balance_element = driver.find_element(By.ID, "balance")
    balance_text = balance_element.text
    dollar_amount = balance_text.replace('$', '')
    balance = float(dollar_amount)
    print(f'Your balance is: ${balance}')

# Check how many times to auto click
def get_runtime():
    while True:    
        runtime = input('How many times would you like to collect?: ')
        try:
            runtime = int(runtime)
            if runtime > 0:
                return runtime
            else:
                print("Please enter a postive number")
        
        except ValueError:
            print("Invalid Input")

# autoclick x amount of time
def auto_collect(num_clicks):
    wait = WebDriverWait(driver, 10) # Wait up to 10 seconds for elements to be clickable
    collect_button = wait.until(EC.element_to_be_clickable((By.ID,  "teapot-clickable")))
    
    for i in range(num_clicks):
        try:
            collect_button.click()
            print(f'Collection {i+1} completed')
            time.sleep(102)
        except Exception as e:
            print(f"Error on collection {i+1}: {str(e)}")
    
    print(f"Completed {num_clicks} collections")

if __name__ == "__main__":
    login()
    time.sleep(2)

    initial_balance = check_balance()

    num_collections = get_runtime()

    auto_collect(num_collections)

    final_balance = check_balance()

    print(f"Initial Balance: ${initial_balance}")
    print(f"Final balance: ${final_balance}")
    print(f"Total earned: ${final_balance - initial_balance}")

    driver.quit