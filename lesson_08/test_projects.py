import uuid

from yougile_api import YougileApi


api = YougileApi()


# POST /api-v2/projects

def test_create_project():
    """Позитивный: создание проекта с валидным названием."""
    title = f"Auto_Project_{uuid.uuid4().hex[:6]}"
    resp = api.create_project(title)

    assert resp.status_code == 201
    body = resp.json()
    assert "id" in body

    project_id = body["id"]

    # Проверяем через GET, что проект создан с нужным названием
    get_resp = api.get_project(project_id)
    assert get_resp.status_code == 200
    assert get_resp.json()["title"] == title

    api.delete_project(project_id)


def test_create_project_negative_missing_title():
    """Негативный: создание без обязательного поля title."""
    resp = api.create_project_raw(payload={})

    assert resp.status_code == 400
    assert "error" in resp.text.lower()


# GET /api-v2/projects/{id}

def test_get_project():
    """Позитивный: получение существующего проекта."""
    title = f"Project_For_Get_{uuid.uuid4().hex[:6]}"
    create_resp = api.create_project(title)
    assert create_resp.status_code == 201
    project_id = create_resp.json()["id"]

    resp = api.get_project(project_id)

    assert resp.status_code == 200
    body = resp.json()
    assert body["id"] == project_id
    assert body["title"] == title

    api.delete_project(project_id)


def test_get_project_negative_not_found():
    """Негативный: запрос несуществующего проекта."""
    fake_id = str(uuid.uuid4())
    resp = api.get_project(fake_id)

    assert resp.status_code == 404
    assert "error" in resp.text.lower()


# PUT /api-v2/projects/{id}

def test_update_project():
    """Позитивный: изменение названия проекта."""
    old_title = f"Old_Title_{uuid.uuid4().hex[:6]}"
    create_resp = api.create_project(old_title)
    assert create_resp.status_code == 201
    project_id = create_resp.json()["id"]

    new_title = f"New_Title_{uuid.uuid4().hex[:6]}"
    resp = api.update_project(project_id, title=new_title)

    assert resp.status_code == 200

    # Проверяем через GET, что название действительно изменилось
    get_resp = api.get_project(project_id)
    assert get_resp.status_code == 200
    assert get_resp.json()["title"] == new_title

    api.delete_project(project_id)


def test_update_project_negative_not_found():
    """Негативный: обновление несуществующего проекта."""
    fake_id = str(uuid.uuid4())
    resp = api.update_project(fake_id, title="Any")

    assert resp.status_code == 404
    assert "error" in resp.text.lower()