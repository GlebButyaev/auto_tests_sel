from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import time
from selenium.webdriver.common.action_chains import ActionChains


# Настройка драйвера
options = Options()
options.add_argument("--start-maximized")
options.add_argument("--disable-webrtc")
options.add_argument("--disable-dns-prefetch")
options.add_argument("--disable-gpu")
options.add_argument("--disable-software-rasterizer")
service = Service(r"C:\\chromedriver-win64\\chromedriver.exe")

report_file = "report.txt"

# Создание или очистка файла отчёта
def initialize_report():
    with open(report_file, "w", encoding="utf-8") as f:
        f.write("Отчёт выполнения тестов:\n\n")

def write_to_report(test_case, name_case, result):
    """Функция для записи результата в отчёт."""
    with open(report_file, "a", encoding="utf-8") as f:
        f.write(f"Тест кейс #{test_case} - {name_case}: {result}\n")

def login():
    """Тест кейс #1: Логирование."""
    try:
        # Открытие страницы
        driver.get("https://sandbox.rightech.io/auth?")

        # Ввод логина
        login_field = WebDriverWait(driver, 100).until(
            EC.presence_of_element_located((By.ID, "login"))
        )
        login_field.send_keys("убрал")

        # Ввод пароля
        password_field = WebDriverWait(driver, 100).until(
            EC.presence_of_element_located((By.ID, "password"))
        )
        password = os.getenv("PASSWORD", "убрал")
        password_field.send_keys(password)

        # Нажатие кнопки "Войти"
        login_button = WebDriverWait(driver, 100).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']"))
        )
        login_button.click()

        # Закрытие всплывающего окна
        close_button = WebDriverWait(driver, 100).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button.ric-btn.ric-btn-wicon.index__WindowClose___1GT-V"))
        )
        close_button.click()

        write_to_report(1, "Логирование", "ОК")
        print("Успешный вход!")
    except Exception as e:
        write_to_report(1, "Логирование", f"Ошибка: {str(e)}")
        raise

def create_model():
    """Тест кейс #2: Создание модели."""
    try:

        # Шаг 2: Переход в раздел "Модели"
        models_section = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "li.ric-main-nav-item[data-module='models-v3']"))
        )
        models_section.click()
        print("Шаг 2: Перешли в раздел 'Модели' успешно!")

        # Шаг 3: Нажатие на кнопку "Плюс"
        plus_button = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, "(//button[@class='ric-module-create-item'])[1]"))
        )
        plus_button.click()
        print("Шаг 3: Нажали на кнопку 'Плюс' успешно!")

        # Шаг 4: Нажатие на кнопку "Создать модель по протоколу"
        create_model_button = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable(
                (By.XPATH, "//div[@class='WizardPage__method___1jmSj']//button[normalize-space(text())='Создать модель по протоколу']")
            )
        )
        create_model_button.click()
        print("Шаг 4: Нажали на кнопку 'Создать модель по протоколу' успешно!")

        # Шаг 5: Нажатие на кнопку "MQTT"
        mqtt_button = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, "//div[@class='GridSelect__itemLabel___1YAVc' and text()='MQTT']"))
        )
        mqtt_button.click()
        print("Шаг 5: Нажали на кнопку 'MQTT' успешно!")

        # Шаг 6: Нажатие на кнопку "Далее"
        next_button = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'WizardPage__btn___2Qvt-') and .//span[text()='Далее']]"))
        )
        next_button.click()
        print("Шаг 6: Нажали на кнопку 'Далее' успешно!")

        # Шаг 7: Нажатие на кнопку "Создать"
        create_button = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'WizardPage__btn___2Qvt-') and text()='Создать']"))
        )
        create_button.click()
        print("Шаг 7: Нажали на кнопку 'Создать' успешно!")

        # Запись в отчёт об успешном выполнении
        write_to_report(2, "Создание модели", "ОК")
        print("Тест кейс #2 - Создание модели: Успешно")
    except Exception as e:
        # Запись в отчёт об ошибке
        write_to_report(2, "Создание модели", f"Ошибка: {str(e)}")
        print(f"Тест кейс #2 - Создание модели: Ошибка: {str(e)}")
        raise


