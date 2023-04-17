import pytest

from project.constants import NAME_TEST_DOC_API, NAME_TEST_FOLDER_API, RENAME_TEST_DOC_API, NOT_FOUND_STATUS_CODE, \
    CREATED_STATUS_CODE


@pytest.mark.parametrize('expected_response', ([{
    'href': 'https://cloud-api.yandex.net/v1/disk/resources?path=disk%3A%2Ftest_api_folder%2Fnew_name.docx',
    'method': 'GET',
    'templated': False
}]))
def test_yadisk_api(api_yandex, expected_response):
    api_yandex.create_folder(NAME_TEST_FOLDER_API)
    api_yandex.copy_file(path_to_file=NAME_TEST_DOC_API, destination=NAME_TEST_FOLDER_API)
    response = api_yandex.rename_file(old_path=f'{NAME_TEST_FOLDER_API}/{NAME_TEST_DOC_API}',
                                      new_path=f'{NAME_TEST_FOLDER_API}/{RENAME_TEST_DOC_API}')

    last_name_response = api_yandex.check_rename_file(path_to_file=f'{NAME_TEST_FOLDER_API}/{NAME_TEST_DOC_API}')
    actual_response = response.json()

    assert last_name_response.status_code == NOT_FOUND_STATUS_CODE, f'File not rename'
    assert response.status_code == CREATED_STATUS_CODE, \
        f'Expected status code: {CREATED_STATUS_CODE}, actual status code: {response.status_code}'
    assert actual_response == expected_response, \
        f'Expected body: {expected_response}, actual body: {actual_response}'

