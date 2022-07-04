import pytest

import selenium

@pytest.fixture()
def go_to_website():
     browser = webdriver.Chrome(executable_path = PATH)
     browser.get(WEBSITE)
     