import allure
from conftest import browser
from pages.logo_page import LogoPage


class TestURL:
    @allure.title('Проверка URL Логотипа "Самокат"')
    def test_main_page(self, browser):
        page = LogoPage()
        # Открытие браузера
        page.open_browser(browser)
        # Клик по кнопке "Заказать" в шапке лендинга
        page.click_order_button(browser)
        # Клик по логотипу "Самокат"
        page.click_scooter_button(browser)
        # Проверка URL Логотипа "Самокат"
        page.should_main_page_url(browser)

    @allure.title('Проверка URL Логотипа "Яндекс"')
    def test_dzen_url(self, browser):
        page = LogoPage()
        # Открытие браузера
        page.open_browser(browser)
        # Клик по кнопке "Заказать" в шапке лендинга
        page.click_dzen_button(browser)
        # Переключение в новую вкладку
        page.switching_to_the_tab(browser)
        # Ожидаем загрузки страницы Дзен
        page.wait_for_page_load(browser)
        # Проверка URL Логотипа "Самокат"
        page.should_dzen_url(browser)