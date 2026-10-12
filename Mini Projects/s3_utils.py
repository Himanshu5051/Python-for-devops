import boto3

s3 = boto3.client('s3')

#List of All Buckets-----
#  print(bucket.name)
    
    
    

#Upload a File to S3 Bucket------

file_name = r"C:\Users\himan\Documents\python_for_deveops\Mini Projects\api.py"
object_name = "api.py"
bucket_name = "devops-ai-py"

response = s3.upload_file(file_name,bucket_name,object_name)

print("File uploaded successfully!!")

def upload_to_s3(file_name,bucket_name,object_name):
    response = s3.upload_file(file_name,bucket_name,object_name)
    
    return response.json()

    
    