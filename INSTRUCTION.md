# Instructions for Deploying and Testing ToDo App on Kubernetes

This document provides instructions to deploy and test the ToDo application using Kubernetes manifests and the `busyboxplus:curl` container.

---

## 1. Prerequisites

* Kubernetes cluster up and running
* `kubectl` configured to communicate with your cluster
* Docker installed and logged in to your Docker Hub account
* Python 3.8+ and required dependencies installed for building the Docker image

---

## 2. Apply Kubernetes Manifests

All manifests are located in the `.infrastructure` folder. To create the resources:

### Step 1: Create Namespace

```bash
kubectl apply -f .infrastructure/namespace.yml
```

This will create the `todoapp` namespace.

---

### Step 2: Deploy BusyBox Pod

```bash
kubectl apply -f .infrastructure/busybox.yml
```

This pod uses the `ikulyk404/busyboxplus:curl` image and will be useful for testing network connectivity and API endpoints from within the cluster.

---

### Step 3: Deploy ToDo App Pod

```bash
kubectl apply -f .infrastructure/todoapp-pod.yml
```

This pod uses your Docker Hub image (`kenu21/todoapp:3.0.0`) and exposes port 8000.

It includes:

* **Readiness Probe**: Checks `/ready` endpoint to determine when the app is ready to serve requests.
* **Liveness Probe**: Checks `/health` endpoint to determine if the pod is still alive.

---

## 3. Test ToDo Application

### Option 1: Using Port-Forward

Forward the pod port to your local machine:

```bash
kubectl port-forward pod/todoapp -n todoapp 8000:8000
```

Then, open your browser and navigate to:

```
http://localhost:8000/
```

You should see the landing page of the ToDo application.
API endpoints are available under:

```
http://localhost:8000/api/
```

---

### Option 2: Using BusyBox Pod and curl

Get the IP address of the ToDo pod from your local machine:

```
kubectl get pod todoapp -n todoapp -o wide
```

Open a shell inside the BusyBox pod:

```
kubectl exec -it busybox -n todoapp -- sh
```

Test the ToDo API endpoints using curl with the pod IP:

Replace <POD_IP> with the actual IP

```
curl http://<POD_IP>:8000/api/ready
```

```
curl http://<POD_IP>:8000/api/health
```

 Example: List all ToDo items

```
curl http://<POD_IP>:8000/api/todos/
```

⚠️ Note: Pod IPs are ephemeral. If the pod restarts, its IP may change.
For stable access within the cluster, consider creating a Service that points to the ToDo pod.

---

## 4. Notes

* The **readiness probe** ensures the pod is marked ready only after the startup period of 40 seconds.
* The **liveness probe** ensures the pod is restarted if it becomes unhealthy.
* All manifests should be applied in the `todoapp` namespace.
* The Docker image `kenu21/todoapp:3.0.0` must exist on Docker Hub before applying the pod manifest.

---
