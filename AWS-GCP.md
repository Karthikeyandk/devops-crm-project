# AWS & GCP Cloud Platforms

## 1. Introduction to Cloud Computing

Cloud computing means using computing resources such as servers, storage, databases, networking, and software services over the internet instead of maintaining all infrastructure locally.

Cloud platforms provide on-demand resources that can be scaled according to application requirements.

Two major cloud platforms are:

* Amazon Web Services (AWS)
* Google Cloud Platform (GCP)

Both platforms provide services for compute, storage, databases, networking, security, monitoring, analytics, and application development.

---

## 2. AWS Overview

Amazon Web Services (AWS) is a cloud platform that provides a wide range of infrastructure and managed services.

AWS can be used to build, deploy, and operate applications without maintaining physical servers directly.

The main AWS service categories relevant to application development include:

* Compute
* Storage
* Databases
* Networking
* Security and Identity
* Serverless Computing
* Monitoring

---

## 3. Important AWS Services

### 3.1 Amazon EC2

Amazon Elastic Compute Cloud (EC2) provides virtual servers in the AWS cloud.

EC2 can be used when an application requires control over the operating system, installed software, networking, and server configuration.

Typical use cases include:

* Hosting web applications
* Running backend services
* Running development environments
* Running custom workloads

### 3.2 Amazon S3

Amazon Simple Storage Service (S3) is an object storage service.

It can be used to store:

* Images
* Videos
* Documents
* Backups
* Application files
* Logs

S3 stores data as objects inside buckets.

### 3.3 Amazon RDS

Amazon Relational Database Service (RDS) is a managed relational database service.

Instead of manually maintaining a database server, RDS handles many infrastructure and operational tasks.

It can be used for application databases such as:

* PostgreSQL
* MySQL
* MariaDB
* SQL Server
* Oracle

### 3.4 Amazon VPC

Amazon Virtual Private Cloud (VPC) provides networking isolation for AWS resources.

A VPC can contain resources such as:

* Subnets
* Route tables
* Security controls
* Network connections

For example, an application server can be placed inside a private network while controlled access is provided to required services.

### 3.5 AWS IAM

AWS Identity and Access Management (IAM) controls access to AWS resources.

IAM can be used to define:

* Users
* Groups
* Roles
* Permissions
* Policies

The main purpose is to ensure that users and applications receive only the permissions they require.

### 3.6 AWS Lambda

AWS Lambda is a serverless compute service.

It allows code to run without managing a traditional server.

Lambda is useful for event-driven workloads and short-running application logic.

### 3.7 Amazon CloudWatch

Amazon CloudWatch provides monitoring and observability capabilities.

It can be used to monitor:

* Application metrics
* Infrastructure metrics
* Logs
* Events
* Alarms

---

## 4. AWS Architecture Understanding

A simple web application architecture on AWS could be:

```text
                         Internet
                            |
                            v
                    +---------------+
                    |     VPC       |
                    |               |
                    |   +-------+   |
                    |   |  EC2  |   |
                    |   |  App  |   |
                    |   +---+---+   |
                    |       |       |
                    +-------|-------+
                            |
              +-------------+-------------+
              |                           |
              v                           v
          +-------+                    +-----+
          |  RDS  |                    | S3  |
          |  DB   |                    |Files|
          +-------+                    +-----+
```

In this example:

* EC2 runs the application.
* RDS stores relational application data.
* S3 stores files and objects.
* CloudWatch can monitor the application and infrastructure.
* IAM controls access to AWS resources.

---

## 5. GCP Overview

Google Cloud Platform (GCP), commonly called Google Cloud, is Google's cloud computing platform.

Google Cloud provides services for computing, storage, databases, networking, security, analytics, application development, and other workloads.

Google Cloud resources are organized within projects. Projects provide a way to organize resources, permissions, and billing-related configuration.

Google Cloud services can be accessed through:

* Google Cloud Console
* Google Cloud CLI (`gcloud`)
* Cloud Shell
* Client libraries
* Infrastructure as Code tools such as Terraform

---

## 6. Important GCP Services

### 6.1 Compute Engine

Compute Engine provides virtual machines that run workloads on Google Cloud.

It is similar in concept to Amazon EC2.

Typical use cases include:

* Hosting applications
* Running backend services
* Running custom workloads
* Creating development and testing environments

### 6.2 Cloud Storage

Cloud Storage is an object storage service.

It can be used to store:

* Images
* Videos
* Documents
* Backups
* Application files
* Large datasets

Data is stored as objects inside buckets.

### 6.3 Cloud SQL

Cloud SQL is a managed relational database service.

It supports common relational database engines such as:

* MySQL
* PostgreSQL
* SQL Server

Cloud SQL reduces the amount of database infrastructure management required from the application team.

### 6.4 Google Cloud VPC

Google Cloud Virtual Private Cloud (VPC) provides networking capabilities for cloud resources.

It allows applications and services to communicate through controlled networks.

Networking concepts include:

* VPC networks
* Subnets
* Routes
* Firewall rules
* IP addresses

### 6.5 Google Cloud IAM

Google Cloud Identity and Access Management (IAM) controls access to Google Cloud resources.

IAM can be used to manage:

* Principals
* Roles
* Permissions
* Policies

The goal is to provide appropriate access to users and applications.

### 6.6 Cloud Run

Cloud Run is a managed platform for running containerized applications.

It is useful when an application has already been packaged as a container and does not require direct management of virtual machines.

### 6.7 BigQuery

BigQuery is Google's data warehouse and analytics platform.

