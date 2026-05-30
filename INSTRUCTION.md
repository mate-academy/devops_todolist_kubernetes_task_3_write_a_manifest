# Deployment Instructions

## 1. Apply all manifests

```bash
kubectl apply -f .infrastructure/namespace.yml
kubectl apply -f .infrastructure/busybox.yml
kubectl apply -f .infrastructure/todoapp-pod.yml
```

## 2. Verify pods are running

```bash
kubectl get pods -n todoapp
```

## 3. Test the app using port-forward

```bash
kubectl port-forward pod/todoapp 8080:8080 -n todoapp
```

Then open in browser or use curl:

```bash
curl http://localhost:8080/api/todos/
curl http://localhost:8080/api/health/
curl http://localhost:8080/api/ready/
```

## 4. Test using the busyboxplus:curl container

```bash
kubectl exec -it busybox -n todoapp -- sh
```

Inside the container, use curl to reach the todoapp pod. First get the pod IP:

```bash
kubectl get pod todoapp -n todoapp -o wide
```

Then from inside busybox:

```sh
curl http://<TODOAPP_POD_IP>:8080/api/todos/
curl http://<TODOAPP_POD_IP>:8080/api/health/
curl http://<TODOAPP_POD_IP>:8080/api/ready/
```