def create_object_in_objects_section():
    """Тест кейс #4: Создание объекта через интерфейс."""
    try:
        # Шаг 1: Переход в раздел "Объекты"
        objects_section = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "li.ric-main-nav-item[data-module='objects']"))
        )
        objects_section.click()
        print("Шаг 1: Перешли в раздел 'Объекты' успешно!")

        # Шаг 2: Нажатие на кнопку '+'
        plus_button = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, "(//button[@class='ric-module-create-item'])[2]"))
        )
        print("Кнопка '+' найдена и кликабельна.")
        plus_button.click()
        print("Шаг 2: Нажали на кнопку '+' успешно!")

        # Шаг 3: Нажатие на кнопку "Сохранить"
        save_button = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@title='Сохранить']"))
        )
        save_button.click()
        print("Шаг 3: Нажали на кнопку 'Сохранить' успешно!")

        # Запись в отчёт об успешном выполнении
        write_to_report(4, "Создание объекта через интерфейс", "ОК")
        print("Тест кейс #4 - Создание объекта через интерфейс: Успешно")
    except Exception as e:
        # Запись в отчёт об ошибке
        write_to_report(4, "Создание объекта через интерфейс", f"Ошибка: {str(e)}")
        print(f"Тест кейс #4 - Создание объекта через интерфейс: Ошибка: {str(e)}")
        raise




def del_obj():
    """Тест кейс #5: Наведение на элемент и открытие выпадающего списка."""
    try:
        # Шаг 1: Найти родительский контейнер, где находятся "три точки"
        parent_container = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "#ric-navigation-objects-tab > div:nth-child(4) > div:nth-child(5) > div > div > div > div > div:nth-child(1) > div:nth-child(1)"))
        )
        
        # Шаг 2: Навести мышку на родительский контейнер
        actions = ActionChains(driver)
        actions.move_to_element(parent_container).perform()
        print("Наведение на родительский контейнер выполнено успешно.")

        # Шаг 3: Найти кнопку "три точки" и кликнуть по ней
        dots_button = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "#ric-navigation-objects-tab > div:nth-child(4) > div:nth-child(5) > div > div > div > div > div:nth-child(1) > div:nth-child(1) > button"))
        )
        dots_button.click()
        print("Клик по 'трем точкам' выполнен успешно.")

        # Шаг 4: Дождаться появления кнопки "Удалить"
        delete_button = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@role='menuitem' and contains(text(),'Удалить')]"))
        )

        # Шаг 5: Кликнуть по кнопке "Удалить"
        delete_button.click()
        print("Клик по кнопке 'Удалить' выполнен успешно.")


        # Шаг 6: Дождаться появления кнопки "Выполнить"
        execute_button = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@title='Выполнить']"))
        )

        # Шаг 7: Кликнуть по кнопке "Выполнить"
        execute_button.click()
        print("Клик по кнопке 'Выполнить' выполнен успешно.")

        # Запись в отчёт об успешном выполнении
        write_to_report(5, "Наведение и открытие выпадающего списка", "ОК")
        print("Тест кейс #5 - Наведение и открытие выпадающего списка: Успешно")
    except Exception as e:
        # Запись в отчёт об ошибке
        write_to_report(5, "Наведение и открытие выпадающего списка", f"Ошибка: {str(e)}")
        print(f"Тест кейс #5 - Наведение и открытие выпадающего списка: Ошибка: {str(e)}")
        raise


