# ToDo app on Kubernetes

## 1) Apply all manifests
```bash
kubectl apply -f .infrastructure/namespace.yml
kubectl apply -f .infrastructure/todoapp-pod.yml
kubectl apply -f .infrastructure/busybox.yml
# (опційно) сервіс
kubectl apply -f .infrastructure/service.yml
kubectl -n todoapp get pods -o wide
kubectl -n todoapp get svc
