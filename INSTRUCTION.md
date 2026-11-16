### To apply manifests
```bash
kubectl apply -f .infrastructure/namespace.yml
kubectl apply -f .infrastructure/busybox.yml
kubectl apply -f .infrastructure/todoapp-pod.yml
```

### To edit manifest
```bash
kubectl edit pod <pod-name> -n todoapp
```

### To delete pod:
```bash
kubectl delete pod <pod-name> -n todoapp
```

### To test app using post-forwarding:
```bash
kubectl port-forward pod/todoapp 8080:8080 -n todoapp
```

### To test the application using the busyboxplus:curl container:
Find `todoapp` Pod IP:
```bash
kubectl get pods -o wide -n todoapp
```
Enter busybox container:
```bash
kubectl -n todoapp exec -it busybox -- sh
```
Use curl command:
```bash
curl http://<todoapp-ip>:8080
```
