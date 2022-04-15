    # # kategoria kobiety
    # elem = browser.find_element(By.XPATH,'//section[@class="header-main-category-menu"]/ul/li/a[@title="Kobiety"]')
    # elem.click()


    # # odzież
    # wait.until(EC.visibility_of_element_located((By.XPATH,"//a[@title='ODZIEŻ']")))
    # element_to_hover_over = browser.find_element(By.XPATH,"//ul[@class='category-tree']//a[@title='ODZIEŻ']")

    # ActionChains(browser).move_to_element(element_to_hover_over).perform()  

    # # bluzki
    # wait.until(EC.visibility_of_element_located((By.XPATH,'//a[@title="Bluzki i koszule"]')))
    # elem = browser.find_element(By.XPATH,'//a[@title="Bluzki i koszule"]')
    # elem.click()

    # # fitr oferta
    # wait.until(EC.visibility_of_element_located((By.XPATH,"//span[text()='Oferta']")))
    # elem = browser.find_element(By.XPATH,"//span[text()='Oferta']")
    # elem.click()
    # # zawężenie nowość
    # wait.until(EC.visibility_of_element_located((By.XPATH,"//label/span[text()='Nowość']")))
    # elem = browser.find_element(By.XPATH,"//label/span[text()='Nowość']")
    # elem.click()

    # # potwierdzenie filtru
    # wait.until(EC.element_to_be_clickable((By.XPATH,"//button[@data-test-id='filters-apply-button'][not(@disabled)]")))
    # elem = browser.find_element(By.XPATH,"//button[@data-test-id='filters-apply-button'][not(@disabled)]")
    # elem.click()
   
    # wait.until(EC.url_to_be("https://modivo.pl/c/kobiety/odziez/bluzki-i-koszule/oferta:nowosc"))

    # # fitr rozmiar
    # wait.until(EC.visibility_of_element_located((By.XPATH,"//span[text()='Rozmiar']")))
    # elem = browser.find_element(By.XPATH,"//span[text()='Rozmiar']")
    # elem.click()
    
    # # zawężenie kobiety
    # elem = browser.find_element(By.XPATH,"//div[@data-test-id='filters-size-category-damskie'][not(@disabled)]")
    # elem.click()

    # # zwężenie góra
    # wait.until(EC.visibility_of_element_located((By.XPATH,"//div[@data-test-id='filters-size-category-item-damskie_gorne_czesci_garderoby'][not(@disabled)]")))
    # elem = browser.find_element(By.XPATH,"//div[@data-test-id='filters-size-category-item-damskie_gorne_czesci_garderoby'][not(@disabled)]")
    # elem.click()

    # # rozmiar ostateczny
    # wait.until(EC.visibility_of_element_located((By.XPATH,"//div[./input[@data-test-id='checkbox-38']]/label")))
    # elem = browser.find_element(By.XPATH,"//div[./input[@data-test-id='checkbox-38']]/label")
    # elem.click()
    # wait.until(EC.element_located_to_be_selected((By.XPATH,"//input[@data-test-id='checkbox-38']")))

    # # potwierdzenie filtru
    # elem = wait.until(EC.element_to_be_clickable((By.XPATH,"//button[@data-test-id='filters-apply-button'][not(@disabled)]")))
    # elem.click()