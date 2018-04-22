import boto3

bucket_name = '203602mirek'
s3 = boto3.resource('s3')
bucket = s3.Bucket(bucket_name)

my_file = open('to_be_uploaded.txt', 'w+')
my_file.write('buuuuuu!')
my_file.close()

bucket.put_object(Key='omega/gamma/test.txt', Body=open('to_be_uploaded.txt', 'rb'))
