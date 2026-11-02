import os
import requests


class YougileApi:
    def __init__(self, url="https://ru.yougile.com/api-v2"):
        self.url = url
        self.token = os.getenv("YOUGILE_TOKEN")
        if not self.token:
            raise ValueError(
                "Переменная окружения YOUGILE_TOKEN не установлена. "
                "Задайте её перед запуском тестов."
            )
        self.headers = {
            "Authorization": f"Bearer {self.token}",
            "Content-Type": "application/json"
        }

    def create_project(self, title, users=None):
        """[POST] /api-v2/projects"""
        payload = {"title": title}
        if users:
            payload["users"] = users
        return requests.post(
            f"{self.url}/projects",
            json=payload,
            headers=self.headers
        )

    def create_project_raw(self, payload):
        """Вспомогательный метод для негативных тестов (некорректный payload)"""
        return requests.post(
            f"{self.url}/projects",
            json=payload,
            headers=self.headers
        )

    def get_project(self, project_id):
        """[GET] /api-v2/projects/{id}"""
        return requests.get(
            f"{self.url}/projects/{project_id}",
            headers=self.headers
        )

    def update_project(self, project_id, title=None, users=None):
        """[PUT] /api-v2/projects/{id}"""
        payload = {}
        if title is not None:
            payload["title"] = title
        if users is not None:
            payload["users"] = users
        return requests.put(
            f"{self.url}/projects/{project_id}",
            json=payload,
            headers=self.headers
        )

    def delete_project(self, project_id):
        """[DELETE] /api-v2/projects/{id} — для очистки данных"""
        return requests.delete(
            f"{self.url}/projects/{project_id}",
            headers=self.headers
        )