def navigate_to_logic_and_create():
    """Тест кейс #6: Переход на вкладку 'Логика', нажатие на '+' и создание сущности."""
    try:
        # Шаг 1: Переход на вкладку "Логика"
        logic_section = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "li.ric-main-nav-item[data-module='logic-v2']"))
        )
        logic_section.click()
        print("Шаг 1: Перешли на вкладку 'Логика' успешно!")

        # Шаг 2: Нажатие на кнопку '+', которая находится под номером 3
        plus_button = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, "(//button[@class='ric-module-create-item'])[3]"))
        )
        plus_button.click()
        print("Шаг 2: Нажали на кнопку '+' под номером 3 успешно!")

        # Шаг 3: Нажатие на кнопку "Создать"
        create_button = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, "//div[contains(@class, 'index__asyncButtonContent___brdE2') and .//span[text()='Создать']]"))
        )
        create_button.click()
        print("Шаг 3: Нажали на кнопку 'Создать' успешно!")

        # Запись в отчёт об успешном выполнении
        write_to_report(6, "Создание сущности в разделе 'Логика'", "ОК")
        print("Тест кейс #6 - Создание сущности в разделе 'Логика': Успешно")
    except Exception as e:
        # Запись в отчёт об ошибке
        write_to_report(6, "Создание сущности в разделе 'Логика'", f"Ошибка: {str(e)}")
        print(f"Тест кейс #6 - Создание сущности в разделе 'Логика': Ошибка: {str(e)}")
        raise



def del_log():
    """Тест кейс: Нажатие на три точки для автомата и удаление через выпадающее меню."""
    try:
        # Шаг 1: Найти родительский контейнер, где находятся "три точки"
        parent_container = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.XPATH, "//*[@id='ric-navigation-logic-v2-tab']/div[4]/div[5]/div/div/div/div/div[1]/div[1]"))
        )

        # Шаг 2: Навести мышку на родительский контейнер
        actions = ActionChains(driver)
        actions.move_to_element(parent_container).perform()
        print("Наведение на родительский контейнер выполнено успешно.")

        # Шаг 3: Найти кнопку "три точки"
        dots_button = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, "//*[@id='ric-navigation-logic-v2-tab']/div[4]/div[5]/div/div/div/div/div[1]/div[1]/button"))
        )

        # Шаг 4: Кликнуть по кнопке "три точки"
        actions.move_to_element(dots_button).click().perform()
        print("Клик по 'трем точкам' выполнен успешно.")

        # Шаг 5: Найти кнопку "Удалить" в выпадающем меню
        delete_button = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@role='menuitem' and text()='Удалить']"))
        )

        # Шаг 6: Кликнуть по кнопке "Удалить"
        delete_button.click()
        print("Шаг 6: Кнопка 'Удалить' нажата успешно.")

        # Шаг 7: Найти и нажать кнопку "OK" в модальном окне
        ok_button = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@class='ric-btn ric-btn-primary' and text()='OK']"))
        )
        ok_button.click()
        print("Шаг 7: Кнопка 'OK' нажата успешно.")

        # Запись в отчет об успешном выполнении
        write_to_report(6, "Нажатие на три точки и удаление через выпадающее меню", "ОК")
        print("Тест кейс: Нажатие на три точки и удаление через выпадающее меню: Успешно")
    except Exception as e:
        # Запись в отчет об ошибке
        write_to_report(6, "Нажатие на три точки и удаление через выпадающее меню", f"Ошибка: {str(e)}")
        print(f"Тест кейс: Нажатие на три точки и удаление через выпадающее меню: Ошибка: {str(e)}")
        raise



