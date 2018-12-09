from flask import escape
from mySmartSheet import access_token, archSheet, ss_get_client, ss_get_sheet_parsed, ss_update_row, ss_remove_rows

from datetime import datetime



ss_client = ss_get_client(access_token)
EN_list = ss_get_sheet_parsed(ss_client,archSheet)

date = datetime.now()
print("\n")
print (client)
print (date)
print ("\n")


