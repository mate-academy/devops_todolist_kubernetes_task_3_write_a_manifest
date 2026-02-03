Markdown
# ToDo App Kubernetes Deployment

## Prerequisites
- Docker installed and running
- Kubernetes cluster (e.g., Minikube, Docker Desktop)
- `kubectl` configured

## 1. Apply Manifests
Run the following commands to deploy the application and the testing pod:

```bash
# Create namespace
kubectl apply -f .infrastructure/namespace.yml

# Deploy ToDo App
kubectl apply -f .infrastructure/todoapp-pod.yml

# Deploy Busybox for internal testing
kubectl apply -f .infrastructure/busybox.yml
```
2. Test using Port-Forward
To access the application from your local machine:

```Bash
kubectl port-forward pod/todoapp-pod -n todoapp 8000:8000
Open http://localhost:8000 in your browser.
```
3. Test using Busybox (Internal Cluster Test)
To verify connectivity inside the cluster:

Get the IP address of the todoapp pod:

```Bash
kubectl get pod todoapp-pod -n todoapp -o wide
(Note the IP address, e.g., 10.1.0.15)

Enter the busybox container:
```
```Bash
kubectl exec -it busybox -n todoapp -- sh
Inside the container, run curl using the IP you found:
```
```Bash
curl <10.1.0.14>:8000/api/readiness/
You should see {"status": "ready"}.