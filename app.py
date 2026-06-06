import boto3
from dotenv import load_dotenv
import os
load_dotenv()
from flask import Flask, render_template, request

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
    return render_template("index.html")


@app.route("/upload", methods=["POST"])
def upload_file():
    file = request.files["file"]

    if file:
        filename = file.filename
        s3.upload_fileobj(file,BUCKET_NAME,filename)
        return f"Uploaded: {filename}"

    return "No file selected"


if __name__ == "__main__":
    app.run(debug=True)
