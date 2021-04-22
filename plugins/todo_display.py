from slackbot.bot import respond_to
from todo_handler import TodoHandler
from todo import Todo

@respond_to('list')
def todo_list(message):
    handler = TodoHandler()
    target_channel = '#' + message.channel._body['name']
    todos = handler.get_todo_by_channel(target_channel)
    if todos:
        todo_message = '\n'.join([todo.to_message()+': '+str(i+1) for i, todo in enumerate(todos)])
    else:
        todo_message = 'このチャンネルにはTodoが設定されていないよ！'
    message.send(todo_message)

@respond_to('add')
def add_todo(message):
    handler = TodoHandler()
    target_channel = '#' + message.channel._body['name']
    todo_title = message._body['text'].split(' ')[1]
    new_todo = Todo(todo_title, False, target_channel)
    new_todo.register()
    message.send(f'{todo_title}を追加したよ！')

@respond_to(r'^done')
def done_todo(message):
    handler = TodoHandler()
    target_channel = '#' + message.channel._body['name']
    todos = handler.get_todo_by_channel(target_channel)
    index = int(message._body['text'].split(' ')[1]) - 1
    target_todo = todos[index]
    target_todo.done()

    message.send(f'『{target_todo.title}』が完了したよ！')

@respond_to(r'^undone')
def done_todo(message):
    handler = TodoHandler()
    target_channel = '#' + message.channel._body['name']
    todos = handler.get_todo_by_channel(target_channel)
    index = int(message._body['text'].split(' ')[1]) - 1
    target_todo = todos[index]
    target_todo.undone()

    message.send(f'『{target_todo.title}』を未完了に戻したよ！')
