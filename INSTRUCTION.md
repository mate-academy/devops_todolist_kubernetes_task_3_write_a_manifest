# Instructions for Deploying and Testing ToDo Application

## 1. How to Apply Manifests
Apply all Kubernetes manifests in the correct order using the following commands from the root directory:

```bash
# Create the namespace first
kubectl apply -f .infrastructure/namespace.yml

# Deploy the ToDo application pod
kubectl apply -f .infrastructure/todoapp-pod.yml

# Deploy the busybox testing pod
kubectl apply -f .infrastructure/busybox.yml
```

To verify that pods are running successfully:
```bash
kubectl get pods -n todoapp
```

---

## 2. How to Test the Application using Port-Forward
You can access the ToDo application from your local machine browser by forwarding the cluster port:

```bash
kubectl port-forward pod/todoapp 8000:8000 -n todoapp
```

Now, open your browser and navigate to:
* **Landing Page:** [http://localhost:8000](http://localhost:8000)
* **Liveness Probe:** [http://localhost:8000/api/healthz/live/](http://localhost:8000/api/healthz/live/)
* **Readiness Probe:** [http://localhost:8000/api/healthz/ready/](http://localhost:8000/api/healthz/ready/)

---

## 3. How to Test using busyboxplus:curl Container
To simulate internal cluster requests, find the IP address of the `todoapp` pod:

```bash
kubectl get pod todoapp -n todoapp -o wide
```
*(Note down the internal `IP` of the pod, e.g., `10.244.0.15`)*

Execute a shell inside the busybox pod and use `curl` to hit the application and health endpoints:

```bash
# Enter the busybox container interactively
kubectl exec -it busybox-curl -n todoapp -- sh

# Inside the container, run curl against the ToDo app's internal IP (replace with actual IP)
curl http://<TODOAPP_POD_IP>:8000/api/healthz/live/
curl http://<TODOAPP_POD_IP>:8000/api/healthz/ready/
```
