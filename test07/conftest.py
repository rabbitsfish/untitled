import pytest
@pytest.fixture()
def login1():
    print('please login')

def pytest_configure(config):
    marker_list = ['login', 'login1']
    for markers in marker_list:
        config.addinivalue_line('markers', markers)