def create_handler():
    """Тест кейс: Создание обработчика через интерфейс."""
    try:
        # Шаг 1: Переход в раздел "Обработчики"
        handlers_section = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "li.ric-main-nav-item[data-module='handlers']"))
        )
        handlers_section.click()
        print("Шаг 1: Перешли на вкладку 'Обработчики' успешно!")

        # Шаг 2: Нажатие на кнопку "Создать" (первая кнопка)
        first_create_button = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'button primary') and text()='Создать']"))
        )
        first_create_button.click()
        print("Шаг 2: Нажали на первую кнопку 'Создать' успешно!")

        # Шаг 3: Нажатие на вторую кнопку "Создать"
        second_create_button = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, "//div[contains(@class, 'index__asyncButtonContent___brdE2') and .//span[text()='Создать']]"))
        )
        second_create_button.click()
        print("Шаг 3: Нажали на вторую кнопку 'Создать' успешно!")

        # Запись в отчёт об успешном выполнении
        write_to_report(8, "Создание обработчика через интерфейс", "ОК")
        print("Тест кейс - Создание обработчика через интерфейс: Успешно")
    except Exception as e:
        # Запись в отчёт об ошибке
        write_to_report(8, "Создание обработчика через интерфейс", f"Ошибка: {str(e)}")
        print(f"Тест кейс - Создание обработчика через интерфейс: Ошибка: {str(e)}")
        raise



def del_handler():
    """Тест кейс: Нажатие на три точки через XPath и удаление с имитацией наведения мышки."""
    try:
        # Шаг 1: Переход в раздел "Обработчики"
        handlers_section = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "li.ric-main-nav-item[data-module='handlers']"))
        )
        handlers_section.click()
        print("Шаг 1: Перешли на вкладку 'Обработчики' успешно!")

        # Шаг 2: Найти родительский контейнер, где находятся "три точки"
        parent_container = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.XPATH, "//*[@id='ric-navigation-handlers-tab']/div[4]/div[5]/div/div/div/div/div[1]/div[1]"))
        )

        # Шаг 3: Навести мышку на родительский контейнер
        actions = ActionChains(driver)
        actions.move_to_element(parent_container).perform()
        print("Шаг 3: Наведение на родительский контейнер выполнено успешно.")

        # Шаг 4: Найти кнопку "три точки" через XPath
        dots_button = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, "//*[@id='ric-navigation-handlers-tab']/div[4]/div[5]/div/div/div/div/div[1]/div[1]/button"))
        )
        print("Кнопка 'три точки' найдена через XPath.")

        # Шаг 5: Кликнуть по кнопке "три точки"
        actions.move_to_element(dots_button).click().perform()
        print("Шаг 5: Клик по 'трем точкам' выполнен успешно.")

        # Шаг 6: Найти кнопку "Удалить" в выпадающем меню
        delete_button = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@role='menuitem' and text()='Удалить']"))
        )

        # Шаг 7: Кликнуть по кнопке "Удалить"
        delete_button.click()
        print("Шаг 7: Кнопка 'Удалить' нажата успешно.")

        # Шаг 8: Найти и нажать кнопку "OK" в модальном окне
        ok_button = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@class='ric-btn ric-btn-primary' and text()='OK']"))
        )
        ok_button.click()
        print("Шаг 8: Кнопка 'OK' нажата успешно.")

        # Запись в отчет об успешном выполнении
        write_to_report(7, "Нажатие на три точки через XPath и удаление", "ОК")
        print("Тест кейс: Нажатие на три точки через XPath и удаление: Успешно")
    except Exception as e:
        # Запись в отчет об ошибке
        write_to_report(7, "Нажатие на три точки через XPath и удаление", f"Ошибка: {str(e)}")
        print(f"Тест кейс: Нажатие на три точки через XPath и удаление: Ошибка: {str(e)}")
        raise


