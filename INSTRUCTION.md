# Instructions for Deploying and Testing the ToDo Application in Kubernetes

This document provides a step-by-step guide on how to deploy the ToDo application and verify its health (`livenessProbe`) and readiness (`readinessProbe`) statuses using built-in Kubernetes diagnostic tools.

---

## 1. Applying Kubernetes Manifests

Before proceeding, ensure your local Kubernetes cluster (Minikube or Docker Desktop) is running, and your updated Docker image has been successfully pushed to your registry.

Execute the following commands sequentially from the root directory of your repository:

```bash
# 1. Create the isolated namespace
kubectl apply -f src/.infrastructure/namespace.yml

# 2. Deploy the busybox debugging pod for in-cluster testing
kubectl apply -f src/.infrastructure/busybox.yml

# 3. Deploy the core ToDo application pod with configured probes
kubectl apply -f src/.infrastructure/todoapp-pod.yml

# The instruction of running and testing Todo ap in Kubernetes
## 1. Using Kubernetes's manifests
For unpackung the app execute next commands from the root directory of project:
```bash
kubectl apply -f .infrastructure/namespace.yml
kubectl apply -f .infrastructure/busybox.yml
kubectl apply -f .infrastructure/todoapp-pod.yml