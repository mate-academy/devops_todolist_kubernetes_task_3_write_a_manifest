# TodoApp
1. Apply the manifests, to create the namespace, TodoApp pod and BusyBox pod:
```bash
kubectl apply -f ./.infrastructure/namespace.yml

kubectl apply -f ./.infrastructure/todoapp-pod.yml

kubectl apply -f ./.infrastructure/busybox.yml
```

2. Test the TodoApp using port-forwarding:
```bash
kubectl port-forward pod/todoapp 8080:8080 -n todoapp
```

3. Open your web browser and test the app at: http://localhost:8080

# Busybox
1. Retrieve the IP address of the TodoApp pod:
```bash
kubectl get pods -n todoapp -o wide
```

2. Access the BusyBox shell:
```bash
kubectl -n todoapp exec -it busybox -- sh
```

3. Send a curl request to the TodoApp:

```bash
curl <TodoApp_IP_address>:8080
```