def create_geozone():
    """Тест кейс: Создание геозоны через интерфейс."""
    try:
        # Шаг 1: Переход в раздел "Геозоны"
        geofences_section = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "li.ric-main-nav-item[data-module='geofences']"))
        )
        geofences_section.click()
        print("Шаг 1: Перешли в раздел 'Геозоны' успешно!")

        # Шаг 2: Нажатие на кнопку "+"
        plus_button = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, "(//button[@class='ric-module-create-item'])[5]"))
        )
        plus_button.click()
        print("Шаг 2: Нажали на кнопку '+' успешно!")

        # Запись в отчет об успешном выполнении
        write_to_report(8, "Создание геозоны через интерфейс", "ОК")
        print("Тест кейс: Создание геозоны через интерфейс: Успешно")
    except Exception as e:
        # Запись в отчет об ошибке
        write_to_report(8, "Создание геозоны через интерфейс", f"Ошибка: {str(e)}")
        print(f"Тест кейс: Создание геозоны через интерфейс: Ошибка: {str(e)}")
        raise


def create_label_through_interface():
    """Тест кейс: Создание метки через интерфейс."""
    try:
        # Шаг 1: Переход в раздел "Метки"
        labels_section = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "li.ric-main-nav-item[data-module='labels']"))
        )
        labels_section.click()
        print("Шаг 1: Перешли на вкладку 'Метки' успешно!")

        # Шаг 2: Нажатие на кнопку "Создать"
        create_button_initial = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, "//*[@id='ric-viewports']/div[15]/div/div/div[2]/button"))
        )
        create_button_initial.click()
        print("Шаг 2: Нажали на кнопку 'Создать' успешно!")

        # Шаг 3: Нажатие на кнопку "Создать" в новом окне
        create_button_final = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, "//*[@id='ric-pages']/div[4]/div[3]/div[1]/div/div[1]/div[1]/button"))
        )
        create_button_final.click()
        print("Шаг 3: Нажали на финальную кнопку 'Создать' успешно!")

        # Запись в отчёт об успешном выполнении
        write_to_report(9, "Создание метки через интерфейс", "ОК")
        print("Тест кейс: Создание метки через интерфейс: Успешно")
    except Exception as e:
        # Запись в отчёт об ошибке
        write_to_report(9, "Создание метки через интерфейс", f"Ошибка: {str(e)}")
        print(f"Тест кейс: Создание метки через интерфейс: Ошибка: {str(e)}")
        raise


def click_three_dots_and_delete_label():
    """Тест кейс: Нажатие на три точки для метки и удаление."""
    try:
        # Шаг 1: Переход в раздел "Метки"
        labels_section = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "li.ric-main-nav-item[data-module='labels']"))
        )
        labels_section.click()
        print("Шаг 1: Перешли на вкладку 'Метки' успешно!")

        # Шаг 2: Найти родительский контейнер с "тремя точками"
        parent_container = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div[3]/div[2]/div[7]/div[4]/div[5]/div/div/div/div/div[1]/div[1]"))
        )

        # Шаг 3: Навести мышку на родительский контейнер
        actions = ActionChains(driver)
        actions.move_to_element(parent_container).perform()
        print("Шаг 3: Наведение на родительский контейнер выполнено успешно.")

        # Шаг 4: Найти кнопку "три точки" с полным XPath
        dots_button = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[3]/div[2]/div[7]/div[4]/div[5]/div/div/div/div/div[1]/div[1]/button"))
        )

        # Шаг 5: Кликнуть по кнопке "три точки"
        actions.move_to_element(dots_button).click().perform()
        print("Шаг 5: Клик по 'трем точкам' выполнен успешно.")

        # Шаг 6: Найти кнопку "Удалить" в выпадающем меню
        delete_button = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@role='menuitem' and text()='Удалить']"))
        )

        # Шаг 7: Кликнуть по кнопке "Удалить"
        delete_button.click()
        print("Шаг 7: Кнопка 'Удалить' нажата успешно.")

        # Шаг 8: Найти и нажать кнопку "OK" в модальном окне
        ok_button = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@class='ric-btn ric-btn-primary' and text()='OK']"))
        )
        ok_button.click()
        print("Шаг 8: Кнопка 'OK' нажата успешно.")

        # Запись в отчёт об успешном выполнении
        write_to_report(10, "Нажатие на три точки для метки и удаление", "ОК")
        print("Тест кейс: Нажатие на три точки для метки и удаление: Успешно")
    except Exception as e:
        # Запись в отчёт об ошибке
        write_to_report(10, "Нажатие на три точки для метки и удаление", f"Ошибка: {str(e)}")
        print(f"Тест кейс: Нажатие на три точки для метки и удаление: Ошибка: {str(e)}")
        raise



