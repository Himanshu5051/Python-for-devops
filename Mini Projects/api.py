from fastapi import FastAPI

from system_utils import get_system_details
import boto3

s3 = boto3.resource('s3')
app = FastAPI(title="Devops APIs")

@app.get("/hello")
def hello():
    return{"message" : "Hello Dosto,Welcome to Devops APIs"}

@app.get("/metrics")
def metrics():
    """
    This Metrics show Sytem details like
    CPU, MEMORY, DISK, etc
    """
    
    return get_system_details()
    
@app.get("/aws/s3")
def get_buckets():
    buckets = []
    for bucket in s3.buckets.all():
     buckets.append(bucket.name)
            
    return buckets
