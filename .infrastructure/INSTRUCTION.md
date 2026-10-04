# ToDo App — Kubernetes Instructions

## Apply manifests

Apply all Kubernetes manifests:

```bash
kubectl apply -f .infrastructure/
```

Check Pods:

```bash
kubectl get pods -n todoapp
```

## Test with port-forward

Forward the application port:

```bash
kubectl port-forward pod/todoapp 8080:8080 -n todoapp
```

In another terminal:

```bash
curl http://localhost:8080/api/liveness/
curl http://localhost:8080/api/readiness/
```

Expected responses:

```text
alive
ready
```

## Test from busybox

Get the ToDo Pod IP:

```bash
kubectl get pod todoapp -n todoapp -o wide
```

Use the IP address in the following commands:

```bash
kubectl exec busybox -n todoapp -- curl http://<TODOAPP_IP>:8080/api/liveness/
kubectl exec busybox -n todoapp -- curl http://<TODOAPP_IP>:8080/api/readiness/
```

Expected responses:

```text
alive
ready
```

## Check probes

```bash
kubectl describe pod todoapp -n todoapp
```

## Remove resources

```bash
kubectl delete -f .infrastructure/
```
