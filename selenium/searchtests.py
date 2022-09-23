import unittest
from selenium import webdriver


class HomePageTests(unittest.TestCase):

    def setUp(self) -> None:
        # digo a selenium donde está el driver
        self.driver = webdriver.Chrome(executable_path='./chromedriver')
        driver = self.driver  # nombro en una variable a self.driver
        driver.get("http://demo-store.seleniumacademy.com/")  # paso la url
        driver.maximize_window()  # maximizo la pantalla para traabajar con sitios responsivos
        driver.implicitly_wait(15)  # le pido que espere 15 segundos

    def test_search_text_field(self):
        search_field = self.driver.find_element_by_id("search")  # busco por id

    def test_search_text_field_by_name(self):
        search_field = self.driver.find_element_by_name(
            "q")  # busco por nombre

    def test_search_text_field_by_class_name(self):
        search_field = self.driver.find_element_by_class_name(
            "input-text")  # busco por nombre de clase

    def test_search_button_enabled(self):
        button = self.driver.find_element_by_class_name("button")

    def test_count_of_promo_banner_images(self):
        banner_list = self.driver.find_element_by_class_name(
            "promos")  # guardo en una variable la lista de promos
        # guardo en una variable los elementos de la lista anterior con tag img
        banners = banner_list.find_elements_by_tag_name('img')
        # assert de que haya 3 dentro de banners
        self.assertEqual(3, len(banners))

    def test_vip_promo(self):
        vip_promo = self.driver.find_elements_by_xpath(
            '//*[@id="top"]/body/div/div[2]/div[2]/div/div/div[2]/div[1]/ul/li[2]/a/img')

    def test_shopping_cart(self):
        shopping_cart_icon = self.driver.find_element_by_css_selector(
            "div.header-minicart span.icon")

    def tearDown(self) -> None:
        self.driver.quit()  # cerrar la ventana al finalizar


if __name__ == "__main__":
    unittest.main(verbosity=2)
