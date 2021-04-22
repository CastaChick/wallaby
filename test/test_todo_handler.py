from ..todo_handler import TodoHandler
from ..todo import Todo

class Test_todoを管理するクラスのテスト:
    def test_スプレッドシートからTodoオブジェクトを生成(self):
        handler = TodoHandler()
        todo = handler.get_todo(0)
        expect = Todo('test', False, '#test')
        
        assert todo.to_message() == expect.to_message()

    def test_あるチャンネルに紐づくtodoを取得する(self):
        handler = TodoHandler()
        todos = handler.get_todo_by_channel('#test')
        first_todo = Todo('test', False, '#test')
        second_todo = Todo('test2', True, '#test')

        assert [todo.to_message() for todo in todos] == [first_todo.to_message(), second_todo.to_message()]