def create_dashboard():
    """Тест кейс: Переход в раздел 'Дашборды' и создание нового дашборда."""
    try:
        # Шаг 1: Переход в раздел "Дашборды"
        dashboards_section = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "li.ric-main-nav-item[data-module='dashboards']"))
        )
        dashboards_section.click()
        print("Шаг 1: Перешли на вкладку 'Дашборды' успешно!")

        # Шаг 1: Ожидание, пока кнопка станет кликабельной
        plus_button = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[3]/div[2]/div[8]/div[1]/button"))
        )
        print("Кнопка '+' найдена и кликабельна.")
        
        # Шаг 2: Клик по кнопке
        plus_button.click()
        print("Клик по кнопке '+' выполнен успешно.")
    except Exception as e:
        # Запись в отчёт об ошибке
        write_to_report(11, "Создание дашборда", f"Ошибка: {str(e)}")
        print(f"Тест кейс: Создание дашборда: Ошибка: {str(e)}")
        raise



def click_three_dots_dashboard():
    """Тест кейс: Нажатие на три точки для дашборда с имитацией наведения."""
    try:
        # Шаг 2: Переход в раздел "Модели"
        models_section = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "li.ric-main-nav-item[data-module='models-v3']"))
        )
        models_section.click()
        print("Шаг 2: Перешли в раздел 'Модели' успешно!")

        # Шаг 1: Найти родительский контейнер для наведения мыши
        parent_container = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div[3]/div[2]/div[1]/div[4]/div[5]/div/div/div/div/div[1]/div[1]"))
        )
        

        actions = ActionChains(driver)
        actions.move_to_element(parent_container).perform()
        print("Шаг 2: Наведение на родительский контейнер выполнено успешно.")


        dots_button = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[3]/div[2]/div[1]/div[4]/div[5]/div/div/div/div/div[1]/div[1]/button"))
        )
        actions.move_to_element(dots_button).click().perform()
        print("Шаг 3: Клик по 'трем точкам' выполнен успешно.")

        delete_button = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@role='menuitem' and text()='Удалить']"))
        )
        delete_button.click()
        print("Шаг 4: Кнопка 'Удалить' нажата успешно.")

        # Шаг 5: Найти и нажать кнопку "OK" в модальном окне
        ok_button = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@class='ric-btn ric-btn-primary' and text()='OK']"))
        )
        ok_button.click()
        print("Шаг 5: Кнопка 'OK' нажата успешно.")

        # Запись в отчёт об успешном выполнении
        write_to_report(13, "Удаление дашборда через три точки и подтверждение", "ОК")
        print("Тест кейс: Удаление дашборда через три точки и подтверждение: Успешно")
    except Exception as e:
        # Запись в отчёт об ошибке
        write_to_report(13, "Удаление дашборда через три точки и подтверждение", f"Ошибка: {str(e)}")
        print(f"Тест кейс: Удаление дашборда через три точки и подтверждение: Ошибка: {str(e)}")
        raise


# Инициализация драйвера
driver = webdriver.Chrome(service=service, options=options)


initialize_report()  # Инициализация отчёта
login()              # Выполнение теста на логирование
create_model()
create_object_in_objects_section()
del_obj()
navigate_to_logic_and_create()
del_log()
create_handler()
del_handler()
# create_geozone()
create_label_through_interface()
click_three_dots_and_delete_label()
# create_dashboard()
click_three_dots_dashboard()
time.sleep(10)
driver.quit()        # Закрытие браузера
