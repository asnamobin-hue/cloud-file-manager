# Cloud File Manager

## Project Preview

![Screenshot](screenshots/Screenshot (271).png)

## Overview

Cloud File Manager is a web application built with Flask and Amazon S3 that allows users to upload files through a browser and store them securely in cloud storage.

The project was developed to gain hands-on experience with backend development, AWS cloud services, IAM authentication, environment variable management, and the boto3 SDK.

---

## Features

* Upload files through a web interface
* Store uploaded files in Amazon S3
* AWS IAM-based authentication
* Secure configuration using environment variables
* Flask-powered backend for request handling

---

## Architecture

```text
User
 │
 ▼
Web Browser
 │
 ▼
Flask Application
 │
 ▼
boto3 SDK
 │
 ▼
Amazon S3 Bucket
```

---

## Tech Stack

| Category          | Technology    |
| ----------------- | ------------- |
| Language          | Python        |
| Backend Framework | Flask         |
| Cloud Storage     | Amazon S3     |
| AWS SDK           | boto3         |
| Configuration     | python-dotenv |
| Frontend          | HTML          |

---

## Project Structure

```text
cloud-file-manager/
├── app.py
├── requirements.txt
├── README.md
├── templates/
│   └── index.html
└── .gitignore
```

---

## Learning Outcomes

This project helped me understand:

* Flask routing and request handling
* File uploads using HTTP POST requests
* AWS IAM users and access credentials
* Amazon S3 object storage
* Integration of AWS services using boto3
* Environment variable management with `.env`
* Building an end-to-end cloud-based application

---

## Current Workflow

1. User selects a file through the web interface.
2. Flask receives the uploaded file.
3. boto3 authenticates with AWS using IAM credentials.
4. The file is uploaded to an Amazon S3 bucket.
5. A success response is returned to the user.

---

## Future Enhancements

* Display files stored in S3
* Download files from S3
* Delete files from S3
* File type validation
* File size restrictions
* Improved frontend UI
* Deployment on AWS EC2

---

## Author

Built as a hands-on cloud and backend development project using Flask and AWS.
