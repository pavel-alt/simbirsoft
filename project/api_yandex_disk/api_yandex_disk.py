from requests import Response

from framework.api.api import API
from project.constants import API_KEY


class ApiYandexDisc(API):
    resources_path = '/resources'
    move_path = '/resources/move'
    upload_path = '/resources/upload'

    def set_headers(self) -> None:
        """Установка заголовков"""
        setattr(self, 'headers',
                {
                 "Authorization": f"OAuth {API_KEY}",
                 "Content-Type": "application/json",
                 "Accept": "application/json"
                 })

    def create_folder(self, name_folder: str) -> Response:
        """Создание папки"""
        return self.put(uri=self.resources_path, params={"path": f"{name_folder}"})

    def copy_file(self, path_to_file: str, destination: str) -> Response:
        """Копирование файла"""
        res = self.get(
            uri=self.upload_path, params={"path": f"{destination}/{path_to_file}"})
        href = res.json()["href"]
        files = {"file": path_to_file}
        return self.put(full_url=href, params=files)

    def rename_file(self, old_path: str, new_path: str) -> Response:
        """Переименование файла"""
        return self.post(uri=self.move_path, params={"from": old_path, "path": new_path})

    def delete_folder(self, name_folder: str) -> Response:
        """Удаление папки"""
        return self.delete(uri=self.resources_path, params={"path": f"{name_folder}"})

    def check_rename_file(self, path_to_file) -> Response:
        """Проверка переименования файла"""
        return self.get(uri=self.resources_path, params={"path": path_to_file})
