# -*- coding: utf-8 -*-
# flake8: noqa

from qiniu import Auth
from qiniu import BucketManager

access_key = '...'
secret_key = '...'

bucket_name = 'Bucket_Name'

q = Auth(access_key, secret_key)

bucket = BucketManager(q)

url = 'http://7xr875.com1.z0.glb.clouddn.com/test.jpg'

key = 'test.jpg'

ret, info = bucket.fetch( url, bucket_name, key)
print(info)
assert ret['key'] == key
