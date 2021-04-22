from slackbot.bot import respond_to
from todo_handler import TodoHandler

@respond_to('list')
def todo_list(message):
    handler = TodoHandler()
    target_channel = '#' + message.channel._body['name']
    todos = handler.get_todo_by_channel(target_channel)
    
    if todos:
        todo_message = '\n'.join([todo.to_message() for todo in todos])
    else:
        todo_message = 'このチャンネルにはTodoが設定されていないよ！'
    message.send(todo_message)
