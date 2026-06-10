import mimetypes
import boto3
from dotenv import load_dotenv
import os
load_dotenv()
from flask import Flask, render_template, request, send_file
from io import BytesIO
app = Flask(__name__)

# AWS S3 Setup

s3 = boto3.client('s3')
BUCKET_NAME = "asna-cloud-file-manager"
response = s3.list_buckets()

print("\nBuckets found:\n")

for bucket in response["Buckets"]:
    print(bucket["Name"])
@app.route("/")
def home():
    response = s3.list_objects_v2(Bucket=BUCKET_NAME)
    files = []
    if "Contents" in response:
      for obj in response["Contents"]:
         files.append({"name": obj["Key"], "size": obj["Size"], "upload-date": obj["LastModified"], "owner": obj.get("Owner")})
    return render_template("index.html", files=files)


@app.route("/upload", methods=["POST"])
def upload_file():
    file = request.files["file"]

    if file:
        filename = file.filename
        s3.upload_fileobj(file,BUCKET_NAME,filename)
        return f"Uploaded: {filename}"

    return "No file selected"
@app.route("/delete", methods=["POST"])
def delete_file():
    filename = request.form["filename"]
    s3.delete_object(Bucket=BUCKET_NAME, Key=filename)
    return f"Deleted: {filename}"  
@app.route("/download", methods=["GET"])
def download_file():
    filename = request.args.get("filename")
    response = s3.get_object(Bucket=BUCKET_NAME, Key=filename)
    mime_type, _ = mimetypes.guess_type(filename)
    return send_file(BytesIO(response["Body"].read()), download_name=filename, as_attachment=True,mimetype=mime_type)

if __name__ == "__main__":
    app.run(debug=True)
