import gspread
from pathlib import Path
import json

from oauth2client.service_account import ServiceAccountCredentials 

import settings

class GoogleSpreadSheetsClient:
    def __init__(self):
        self.scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
        self.credentials = ServiceAccountCredentials.from_json_keyfile_name(Path().resolve().joinpath('env').joinpath('account_key.json'), self.scope)
        self.gc = gspread.authorize(self.credentials)
        self.SHEET_KEY = settings.SHEET_KEY
        self.worksheet = self.gc.open_by_key(self.SHEET_KEY).sheet1

    def get_cell(self, cell):
        target_value = self.worksheet.acell(cell).value
        return target_value

    def get_record(self, row):
        header = self.worksheet.row_values(1)
        values = self.worksheet.row_values(row + 2)
        return {key: value for key, value in zip(header, values)}

    def get_column(self, col):
        values = self.worksheet.col_values(col+1)
        return {'header': values[0], 'values': values[1:]}

    def write_cell(self, cell, value):
        self.worksheet.update_acell(cell, value)

    def write_record(self, d_list):
        record_id = last_record_id = len(self.get_column(0)['values']) + 2
        c_list = ['A', 'B', 'C']
        for i, data in enumerate(d_list):
            self.write_cell(c_list[i]+str(record_id), data)
