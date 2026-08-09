
# Instructions for running and testing an application in Kubernetes

## To apply manifests, run the following commands:
1. Create a namespace
```bash
kubectl apply -f .infrastructure/namespace.yml
```

Wait until the Pod is ready:
```
kubectl get pods -n todoapp -w
```

2. Launch a Busybox container in the cluster
```bash
kubectl apply -f .infrastructure/busybox.yml
```
3. Launch the Todo app container in the cluster
```bash
kubectl apply -f .infrastructure/todoapp-pod.yml
```


**To test the ToDo app, use the port-forward command.**
```bash
kubectl port-forward -n todoapp pod/todoapp 8000:8000
```

Open http://localhost:8000

**To test the application using busybox, use**
```bash
kubectl exec -n todoapp pod/busybox -- curl http://todoapp:8000/api/healthz/ready/
```

**To check the status of events, use the command:**
```bash
kubectl get pods -n todoapp
```