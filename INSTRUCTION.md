# Instruction

## Apply all manifests

```bash
kubectl apply -f .infrastructure/namespace.yml
kubectl apply -f .infrastructure/busybox.yml
kubectl apply -f .infrastructure/todoapp-pod.yml
```

## Test ToDo application using port-forward

```bash
kubectl port-forward -n todoapp pod/todoapp 8080:8080
```

Then open in browser: http://localhost:8080

## Test application using busyboxplus:curl

```bash
kubectl exec -it -n todoapp busybox -- curl http://todoapp:8080/api/health/
kubectl exec -it -n todoapp busybox -- curl http://todoapp:8080/api/readiness/
```
