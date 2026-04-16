# Instruction

## Applying manifests

To apply all manifests you need to enter this command

```bash
kubectl apply -f .infrastructure/namespace.yml && \
kubectl apply -f .infrastructure/busybox.yml && \
kubectl apply -f .infrastructure/todoapp-pod.yml
```

## Testing app

To test app you need to map ports via ```port-forward``` function

```bash
kubectl port-forward pod/todoapp -n todoapp 8000:8000
```

## Accessing the app

To access the app follow the [app link](http://localhost:8000/)
