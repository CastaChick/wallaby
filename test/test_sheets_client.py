from ..spread_sheets_client import GoogleSpreadSheetsClient

class Test_スプレッドシートにアクセスして読み書きを行う:
    def test_スプレッドシートのA1の値を読み取る(self):
        client = GoogleSpreadSheetsClient()
        assert client.get_cell('A1') == 'title'

    def test_スプレッドシートの行から1レコードを取得する(self):
        client = GoogleSpreadSheetsClient()
        expect = {
            'title': 'test',
            'is_done': 'FALSE',
            'channel': '#test',
            }
        data = client.get_record(0)
        assert data == expect

    def test_スプレッドシートの列から値を取得する(self):
        client = GoogleSpreadSheetsClient()
        data = client.get_column(0)
        assert data['values'][0] == 'test'
    
    def test_スプレッドシートのA2に値を書き込む(self):
        client = GoogleSpreadSheetsClient()
        client.write_cell('A2', 'test')
        assert client.get_cell('A2') == 'test'

    def test_スプレッドシートの末尾にレコードを追加する(self):
        client = GoogleSpreadSheetsClient()
        client.write_record(['test_write', 'FALSE', '#test_write'])
        expect = {
            'title': 'test_write',
            'is_done': 'FALSE',
            'channel': '#test_write'
        }

        last_record_id = len(client.get_column(0)['values']) - 1
        data = client.get_record(last_record_id)
        assert data == expect

