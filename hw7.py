from pwn import *

r = remote("167.172.231.203", 8888)

def getFormats(str):
    splitList = str.split("format")
    return splitList[1].split(")")[0][2:], splitList[2].split(")")[0][2:]

def getData(str):
    data1 = str.split("XOR the following: ")[1].split(" (")[0]
    data2 = str.split("AND ")[1].split(" (")[0]
    return data1, data2

def convertToBytes(data, format):
    if format == "bytearray":
        return bytes(bytearray(eval(data)))
    elif format == "integer":
        return int(data).to_bytes(length = math.floor(math.log(int(data), 2))//8 + 1, byteorder='big')
    elif format == "string":
        return str.encode(data, "iso-8859-1")
    elif format == "hexdigest":
        return bytes.fromhex(data)
r.recv()
for i in range(100):
    output = r.recv().decode("iso-8859-1")
    print(output)
    type1, type2 = getFormats(output)
    data1, data2 = getData(output)
    print(data1, data2)
    byteData1 = convertToBytes(data1, type1)
    byteData2 = convertToBytes(data2, type2)
    print(byteData1, byteData2)
    result = "".join(chr(a ^ b) for a,b in zip(byteData1, byteData2))
    print(result)
    r.send(result)
    print(r.recv())
print(r.recv())