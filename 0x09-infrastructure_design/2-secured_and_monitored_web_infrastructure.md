**Infrastructure Explanation:**

1. **Additional Elements:**
   - **Load Balancer:** Added for distributing incoming network traffic across multiple servers to ensure high availability and reliability.
   - **Firewalls:** Implemented for security by monitoring and controlling incoming and outgoing network traffic.
   - **HTTPS:** Used to encrypt data in transit between clients and servers for enhanced security.
   - **Monitoring Tool:** Employed to track system performance, detect issues, and ensure optimal operation.

2. **Firewalls:**
   - **Purpose:** Firewalls act as a barrier between a trusted internal network and untrusted external networks, controlling and filtering incoming and outgoing traffic based on predetermined security rules.
   
3. **HTTPS Traffic:**
   - **Purpose:** HTTPS encrypts the communication between clients and servers, preventing unauthorized access and protecting data integrity during transit.

4. **Monitoring:**
   - **Purpose:** Monitoring is essential for proactive issue detection, performance optimization, and ensuring system reliability.
   - **Data Collection:** Monitoring tools collect data through various methods, including log analysis, performance metrics, and system health checks.

5. **Monitoring Web Server QPS:**
   - **Steps:**
      1. Set up monitoring tool to track web server metrics.
      2. Define and configure a metric for monitoring Query Per Second (QPS).
      3. Monitor the QPS metric regularly and set up alerts for abnormal values.
      4. Investigate and address any issues causing fluctuations in QPS.

**Infrastructure Issues:**

1. **SSL Termination at Load Balancer:**
   - **Issue:** Terminating SSL at the load balancer leaves the internal network exposed to potential security risks as the traffic is decrypted before reaching backend servers.

2. **Single MySQL Server for Writes:**
   - **Issue:** Having only one MySQL server capable of accepting writes introduces a single point of failure. If this server goes down, write operations are affected, leading to service disruptions.

3. **Uniform Server Components:**
   - **Issue:** Uniformity in server components can lead to vulnerabilities. If a flaw is discovered in a particular component, all servers are susceptible, increasing the risk of widespread system compromise.


