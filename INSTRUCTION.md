# 🚀 ToDo App Deployment Instructions

This document describes how to deploy the ToDo Django application to a Kubernetes cluster, test its health/readiness endpoints, and interact with it using port forwarding and a BusyBox container.

## 📁 Prerequisites

- A Kubernetes cluster (e.g., local with minikube, or any remote cluster)
- kubectl configured and connected to your cluster
- Docker installed and logged in to Docker Hub
- Python 3.8+ installed (for local testing)

## 🐳 1. Pull Pre-Built Docker Image (Optional)

If you’d like to inspect or test the image locally, you can pull it from Docker Hub:

```sh
docker pull denyssheremeta/todoapp:3.0.0
```

`Note:` This step is optional — the Kubernetes manifests already reference this image and will pull it automatically during deployment.

## ☸️ 2. Apply Kubernetes Manifests

All required manifests are located in the .infrastructure folder. Apply them in the following order:

```sh
kubectl apply -f .infrastructure/namespace.yml
kubectl apply -f .infrastructure/busybox.yml
kubectl apply -f .infrastructure/todoapp.yml
```

## 🔁 3. Port-Forward to Access the App Locally

Once the pod is running, forward the container port to your local machine:

```sh
kubectl port-forward pod/todoapp -n todoapp 8000:8000
```

---

### Then you can:

- Open the app in a browser: http://localhost:8000
- Explore the API: http://localhost:8000/api/
- Test endpoints:

```sh
curl http://localhost:8000/health
curl http://localhost:8000/ready
```

## 🧪 4. Test Health & Readiness with busybox Pod

You can use the included BusyBox pod to verify the ToDo app from inside the cluster.

1. Open a shell in the BusyBox pod:

   ```sh
   kubectl exec -it busybox -n todoapp -- /bin/sh
   ```

2. Run curl commands from inside the pod:

   ```sh
   curl http://todoapp:8000/health
   curl http://todoapp:8000/ready
   ```
