 # По какой характеристике ищем 
import pytest

from pages.page_class import PageObject

# Название класса ДОЛЖНО выглядеть как: Test<Имя>
class TestWebsite:
    # Test Case 1 - Check Address
    def test_check_address(self):
        page = PageObject()
        # Проверить, что адрес отображается на странице
        expected_text = 'Днепр, пр. Правды, 143'
        address = page.get_text(block_name='//div[@class="company-contacts"]/div[2]',
                                search='xpath')
        # Правильный ли в нем текст? (Тут мы находим баг)
        assert expected_text == address