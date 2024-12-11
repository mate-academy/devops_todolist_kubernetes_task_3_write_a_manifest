# Instructions for ToDo App Deployment and Testing

## Prerequisites
Ensure you have the following installed:
- Kubernetes cluster (Minikube, Kind, or other).
- kubectl (configured to access your cluster).
- Docker (to build and push images).

---

## Steps to Deploy the Application

### 1. Create a Namespace
Apply the namespace manifest to create the `todoapp` namespace:
```bash
kubectl apply -f .infrastructure/namespace.yml
