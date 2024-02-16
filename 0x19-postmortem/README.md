# POSTMORTEM ABOUT ISSUE IN MY APACHE2:

![](https://i.pinimg.com/originals/26/8c/3f/268c3f0f74e4db0ee66cc875ad55d4fc.gif) 

## Issue Summary:

Duration of outage: The outage lasted for approximately 2 hours, from 14:00 to 16:00 UTC.
Impact: The Apache server experienced downtime, resulting in a 500 Internal Server Error for all incoming requests. Approximately 80% of users were affected, leading to service disruption and unavailability.
Root Cause: The root cause of the issue was identified as incorrect file permissions, causing Apache to fail in accessing necessary files and directories.

## Timeline:

14:00 UTC: Issue detected when monitoring alerts indicated a sudden increase in 500 Internal Server Error responses.
Detected through monitoring alerts.
Initial investigation focused on Apache error logs and system resource utilization.
Misleading paths included checking for network issues and examining Apache configuration files.
The incident was escalated to the DevOps team for further investigation and resolution.
16:00 UTC: The issue was resolved by identifying and correcting the incorrect file permissions on the Apache server.
Root Cause and Resolution:

## Root Cause: 

The issue was caused by incorrect file permissions, preventing Apache from accessing necessary files and directories.
Resolution: The incorrect file permissions were corrected using Puppet automation (0-strace_is_your_friend.pp), ensuring that Apache could access the required files and directories without errors.
Corrective and Preventative Measures:

## Improvement/Fixes:

Implement regular audits of file permissions on critical servers to identify and correct any discrepancies.
Enhance monitoring to proactively detect changes in server behavior and performance, allowing for early intervention in case of issues.
Tasks:

Implement Puppet manifests to automate the management of file permissions across servers.
Enhance monitoring alerts to provide more detailed information on server errors, facilitating quicker diagnosis and resolution.


