# Instructions to Deploy ToDo App on Kubernetes

# 1️⃣ Apply Namespace
```
kubectl apply -f .infrastructure/namespace.yml
```
# 2️⃣ Deploy Busybox Pod
```
kubectl apply -f .infrastructure/busybox.yml
```
# 3️⃣ Deploy ToDo App Pod
```
kubectl apply -f .infrastructure/todoapp-pod.yml
```
# Verify pod status
```
kubectl get pods -n todoapp
```
# 4️⃣ Port-forward ToDo App to localhost
````
echo "Running port-forward in background..."
kubectl port-forward pod/todoapp 8000:8000 -n todoapp &

echo "You can now open the ToDo app in your browser at http://localhost:8000"
````
# 5️⃣ Test readiness endpoint from Busybox pod
```
kubectl exec -it busybox -n todoapp -- curl http://todoapp:8000/api/readiness/
```

# 6️⃣ Test liveness endpoint from Busybox pod
```
kubectl exec -it busybox -n todoapp -- curl http://todoapp:8000/api/liveness/
```

# 7️⃣ Reminder: If not done, build and push your Docker image
```
echo "Reminder: build and push your Docker image if you haven't done it yet"
echo "docker build -t YOUR_DOCKERHUB_USERNAME/todoapp:3.0.0 ."
echo "docker push YOUR_DOCKERHUB_USERNAME/todoapp:3.0.0"
```
