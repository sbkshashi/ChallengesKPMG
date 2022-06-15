object = {"a":{"b":{"c":"d"}}}

print(object.get("a"))
print(object.get('a', {}).get('b'))
print(object.get('a', {}).get('b',{}).get('c'))
print(object.get("d", "Not Found ! "))