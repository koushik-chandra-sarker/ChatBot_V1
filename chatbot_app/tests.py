from django.test import TestCase
import json
# Create your tests here.
res = "sds"
x = {"message": res}
y = json.dumps(x)
print(y)