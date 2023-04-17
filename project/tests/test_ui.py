from project.constants import mail, password, NAME_TEST_FOLDER_UI, NAME_TEST_DOC_UI
from project.pages.authorization_page import AuthorizationPage
from project.pages.home_page import HomePage
from project.pages.ya_disk_page import YaDiskPage


def test_yadisk_ui(driver):
    work_driver = driver
    home_page = HomePage(work_driver)
    home_page.open_page()
    home_page.click_enter_button()
    home_page.click_enter_yandex_id_link()

    authorization_page = AuthorizationPage(work_driver)
    authorization_page.change_mail_way()
    authorization_page.logining(mail, password)

    ya_disk_page = YaDiskPage(work_driver)
    ya_disk_page.open_page()
    ya_disk_page.create_dir(name_folder=NAME_TEST_FOLDER_UI)
    ya_disk_page.open_dir()

    files_before_create = ya_disk_page.get_all_file()
    doc = ya_disk_page.create_file(name_doc=NAME_TEST_DOC_UI)

    doc.close_file()
    files_after_create = ya_disk_page.get_all_file()
    add_files = set(files_after_create) ^ set(files_before_create)
    assert add_files, 'New file not create '

    expected_file = ya_disk_page.test_file.find_element_by_xpath()
    assert expected_file, 'File with expected name not found '

