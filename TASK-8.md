\# Task 8: AWS Observability



\## Objective



The objective of this task is to explore AWS observability and monitoring services,

understand their purpose and use cases, and document the learnings.



\---



\## 1. Amazon CloudWatch



Amazon CloudWatch is AWS's monitoring and observability service.



\### Purpose

\- Monitor AWS resources and applications

\- Collect metrics and logs

\- Create alarms

\- Build dashboards

\- Analyze operational data



\### Important Features

\- Metrics

\- Logs

\- Alarms

\- Dashboards

\- Logs Insights

\- Application Signals

\- Synthetics

\- Real User Monitoring (RUM)



\### Example



EC2 metrics such as CPU utilization, NetworkIn, NetworkOut,

DiskReadOps and DiskWriteOps can be monitored using CloudWatch Metrics.



\---



\## 2. CloudWatch Metrics



CloudWatch Metrics are time-series data used to monitor resource

and application performance.



\### Metrics options explored



\- Query Studio

\- Classic Metrics

\- Explorer

\- Streams



\### Learning



Classic Metrics can be used to browse metrics by AWS service.

For example, EC2 provides metrics such as CPU utilization and

network traffic.



\---



\## 3. CloudWatch Logs



CloudWatch Logs is used to collect, store and analyze log data

from applications, servers and AWS services.



\### Use cases



\- Application troubleshooting

\- Error investigation

\- Server log monitoring

\- Operational analysis



\---



\## 4. CloudWatch Alarms



CloudWatch Alarms monitor metrics against configured thresholds.



\### Use cases



\- Detect high CPU utilization

\- Detect application/resource problems

\- Trigger notifications or automated actions



\### Issue Encountered



While exploring CloudWatch, the console displayed a permission

error for `CloudWatch:DescribeAlarms`.



This was an IAM permission limitation and not an application setup issue.



\---



\## 5. CloudWatch Application Signals



Application Signals provides application performance monitoring

and helps understand application health, latency, faults and

service dependencies.



\### Use cases



\- Monitor application health

\- Track latency

\- Identify faults

\- Understand application dependencies

\- Monitor service-level indicators (SLIs)



\---



\## 6. AWS X-Ray



AWS X-Ray provides distributed tracing for applications.



\### Purpose



It helps understand how requests travel through multiple

services and helps identify latency and performance bottlenecks.



\### Use cases



\- Distributed tracing

\- Request analysis

\- Performance troubleshooting

\- Finding service dependencies



\---



\## 7. AWS CloudTrail



AWS CloudTrail records AWS API activity and account activity.



\### Purpose



It helps identify:



\- Who performed an action

\- What action was performed

\- When the action happened

\- Which AWS resource was affected



\### Use cases



\- Auditing

\- Security investigation

\- Compliance

\- Tracking AWS API activity



\---



\## 8. AWS Config



AWS Config provides resource configuration history and

configuration/compliance monitoring.



\### Use cases



\- Track resource configuration changes

\- Evaluate compliance

\- Audit AWS resource configurations

\- Detect configuration changes



\---



\## 9. AWS Distro for OpenTelemetry (ADOT)



AWS Distro for OpenTelemetry is AWS's distribution of

OpenTelemetry.



It can collect telemetry such as metrics and traces and send

them to observability backends.



\### Possible destinations



\- Amazon CloudWatch

\- AWS X-Ray

\- Amazon OpenSearch Service

\- Amazon Managed Service for Prometheus



\### Learning



ADOT allows applications to be instrumented using OpenTelemetry

and telemetry can be sent to multiple monitoring solutions.



\---



\## 10. Amazon Managed Service for Prometheus



Amazon Managed Service for Prometheus is a managed monitoring

service compatible with the open-source Prometheus ecosystem.



\### Use cases



\- Collect and query Prometheus metrics

\- Monitor containerized workloads

\- Kubernetes monitoring

\- Application and infrastructure metrics



\---



\## 11. Amazon Managed Grafana



Amazon Managed Grafana provides managed Grafana dashboards

for visualizing and analyzing observability data.



\### Use cases



\- Create monitoring dashboards

\- Visualize metrics

\- Analyze operational data

\- Combine data from different sources



\---



\## 12. Amazon OpenSearch Service



Amazon OpenSearch Service can be used for searching,

analyzing and visualizing logs and observability data.



\### Use cases



\- Log analysis

\- Application performance monitoring

\- Search and investigation

\- Observability dashboards



\---



\## 13. AWS Control Tower



AWS Control Tower helps manage and govern multi-account AWS

environments.



\### Observability-related use cases



\- Centralized governance

\- Monitoring account activity

\- Compliance visibility

\- Organization-level controls



\---



\# Observability Signals



The three important observability signals are:



1\. Metrics

2\. Logs

3\. Traces



\### Metrics



Numerical time-series data representing system or application

performance.



Example:

CPU utilization = 65%



\### Logs



Detailed records of events generated by applications and systems.



Example:

Application error logs.



\### Traces



Records showing how a request travels through distributed services.



Example:

User request → API Gateway → Lambda → DynamoDB



\---



\# AWS Observability Architecture - High Level



Application / Infrastructure

&#x20;       |

&#x20;       v

Metrics + Logs + Traces

&#x20;       |

&#x20;       v

CloudWatch / ADOT / X-Ray

&#x20;       |

&#x20;       +----> CloudWatch

&#x20;       |

&#x20;       +----> X-Ray

&#x20;       |

&#x20;       +----> Managed Prometheus

&#x20;       |

&#x20;       +----> OpenSearch

&#x20;       |

&#x20;       +----> Managed Grafana

&#x20;       |

&#x20;       v

Monitoring / Analysis / Troubleshooting



\---



\# Key Learnings



Through this task I learned that AWS observability is not

limited to monitoring CPU or memory.



Different observability tools serve different purposes:



\- CloudWatch → General AWS monitoring, metrics, logs and alarms

\- Application Signals → Application performance monitoring

\- X-Ray → Distributed tracing

\- CloudTrail → API activity and auditing

\- AWS Config → Resource configuration and compliance

\- ADOT → OpenTelemetry-based telemetry collection

\- Managed Prometheus → Prometheus metrics monitoring

\- Managed Grafana → Metrics visualization and dashboards

\- OpenSearch → Log and observability data analysis

\- Control Tower → Multi-account governance and compliance



The three major observability signals are metrics, logs and traces.



\---



\# Issues Encountered



While exploring CloudWatch, the following permission error was

observed:



`CloudWatch:DescribeAlarms`



The error indicated that the current IAM identity did not have

permission to retrieve alarms.



This was documented as an IAM permission limitation.



\---



\# Conclusion



AWS provides a complete observability ecosystem for monitoring

infrastructure, applications and distributed systems.



CloudWatch provides the core monitoring capabilities, while

services such as X-Ray, Application Signals, ADOT, Managed

Prometheus, Managed Grafana and OpenSearch provide specialized

observability capabilities.



This task helped me understand how metrics, logs and traces work

together for monitoring, troubleshooting and improving application

reliability.

