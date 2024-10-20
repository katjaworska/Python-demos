import requests

URL = 'https://simple-books-api.glitch.me'

def test_get_status():
    response = requests.get(f"{URL}/status")
    assert response.status_code == 200

def test_get_book_list():
    response = requests.get(f"{URL}/books")
    assert response.status_code == 200
    assert response.json() is not None

def test_get_book_list_fiction():
    response = requests.get(f"{URL}/books?type=fiction")
    assert response.status_code == 200
    list = response.json()
    for list_el in list:
        for dict_key, dict_value in list_el.items():
            if dict_key == 'type':
                assert dict_value == 'fiction'

def test_get_single_book():
    book_id = 1
    response = requests.get(f"{URL}/books/{book_id}")
    result = response.json()
    assert response.status_code == 200
    assert result['id'] == book_id