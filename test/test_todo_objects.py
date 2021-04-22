import pytest
from ..todo import Todo

class Test_Todoクラスのテスト:
    @pytest.fixture
    def test_todo(self):
            title = 'test'
            is_done = False
            channel = '#test'
            return Todo(title, is_done, channel)
    def test_Todoを作成してその属性値をを取得できる(self, test_todo):
        expect = Todo('test', False, '#test')
        assert test_todo.to_message() == expect.to_message()

    def test_Todoを文字列で表示する(self, test_todo):
        expect = ':heavy_minus_sign: test'
        assert test_todo.to_message() == expect
