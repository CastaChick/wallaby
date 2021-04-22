from spread_sheets_client import GoogleSpreadSheetsClient

class Todo:
    def __init__(self, title, is_done, channel):
        self.title = title
        self.is_done = is_done
        self.channel = channel
        self.__index = None

    def to_message(self):
        checkmark = ':ballot_box_with_check:' if self.is_done else ':heavy_minus_sign:'
        message = f'{checkmark} {self.title}'

        return message

    def register(self):
        client = GoogleSpreadSheetsClient()
        row_data = [self.title, 'TRUE' if self.is_done else 'FALSE', self.channel]
        client.write_record(row_data)

    def done(self):
        self.is_done = True
        client = GoogleSpreadSheetsClient()
        target_cell = 'B' + str(self.__index + 2)
        client.write_cell(target_cell, 'TRUE')

    def undone(self):
        self.is_done = False
        client = GoogleSpreadSheetsClient()
        target_cell = 'B' + str(self.__index + 2)
        client.write_cell(target_cell, 'FALSE')
        
    def set_index(self, i):
        self.__index = i
