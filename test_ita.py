from selenium.webdriver import Chrome
from selenium.webdriver import ChromeOptions
from selenium.webdriver.support.ui import WebDriverWait       
from selenium.webdriver.common.by import By       
from selenium.webdriver.support import expected_conditions as EC, wait
import time

opcije = ChromeOptions()
opcije.add_argument("--log-level=3")
browser = Chrome(options=opcije)


def log_in_logout():
    browser.get("https://www.kupujemprodajem.com/")
    browser.save_screenshot("kp_pocetna.png")
    time.sleep(3)

    zatvori = browser.find_element_by_class_name("kpBoxCloseButton")
    zatvori.click()
    browser.save_screenshot("kp_box_.png")
    time.sleep(3)

    ulogujtese = browser.find_element_by_link_text("Ulogujte se")
    ulogujtese.click()
    browser.save_screenshot("kp_login.png")
    time.sleep(3)

    email = browser.find_element_by_id("email")
    password = browser.find_element_by_id("password")
    klik = browser.find_element_by_id("submitButton")
    time.sleep(3)

    email.click()
    email.send_keys("itilija2@gmail.com")
    password.click()
    password.send_keys("Miljevic2005")
    klik.click()
    browser.save_screenshot("kp_login_.png")
    time.sleep(3)

    browser.close()


# Postavljanje oglasa na sajt
def postavi_oglas():

    browser.get("https://www.kupujemprodajem.com/")
    browser.save_screenshot("kp_pocetna.png")
    time.sleep(3)

    zatvori = browser.find_element_by_class_name("kpBoxCloseButton")
    zatvori.click()
    browser.save_screenshot("kp_box_.png")
    time.sleep(3)

    ulogujtese = browser.find_element_by_link_text("Ulogujte se")
    ulogujtese.click()
    browser.save_screenshot("kp_login.png")
    time.sleep(3)

    email = browser.find_element_by_id("email")
    password = browser.find_element_by_id("password")
    klik = browser.find_element_by_id("submitButton")
    time.sleep(3)

    email.click()
    email.send_keys("itilija2@gmail.com")
    password.click()
    password.send_keys("Miljevic2005")
    klik.click()
    browser.save_screenshot("kp_login_.png")
    time.sleep(3)

    oglas = browser.find_element_by_xpath("//div[@class='noAdsButtonHolder']//a")
    browser.execute_script("arguments[0].click();", oglas)
    browser.save_screenshot("kp_postavi_oglas_.png")
    time.sleep(3)

    naziv_oglasa = browser.find_element_by_id("data[group_suggest_text]")
    naziv_oglasa.click()
    naziv_oglasa.send_keys("iPhone 13 Pro Max")
    browser.save_screenshot("kp_new_.png")
    time.sleep(3)

    dugme = browser.find_element_by_css_selector('[value="Predloži gde"]')
    dugme.click()
    browser.save_screenshot("kp_predlozi_.png")
    time.sleep(3)

    element =browser.find_element_by_xpath("//span[text()='Apple iPhone']")
    element.click()
    element.click()
    browser.save_screenshot("kp_izabrano_.png")
    time.sleep(3)

    stanje = browser.find_element_by_id("data[condition]as-new")
    stanje.click()
    time.sleep(3)

    cena = browser.find_element_by_id("price_number")
    cena.click()
    cena.send_keys("1200")
    time.sleep(3)

    valuta = browser.find_element_by_id("currency_eur")
    valuta.click()
    time.sleep(3)

    browser.switch_to.frame("data[description]_ifr")
    browser.find_element_by_id("tinymce").send_keys("Kao nov, poslati poruku za vise informacija!")
    browser.switch_to.parent_frame()
    browser.save_screenshot("kp_forma_.png")
    time.sleep(3)
    browser.implicitly_wait(10)

    sledeca = browser.find_element_by_xpath("//div[input/@action-name ='adInfoNextButton']")
    sledeca.click()
    time.sleep(3)

    promocija = browser.find_element_by_id("data[promo_type]none")
    promocija.click()
    browser.save_screenshot("kp_promocija_.png")
    time.sleep(3)

    sledeca2 = browser.find_element_by_xpath("//div[input/@action-name ='adPromoNextButton']")
    sledeca2.click()
    time.sleep(3)

    prihvatam = browser.find_element_by_id('accept_yes')
    prihvatam.click()
    time.sleep(3)

    postavi = browser.find_element_by_css_selector('[value="Postavite oglas"]')
    postavi.click()
    browser.save_screenshot("kp_postavi_.png")
    log_out = browser.find_element_by_link_text("Izlogujte se")
    log_out.click()
    time.sleep(3)

def ulazak_u_oglas_i_brisanje():

    browser.get("https://www.kupujemprodajem.com/")
    browser.save_screenshot("kp_pocetna.png")
    time.sleep(3)

    zatvori = browser.find_element_by_class_name("kpBoxCloseButton")
    zatvori.click()
    browser.save_screenshot("kp_box_.png")
    time.sleep(3)

    ulogujtese = browser.find_element_by_link_text("Ulogujte se")
    ulogujtese.click()
    browser.save_screenshot("kp_login.png")
    time.sleep(3)

    email = browser.find_element_by_id("email")
    password = browser.find_element_by_id("password")
    klik = browser.find_element_by_id("submitButton")
    time.sleep(3)

    email.click()
    email.send_keys("itilija2@gmail.com")
    password.click()
    password.send_keys("Miljevic2005")
    klik.click()
    browser.save_screenshot("kp_login_.png")
    time.sleep(3)
    moji_oglasi = browser.find_element_by_link_text("Moji oglasi")
    moji_oglasi.click()
    browser.save_screenshot("kp_oglasi.png")
    time.sleep(3)
    telefon = browser.find_element_by_link_text("iPhone 13 Pro Max")
    telefon.click()
    browser.save_screenshot("kp_oglas.png")
    brisanje = browser.find_element_by_link_text("Obriši")
    brisanje.click()
    browser.implicitly_wait(5)
    browser.save_screenshot("kp_brisanje.png")
    brisanje1 = browser.find_element_by_css_selector('[value="renew"]')
    brisanje1.click()
    browser.save_screenshot("kp_brisanje1.png")
    brisanje2 = browser.find_element_by_name("submit[delete]")
    brisanje2.click
    browser.save_screenshot("kp_brisanje2.png")
    time.sleep(3)
    
ulazak_u_oglas_i_brisanje()