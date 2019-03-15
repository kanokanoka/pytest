import hashlib

md5 = hashlib.md5(b"test").hexdigest()
print(md5)
