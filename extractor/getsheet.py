import google.oauth2.credentials
import json
from RuleInteraction import RuleInteraction, RuleSet

from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from google_auth_oauthlib.flow import InstalledAppFlow

# TODO: You will need to change this to the location of your secrets file
CLIENT_SECRETS_FILE = "/Users/linneaross/Downloads/client_secrets.json"

SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']
API_SERVICE_NAME = 'sheets'
API_VERSION = 'v4'

# The sheet-id is the identifier of the spreadsheet
#
# TODO: You will need to replace this with the ID of your spreadsheet
#       It can be found from the URL of the spreadsheet in your browser (between slashes)
SHEET_ID = '1BSEXfFzA2cRIMQGIrDmWrZnOcAHuVF9TBjRwtcq6_aQ'


class SpreadSheetRow(object):
    def __init__(self, apiRow):
        self.values = []
        for col in apiRow:
            if "formattedValue" in col:
                self.values.append(col['formattedValue'])
            else:
                self.values.append("")

    def htmlRow(self):
        result = "<tr>\n"
        for value in self.values:
            result += "  <td>%s</td>\n" % unicode(value)
        result += "</tr>\n"
        return result

    
class SpreadSheet(object):
    def __init__(self, apiRowData):
        #print json.dumps(apiRowData, indent=4, sort_keys=True)
        self.rows = []
        for row in apiRowData[1:]:
            self.rows.append(SpreadSheetRow(row['values']))

    def htmlTable(self):
        result = "<table>\n"
        for row in self.rows:
            result += row.htmlRow()
        result += "</table>"
        return result


def get_authenticated_service():
    flow = InstalledAppFlow.from_client_secrets_file(CLIENT_SECRETS_FILE, SCOPES)
    credentials = flow.run_local_server(host='localhost',
                                        port=8080, 
                                        success_message='You may close this window.',
                                        open_browser=True)
    return build(API_SERVICE_NAME, API_VERSION, credentials=credentials)


def get_sheet(service, **kwargs):
    results = service.spreadsheets().get(**kwargs).execute()
    return results


def extractCells(sheet):
    return SpreadSheet(sheet['sheets'][0]['data'][0]['rowData'])


if __name__ == '__main__':
    service     = get_authenticated_service()
    sheet       = get_sheet(service, spreadsheetId=SHEET_ID, includeGridData=True)
    spreadsheet = extractCells(sheet)
    rule_interactions = []
    for row in spreadsheet.rows:
        ri = RuleInteraction()
        ri.loadData(row.values)
        rule_interactions.append(ri)
    rule_set = RuleSet(rule_interactions)
    print ("Total number of records: %d" % len(rule_interactions))
    theList = rule_set.toList()
    #result = json.loads(theList)
    result = "data = " + json.dumps(theList, indent=2, sort_keys = True) + ";"
    f = open("json_rules.js", "w+")
    f.write(result)
    f.close()
    
