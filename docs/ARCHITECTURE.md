# CLOUD-03 — System Architecture

## Overview

This project implements an HTTP reverse proxy architecture using Nginx and two FastAPI backend services managed through Docker Compose.

## Components

**Client**

Sends HTTP requests to `127.0.0.1:8080`.

**Nginx**

Receives incoming requests and distributes them to Backend A and Backend B through an upstream group.

**Backend A**

Runs a FastAPI application with the environment variable `SERVER_ID=backend-a`.

**Backend B**

Runs the same FastAPI application with the environment variable `SERVER_ID=backend-b`.

**Docker Compose**

Defines the services, internal networking, environment variables, and startup dependencies.

## Network Architecture

```text
          Windows / WSL2 Host
                   |
             127.0.0.1:8080
                   |
            Docker Network
                   |
              Nginx :80
                /     \
               /       \
              v         v
        backend-a     backend-b
          :8000         :8000
```

The backend service ports are not published to the host. Only Nginx exposes an HTTP endpoint through localhost.

## Load Balancing

Nginx distributes requests using the default round-robin upstream algorithm.

Each backend has the same weight.

## Dynamic Service Discovery

Docker Compose provides internal DNS resolution for service names.

The Nginx configuration uses Docker's embedded DNS resolver at `127.0.0.11` and the `resolve` parameter to update backend addresses.

## Failure Handling

When a backend is unavailable, Nginx may retry another upstream depending on the failure type and proxy configuration.

The experiment showed that backend failure can produce temporary HTTP timeouts.

The system does not guarantee uninterrupted availability.

## Limitations

- Single Nginx instance
- No active health-check scheduler
- No automatic scaling
- No TLS termination
- Local testing environment only

## Conclusion

The architecture demonstrates fundamental reverse proxy, load balancing, container networking, and service discovery concepts.
