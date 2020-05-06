
İnput - {"item_1":"value_11",
   "item_2":"value_12",
   "item_3":"value_13",
   "item_4":["sub_value_14", "sub_value_15"],   "item_5":{       "sub_item_1":"sub_item_value_11","sub_item_2":["sub_item_value_12", "sub_item_value_13"]} }

output ['value_11', 'value_12', 'value_13', None, 'sub_value_14', 'sub_value_15', None, 'sub_item_1', 'sub_item_value_11', 'sub_item_2', None, 'sub_item_value_12', 'sub_item_value_13', None]

<br>

```python

import JsonToCsv, json
JSONDATA = your json data

with open('data.json', 'w') as f:
  json.dump(json.loads(JSONDATA), f)
   
file = open("data.json", encoding='utf8')
headers = JsonToCsv.JsonParse(file, "header").headers
row = JsonToCsv.JsonParse(file, "rows").rows
```

