import sys
sys.path.append('../../../../../Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/site-packages/')
import os
import configparser
import traceback
from selenium import common
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


config_file = os.path.join(os.getcwd(), 'config.ini')

def read_config_limit(config_file):
    config = configparser.ConfigParser()
    config.read(config_file)

    # contribution limit
    con_limit = config['TFSA']['limit']
    return con_limit


def read_config(config_file, site):
    config = configparser.ConfigParser()
    config.read(config_file)

    # url of the sign in page
    url = config[site]['url']
    # xPath of the 'account/email' field
    acct_path = config[site]['acct_path']
    # xPath of the 'password' field
    pw_path = config[site]['pw_path']
    # your 'account name/email address' field
    acct_value = config[site]['acct_value']
    # your 'password'
    pw_value = config[site]['pw_value']
    # True/False for need authentication
    authen = config[site]['authen']
    # xPath of 'need for authentication' button
    authen_page = config[site]['authen_page']
    # xPath of the 'balance'
    value_path = config[site]['valuepath']
    # xPath of the 'authentication code' field
    authen_code = config[site]['authen_code']
    # xpath of the 'send authentication code' button
    authen_send = config[site]['authen_send']

    # file path to the webdriver
    browser_loc = config['browser']['location']
    return {
            'site': site,
            'url': url,
            'acct_value': acct_value,
            'pw_value': pw_value,
            'acct_path': acct_path,
            'pw_path': pw_path,
            'authen': authen,
            'authen_page': authen_page,
            'authen_code': authen_code,
            'authen_send': authen_send,
            'valuepath': value_path,
            'browser_loc': browser_loc}


def browser_interact(config):
    try:
        browser = webdriver.Chrome(ChromeDriverManager().install())
        browser.get(config['url'])
        browser.implicitly_wait(10)
        email_add = browser.find_element_by_xpath(config['acct_path'])
        email_add.send_keys(config['acct_value'])
        pw = browser.find_element_by_xpath(config['pw_path'])
        pw.send_keys(config['pw_value'])
        pw.send_keys(Keys.RETURN)
        if config['authen'] == 'True':
            if len(browser.find_elements(By.XPATH, config['authen_page'])) != 0:
                if config['site'] == 'ws':
                    # Need authentication for Wealth Simple
                    print("##### Check email for authentication code... ")
                    authen_code = browser.find_element_by_xpath(config['authen_code'])
                    authen_code.send_keys(input("Enter authentication code: "))
                    submit = browser.find_element_by_xpath(config['authen_send'])
                    submit.click()
                elif config['site'] == 'qst':
                # Need authentication for Questrade
                    print("##### Check text message for authentication code... ")
                    send_code = browser.find_element_by_xpath(config['authen_page'])
                    send_code.click()
                    authen_code = browser.find_element_by_xpath(config['authen_code'])
                    authen_code.send_keys(input("Enter authentication code: "))
                    verify = browser.find_element_by_xpath(config['authen_send'])
                    verify.click()

        # wait for 10s
        browser.implicitly_wait(10)
        acct_value = browser.find_element_by_xpath(config['valuepath'])
        balance = ''
        for num in acct_value.text[1:]:
            if num != ',':
                balance += num
        balance_result = float(balance)
        return balance_result
    except common.exceptions.NoSuchElementException:
        print(traceback.format_exc())
    except common.exceptions.ElementNotInteractableException:
        print(traceback.format_exc())
    finally:
        browser.quit()


def get_limit():
    limit = read_config_limit(config_file)
    return limit


def get_balance(site):
    # read from config to get url, account_name, password
    config = read_config(config_file, site)
    # get balance
    balance = browser_interact(config)
    return balance


if __name__ == '__main__':
    print(get_balance('qst'))
