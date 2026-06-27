# Applying the manifests step by step
### namespace first

```
kubectl apply -f .infrastructure/namespace.yml
```

### busybox pod

```
kubectl apply -f .infrastructure/busybox.yml
```

### todoapp pod

```
kubectl apply -f .infrastructure/todoapp-pod.yml
```
