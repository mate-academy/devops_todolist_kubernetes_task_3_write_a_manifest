### 1. Create the Namespace
Create the dedicated `todoapp` isolated namespace first:

```bash
kubectl apply -f src/.infrastructure/namespace.yml
```

### 2. Deploy the ToDo Application Pods
```bash
kubectl apply -f src/.infrastructure/busybox.yml
kubectl apply -f src/.infrastructure/todoapp-pod.yml
```

### 3. How to test ToDo application
```bash
kubectl port-forward pod/todoapp-pod 8081:8000 -n todoapp 
```

http://localhost:8081

### 4. How to test the application using the busyboxplus:curl container
#### 1. Retrieve the IP Address of todoapp_pod
```bash
kubectl get pods -n todoapp -o wide
```
#### 2. Execute curl Commands from inside busybox
```bash
kubectl -n todoapp exec -it busybox -- sh
```
####    3.Inside the busybox container shell, execute HTTP requests directly to the application pod IP
```bash
# Test Liveness Probe
curl -i http://<TODOAPP_POD_IP>:8000/api/health

# Test Readiness Probe
curl -i http://<TODOAPP_POD_IP>:8000/api/ready

# Test ToDo API Endpoints
curl -i http://<TODOAPP_POD_IP>:8000/api/todos/

# Exit the container
exit
```