# CLOUD-03 — Load Balancer & Reverse Proxy Lab

## Overview

This project demonstrates the implementation of an Nginx reverse proxy and load balancer for two containerized FastAPI backend services using Docker Compose.

The laboratory explores HTTP request distribution, internal container networking, backend failure simulation, service recovery, and reverse proxy troubleshooting.

## Technology Stack

- Ubuntu WSL2
- Docker Engine
- Docker Compose
- Nginx
- Python
- FastAPI
- Uvicorn
- curl

## Architecture

```text
               HTTP Client
                   |
                   v
          localhost:8080
                   |
                   v
           Nginx Load Balancer
              /          \
             v            v
        Backend A      Backend B
         FastAPI        FastAPI
         Port 8000      Port 8000
```

Both backend services communicate with Nginx through an internal Docker Compose network.

## Project Structure

```text
CLOUD-03_LOAD_BALANCER/
├── backend/
│   ├── Dockerfile
│   ├── main.py
│   └── requirements.txt
├── nginx/
│   └── default.conf
├── docs/
│   ├── ARCHITECTURE.md
│   └── TROUBLESHOOTING.md
├── compose.yaml
├── .gitignore
├── README.md
└── CLOUD 03.docx
```

## Implementation

### Backend Development

Created a FastAPI application with two endpoints:

- `/` returns the responding backend's identity.
- `/health` returns application health information.

The same backend image is used for two service instances, identified through the `SERVER_ID` environment variable.

### Docker Containerization

Created a Dockerfile to package the Python application and its dependencies.

### Reverse Proxy Configuration

Configured Nginx to distribute HTTP requests across Backend A and Backend B using round-robin load balancing.

### Dynamic DNS Resolution

Configured Nginx to use Docker's internal DNS resolver at `127.0.0.11` and dynamically resolve backend service names.

### Failure Simulation

Stopped Backend A to observe how Nginx handled backend unavailability.

The experiment revealed HTTP timeouts and an upstream hostname resolution failure during troubleshooting.

### Load Balancing Verification

After updating the Nginx configuration, the final test successfully distributed 20 HTTP requests:

| Backend | Requests | Distribution |
|---|---:|---:|
| Backend A | 10 | 50% |
| Backend B | 10 | 50% |

Both backend instances successfully responded through the Nginx endpoint.

## How to Run

### Requirements

- Docker Engine
- Docker Compose

### Start the Services

```bash
docker compose up -d --build
```

### Verify Containers

```bash
docker compose ps
```

### Test the Reverse Proxy

```bash
curl http://127.0.0.1:8080/
```

### Test Load Distribution

```bash
for i in $(seq 1 20); do
  curl -sS http://127.0.0.1:8080/
  echo
done
```

### Stop the Services

```bash
docker compose down
```

## Key Learning Outcomes

- Nginx reverse proxy configuration
- Round-robin load balancing
- Docker containerization
- Docker Compose networking
- Internal DNS resolution
- Backend failure simulation
- Reverse proxy troubleshooting
- Service recovery

## Limitations

This laboratory uses a single Nginx instance and does not provide full high availability.

The `/health` endpoint is an application endpoint, not an active Nginx health-check mechanism.

## Author

Abdurrasyid Ridho

Computer Engineering — Cloud Engineering Portfolio
