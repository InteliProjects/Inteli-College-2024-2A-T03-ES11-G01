import os
from dotenv import load_dotenv
import supabase

Client = supabase.Client
create_client = supabase.create_client
from prefect import task

load_dotenv()

url = os.getenv("SUPABASE_URL")
key = os.getenv("SUPABASE_KEY")
supabase: Client = create_client(url, key)

def create_bucket(bucket_name): 
  buckets = list_buckets()

  # Check if the bucket already exists
  if not buckets or not any(bucket['name'] == bucket_name for bucket in buckets):
    # Create the bucket
    res = supabase.storage.create_bucket(bucket_name)
    return res
  else:
    print(f"Bucket '{bucket_name}' already exists.")
    return {"error": "already exists"}

def get_bucket(bucket_name):
  res = supabase.storage.get_bucket(bucket_name)
  print(res)
  return res

def list_buckets():
  res = supabase.storage.list_buckets()
  
  buckets_list = []
  for bucket in res:
    bucket_dict = {
      "id": bucket.id,
      "name": bucket.name,
      "owner": bucket.owner,
      "public": bucket.public,
      "created_at": bucket.created_at.isoformat(),  # Convert datetime to ISO format
      "updated_at": bucket.updated_at.isoformat(),  # Convert datetime to ISO format
      "file_size_limit": bucket.file_size_limit,
      "allowed_mime_types": bucket.allowed_mime_types
    }
    buckets_list.append(bucket_dict)
    
  return buckets_list

def clear_bucket(bucket_name):
  res = supabase.storage.empty_bucket(bucket_name)
  print(res)
  return res

def delete_bucket(bucket_name):
  res = supabase.storage.delete_bucket(bucket_name)
  print(res)
  return res

def upload_file(bucket_name, filepath, filename):
  with open(filepath, 'rb') as file:
    res = supabase.storage.from_(bucket_name).upload(filename, file)
    print("Success to upload")
  
  return res

def download_file(bucket_name, filename, local_path):
  file_data = supabase.storage.from_(bucket_name).download(filename)

    # Write the file to the specified destination
  with open(local_path, 'wb') as f:
      f.write(file_data)  # file_data is already in bytes

  return  f"File downloaded successfully to {local_path}"
