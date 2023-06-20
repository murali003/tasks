import json
data = '{"key1" : "value1", "key2" : "value2"}'
result = json.loads(data)
print(result['key2'])