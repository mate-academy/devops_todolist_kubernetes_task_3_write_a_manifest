

## Create pods
```
kubectl apply -f .infrastructure/namespace.yml
kubectl apply -f .infrastructure/busybox.yml
kubectl apply -f .infrastructure/todoapp-pod.yml
```

## Testing

```
kubectl port-forward pod/todoapp 8001:8000 -n todoapp
```

## Curl

```
kubectl exec -it busybox -n todoapp -- curl http://todoapp:8000
```
