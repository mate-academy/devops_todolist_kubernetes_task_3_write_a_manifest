# Kubernetes instructions

### Apply all Kubernetes manifests from the .infrastructure directory:

```
kubectl apply -f .infrastructure/
```

### Check that the namespace and pods were created:

```
kubectl get namespace 
kubectl get pods -n todoapp
```

### More details about the ToDo application pod:

```
kubectl describe pod todoapp -n todoapp
```

### Test the ToDo application using port-forward

```
kubectl port-forward pod/todoapp 8000:8000 -n todoapp
```

### In another terminal:

```
curl http://localhost:8000/api/readiness
curl http://localhost:8000/api/liveness
```

### The application is available at:
(http://localhost:8000)[http://localhost:8000]

# Test the ToDo application using busyboxplus

Get the ToDo application pod IP:

```
kubectl get pod todoapp -n todoapp -o wide
```

Open the busybox container:

```
kubectl exec -it busybox -n todoapp -- sh
```
Test the readiness endpoint from the busybox container:

```
curl http://<TODOAPP_POD_IP>:8000/api/readiness
```

Test the liveness endpoint:

```
curl http://<TODOAPP_POD_IP>:8000/api/liveness
```