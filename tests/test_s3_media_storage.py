import unittest
from media.s3_storage import S3MediaStorage

class TestS2Storage(unittest.TestCase):

  def test_it_allow_store_files(self):
    storage = self.there_is_s3_storage()
    file_to_up = self.there_is_file() 

    storage.save(path="my/test/path.txt", file_to_be_uploaded = file_to_up)

    assert storage.contains(pate='my/test/path.txt')

  def there_is_s3_storage(self):
    return S3MediaStorage()

  def there_is_file(self):
    pass 
