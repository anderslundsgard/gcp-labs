import sys
from google.cloud import storage

hello = 'Hello World'

print(f'{hello} with Python {sys.version}')

storage_client = storage.Client()
buckets = storage_client.list_buckets()

for bucket in buckets:
    print(bucket.name)
