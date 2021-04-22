import settings

API_TOKEN = settings.API_TOKEN
DEFAULT_REPLY = \
'''コマンドの使い方を教えるよ！
`list` : このチャンネルに登録されているTodoをリスト形式で教えるよ
`add` : このチャンネルに新しいTodoを作成するよ
`done [番号]` : リストに書かれた番号のTodoを完了にするよ
`undone [番号]` : リストに書かれた番号のTodoを未完了に戻すよ
'''

PLUGINS = ['plugins']
