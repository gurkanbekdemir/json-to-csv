import ijson,json
from ijson import parse

class JsonParse():
  def __init__(self,JsonData,type):
    if type == "header":
      self.headers =self.header(JsonData)
    elif type == "rows":
      self.rows =self.row_parsing(JsonData)

  def header(self,data):
    headers = []
    for pfx, event, value in ijson.parse(data):
      if "start_map" == event or "end_map" == event or pfx =="":
        pass
      else:
        headers.append(pfx)
    return headers

  def row_parsing(self,data):
    rows = []
    for pfx, event, value in ijson.parse(data):

      if "start_map" == event or "end_map" == event or pfx == "":
        pass
      else:
        rows.append(value)
    return rows