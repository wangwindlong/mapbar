location = "province=内蒙古;city=阿拉善;coord=105.68908,38.84287"
details = location.split(";")


def getdict(item):
    result = dict()
    s = item.split("=")
    result[s[0]] = s[1]
    return result


address = dict()
for detail in details:
    address = {**address, **getdict(detail)}
print(address['province'])
