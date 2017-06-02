
import base64

str = "Hello World!!"

base64_str = base64.b64encode(str)
print base64_str
print base64.b64decode(base64_str)

# + >>> -
# / >>> _
base64_str = base64.urlsafe_b64encode(str)
print base64_str
print base64.urlsafe_b64decode(base64_str)

