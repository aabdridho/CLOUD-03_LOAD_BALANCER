# CLOUD-03 — Troubleshooting Documentation

## 1. Python Virtual Environment Error

**Problem**

`source .venv/bin/activate` returned:

`No such file or directory`

**Cause**

The Python virtual environment had not been created successfully because the required system package was unavailable.

**Resolution**

Installed `python3-venv`, recreated the virtual environment, and activated it.

## 2. Backend Failure and HTTP Timeouts

**Problem**

During Backend A failure simulation, some HTTP requests timed out.

**Cause**

The proxy experienced upstream connectivity failures during the test.

**Resolution**

Examined Docker Compose service status and Nginx logs, then restarted Backend A.

**Learning Outcome**

Backend failover does not automatically guarantee zero failed requests.

## 3. Nginx Restart Loop

**Problem**

The Nginx container repeatedly restarted.

**Error**

`host not found in upstream "backend-a:8000"`

**Cause**

Nginx could not resolve the Backend A hostname during startup.

**Resolution**

Restored Backend A and verified Nginx startup and HTTP connectivity.

## 4. Uneven Load Distribution

**Problem**

Initial load distribution tests showed requests being handled primarily by Backend A.

**Investigation**

Verified HTTP connectivity from Nginx to both backend services.

Inspected active upstream configuration using `nginx -T`.

**Resolution**

Updated Nginx configuration to support dynamic Docker DNS resolution.

The final 20-request test showed an even 10:10 distribution.

## 5. Git Repository Hygiene

**Problem**

The repository contained local Python virtual environments and Microsoft Word temporary files.

**Resolution**

Added appropriate ignore patterns to `.gitignore`.

**Learning Outcome**

Repositories should contain project source files and relevant documentation rather than local environment artifacts.

## Conclusion

The troubleshooting process demonstrated container debugging, upstream DNS diagnosis, HTTP testing, and operational recovery.
