# Instructions

## Apply Kubernetes manifests

Apply all manifests from the .infrastructure directory:

```bash
kubectl apply -f .infrastructure/
```

If the manifests are applied one by one, create the namespace first and then apply the pods:

```bash
kubectl apply -f .infrastructure/namespace.yml
kubectl apply -f .infrastructure/todoapp-pod.yml
kubectl apply -f .infrastructure/busybox.yml
```

Check that the pods are running:

```bash
kubectl get pods -n todoapp
```

## Test the ToDo application with port-forward

Forward the ToDo application pod port to your local machine:

```bash
kubectl port-forward -n todoapp pod/todoapp 8000:8000
```

Open the application in a browser:

```text
http://localhost:8000/
```

Test the API health endpoints:

```bash
curl http://localhost:8000/api/health/live/
curl http://localhost:8000/api/health/ready/
```

Expected responses:

```json
{"status": "ok"}
{"status": "ready"}
```

## Test the application from the busyboxplus:curl container

Open a shell inside the busyboxplus:curl pod:

```bash
kubectl exec -it -n todoapp busybox -- sh
```

From inside the container, call the ToDo application pod by its pod IP.
First, get the ToDo application pod IP:

```bash
kubectl get pod -n todoapp todoapp -o wide
```

Then run curl from the busyboxplus:curl shell:

```bash
curl http://<TODOAPP_POD_IP>:8000/
curl http://<TODOAPP_POD_IP>:8000/api/health/live/
curl http://<TODOAPP_POD_IP>:8000/api/health/ready/
```

Exit the busyboxplus:curl shell:

```bash
exit
```
