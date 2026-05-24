# Instructions for Deploying and Testing the Django ToDo Application

This document provides step-by-step instructions on how to deploy the ToDo application manifests to a Kubernetes cluster and verify its functionality.

---

## 1. How to Apply the Manifests

Make sure you are in the root directory of the project. Apply the Kubernetes manifests in the exact order listed below to ensure dependencies (like the namespace) are created first.

### Step 1: Create the Namespace
```
kubectl apply -f .infrastructure/namespace.yml
```
### Step 2: Deploy the ToDo Application Pod
```
kubectl apply -f .infrastructure/todoapp-pod.yml
```
### Step 3: Deploy the Testing BusyBox Pod
```
kubectl apply -f .infrastructure/busybox.yml
```
## Verification
Check the status of the deployed pods inside the todoapp namespace:

```
kubectl get pods -n todoapp
```
Note: Wait until the todoapp pod reaches 1/1 Running status. This might take a few seconds as database migrations run on startup.

## 2. Testing the Application via Port-Forward
To test the interactive UI and browse the application directly from your local machine, use the port-forward command.

Run the port-forwarding command to map port 8080 of the pod to your local port 8080:

```
kubectl port-forward pod/todoapp 8080:8080 -n todoapp
```
Open your web browser or use curl to access the application:

Landing Page: http://localhost:8080/

API Root: http://localhost:8080/api/

Readiness Probe Endpoint: http://localhost:8080/api/ready

Liveness Probe Endpoint: http://localhost:8080/api/health

## 3. Testing the Application via BusyBox Container
To verify internal cluster connectivity and ensure the probes are responding properly within the same network namespace, use the busyboxplus:curl container.

Exec into the running busybox container interactively:

```
kubectl exec -it busybox -n todoapp -- sh
```
Inside the container shell, test the endpoints of the todoapp pod using its internal IP address or DNS name (if services are configured), or directly via the Pod IP. Since it's in the same namespace, you can target the application pod directly.
(Alternatively, if testing by Pod IP, find it via kubectl get pod todoapp -n todoapp -o wide).

If testing directly within the cluster network to the local pod instance, run:

### Test Liveness Probe
```
curl http://todoapp:8080/api/health
```

### Test Readiness Probe
```
curl http://todoapp:8080/api/ready
```
Type exit to close the container session when finished.