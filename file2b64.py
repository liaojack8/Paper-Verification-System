import base64
file = open('a.pdf', 'rb')
file_content = file.read()
print(file_content)
b64 = base64.b64encode(file_content)
print(b64.decode())