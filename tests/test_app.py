from http import HTTPStatus
from fastapi.testclient import TestClient  # type: ignore
from aula08.app import app
import pytest


def test_root_deve_retornar_ok_e_ola_mundo(client):
    response = client.get('/')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'Ola Mundo!'}


def test_create_user(client):
    response = client.post( # Validando o UserSchema
        '/users/',
        json={
            'username': 'alice',
            'email': 'alice@example.com',
            'password': 'secret',
        },
    )
    assert response.status_code == HTTPStatus.CREATED
    assert response.json() == {
        'username': 'alice',
        'email': 'alice@example.com',
        'id': 1,
    }
    
def test_update_user_error(client):
    response = client.put(
        '/users/100',
        json={
            'username': 'testeusername2',
            'email': 'alice@example.com',
            'password': '123',
            'id': 1,
        },
    )
    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {'detail': 'User not found'}
    
    
def test_delete_user(client):
    response = client.delete('/users/1')
    
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'User Deleted'}
    
    
def test_delete_user_error(client):
    response = client.delete('/users/100')
    
    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {'detail': 'User not found'}    
    