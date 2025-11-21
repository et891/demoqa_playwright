import pytest
from config.settings import BASE_URL

@pytest.fixture
def page_context(page):
    page.set_viewport_size({"width": 1400, "height": 900})
    page.goto(BASE_URL)
    return page