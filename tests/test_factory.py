# 工厂
# 唯一可以改变的行为是传递测试配置。如果没传递配置，那么会有一些缺省配置可 用，否则配置会被重载。
from flaskr import create_app


def test_config():
    assert not create_app().testing
    assert create_app({'TESTING': True}).testing


def test_home(client):
    result = client.get('/home')
    assert result.data == b'home'
