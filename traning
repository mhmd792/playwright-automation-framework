import pytest 

@pytest.fixture
def mock_user():
    return {
        "username": "mohamed",
        "role": "admin",
        "is_active": True,
        "password": "123"
    }

@pytest.mark.parametrize("check_user", [
    "monday",
    "245",
    "258",
    "123"
])

def test_user_password(check_user, mock_user):
  assert mock_user["is_active"] == True
  assert mock_user["password"] == check_user
