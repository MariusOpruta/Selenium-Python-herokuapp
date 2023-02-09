from pages.dropdown_page import DropDown


def test_dropdown(browser):
    drop_down = DropDown(browser)
    drop_down.load_page()
    drop_down.list_down()
    drop_down.option_1()
    drop_down.option_2()
    assert "Dropdown List" in drop_down.getText()

