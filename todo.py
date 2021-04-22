from spread_sheets_client import GoogleSpreadSheetsClient

class Todo:
    def __init__(self, title, is_done, channel):
        self.title = title
        self.is_done = is_done
        self.channel = channel

    def to_message(self):
        checkmark = ':ballot_box_with_check:' if self.is_done else ':heavy_minus_sign:'
        message = f'{checkmark} {self.title}'

        return message

    def register(self):
        client = GoogleSpreadSheetsClient()
        row_data = [self.title, 'TRUE' if self.is_done else 'FALSE', self.channel]
        client.write_record(row_data)
