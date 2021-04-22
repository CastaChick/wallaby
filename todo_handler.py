from spread_sheets_client import GoogleSpreadSheetsClient
from todo import Todo

class TodoHandler:
    def __init__(self):
        self.client = GoogleSpreadSheetsClient()

    def get_todo(self, n):
        values = self.client.get_record(n)
        return self.__dict_to_todo(values)
        

    def __dict_to_todo(self, _dict):
        _dict['is_done'] = True if _dict['is_done'] == 'TRUE' else False

        return Todo(**_dict)


    def get_todo_by_channel(self, channel):
        todo_channels = self.client.get_column(2)['values']
        picked_todos = []
        for i, todo_channel in enumerate(todo_channels):
            if channel == todo_channel:
                picked_todos.append(i)

        return [self.__dict_to_todo(self.client.get_record(i)) for i in picked_todos]