It can be used to analyze large datasets and run analytical queries.

It is especially useful for:

* Business analytics
* Data analysis
* Reporting
* Large-scale datasets

---

## 7. GCP Architecture Understanding

A simple web application architecture on GCP could be:

```text
                         Internet
                            |
                            v
                    +---------------+
                    |   Google Cloud|
                    |      VPC      |
                    |               |
                    |  +----------+ |
                    |  | Compute  | |
                    |  |  Engine  | |
                    |  +----+-----+ |
                    +-------|-------+
                            |
              +-------------+-------------+
              |                           |
              v                           v
         +----------+               +------------+
         | Cloud SQL|               |   Cloud    |
         | Database |               |  Storage   |
         +----------+               +------------+
```

In this example:

* VPC provides the networking environment.
* Compute Engine runs the application.
* Cloud SQL stores relational application data.
* Cloud Storage stores objects and files.
* IAM controls access to resources.
* Cloud Monitoring can be used for monitoring and observability.

---

## 8. AWS vs GCP Comparison

AWS and GCP provide similar cloud capabilities, but the service names and specific implementations are different.

| Requirement                     | AWS                    | GCP                         |
| ------------------------------- | ---------------------- | --------------------------- |
| Virtual Machines                | EC2                    | Compute Engine              |
| Object Storage                  | S3                     | Cloud Storage               |
| Managed Relational Database     | RDS                    | Cloud SQL                   |
| Networking                      | VPC                    | VPC                         |
| Identity & Access               | IAM                    | IAM                         |
| Serverless / Container Platform | Lambda / ECS / Fargate | Cloud Run / Cloud Functions |
| Data Warehouse                  | Redshift               | BigQuery                    |
| Monitoring                      | CloudWatch             | Cloud Monitoring            |
| Command Line                    | AWS CLI                | gcloud CLI                  |
Both platforms support similar fundamental cloud concepts:


* Compute
* Storage
* Databases
* Networking

* Identity and access management
* Monitoring
* Scalability
* Automation


The main difference is how each cloud provider implements and integrates these capabilities.


---


## 9. Real-World Application Example


Consider a CRM application similar to the application used in this project.


A cloud deployment could contain:


```text
                         Users
                           |
                           v

                    Load Balancer

                           |
                           v
                    Application Layer
                           |
              +------------+------------+

              |                         |
              v                         v
         Database                  Object Storage
              |                         |

              v                         v
       Customer Records          Files / Documents

```

For AWS, this could be implemented using services such as:


* EC2 or another compute service for the application
* RDS for relational database storage

* S3 for files
* VPC for networking
* IAM for access control
* CloudWatch for monitoring


For GCP, equivalent services could include:

* Compute Engine or Cloud Run for the application

* Cloud SQL for relational database storage
* Cloud Storage for files

* VPC for networking
* IAM for access control
* Cloud Monitoring for monitoring

This demonstrates that cloud platforms provide building blocks that can be combined according to application requirements.


---

## 10. Security and Access Management

Security is an important part of cloud infrastructure.

Both AWS and GCP provide identity and access management systems.

The main principles I learned are:

* Give users only the permissions they require.
* Avoid using highly privileged accounts for normal tasks.
* Use roles and policies to control access.
* Keep API keys and credentials private.
* Do not commit secrets to Git repositories.
* Separate development and production environments where appropriate.
* Monitor access and application activity.

IAM is therefore not only about creating users; it is also about controlling which resources users and applications can access.

---

## 11. Scalability and Cost

One major advantage of cloud computing is the ability to scale resources according to workload requirements.

For example:

```text
Low traffic
    |
    v
Small compute capacity
    |
    |  Traffic increases
    v
More compute capacity
```

Cloud platforms also provide different pricing models and tools for estimating and monitoring costs.

Instead of purchasing physical servers upfront, organizations can provision cloud resources based on their requirements and manage usage and costs over time.

However, cloud resources still need to be monitored carefully because unnecessary or incorrectly configured resources can increase costs.

---

## 12. What I Learned

Through this task, I learned that AWS and GCP are cloud platforms that provide many managed services instead of requiring organizations to maintain all infrastructure themselves.

My main understanding is:

1. Compute services run applications and workloads.
2. Storage services store files and objects.
3. Database services provide managed data storage.
4. Networking services control communication between resources.
5. IAM controls access and permissions.
6. Monitoring services help observe applications and infrastructure.
7. Serverless and managed container services can reduce infrastructure management.
8. Cloud services can be combined to build complete application architectures.
9. AWS and GCP provide similar cloud capabilities but use different service names and implementations.
10. Security, scalability, and cost management are important when designing cloud infrastructure.

---

## 13. Conclusion

AWS and GCP provide flexible cloud infrastructure for building and operating modern applications.

AWS provides services such as EC2, S3, RDS, VPC, IAM, Lambda, and CloudWatch.

GCP provides services such as Compute Engine, Cloud Storage, Cloud SQL, VPC, IAM, Cloud Run, and BigQuery.

Although the service names differ, both platforms provide the fundamental capabilities required to build scalable cloud applications.

This task helped me understand the basic architecture of cloud platforms and how different cloud services work together to support an application.

---

## 14. Loom Demonstration

The Loom video explains the concepts covered in this document, including:

* Introduction to cloud computing
* AWS overview
* Important AWS services
* GCP overview
* Important GCP services
* AWS vs GCP comparison
* Real-world application architecture
* Key learnings

Loom Video:

https://www.loom.com/share/3ef8578a879344f18acd4f91cd3d2926
