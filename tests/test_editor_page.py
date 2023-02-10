from time import sleep
from pages.editor_page import wysiwygEditor

def test_editor(browser):
    editor = wysiwygEditor(browser)
    editor.load_Page()
    editor.click_link_editor()
    assert "An iFrame containing the TinyMCE WYSIWYG Editor" in editor.get_text_page()
    editor.click_select_file()
    editor.click_new_documnet()
    editor.text_editor("Am Scris Ceva")
    #editor.text_editor()==True
    editor.click_select_italic()
    editor.click_select_bold()
    editor.text_editor("Am scris inca ceva")
    assert "Italic" == editor.get_confirm_italic()
    editor.click_format_text()
    #editor.click_clear()

