# Kubernetes deployment instructions

## Prerequisites

- `kubectl` configured for your cluster (Minikube, Docker Desktop Kubernetes, kind, etc.)
- Docker image `artemzakharchukhome/todoapp:3.0.0` built and pushed to Docker Hub

## Apply all manifests

From the repository root:

```bash
kubectl apply -f .infrastructure/namespace.yml
kubectl apply -f .infrastructure/busybox.yml
kubectl apply -f .infrastructure/todoapp-pod.yml
```

Or apply the whole folder at once:

```bash
kubectl apply -f .infrastructure/
```

Check that resources are created:

```bash
kubectl get namespace todoapp
kubectl get pods -n todoapp
```

Wait until the `todoapp` pod is `Running` and `READY` is `1/1` (readiness may take up to ~40 seconds after the container starts).

```bash
kubectl wait --for=condition=Ready pod/todoapp -n todoapp --timeout=120s
```

## Test the ToDo app with port-forward

Forward local port `8080` to the `todoapp` pod:

```bash
kubectl port-forward -n todoapp pod/todoapp 8080:8080
```

In another terminal:

```bash
curl -i http://127.0.0.1:8080/api/health/live/
curl -i http://127.0.0.1:8080/api/health/ready/
open http://127.0.0.1:8080/
```

Stop port-forward with `Ctrl+C`.

## Test the app from the busyboxplus:curl pod

The `busybox` pod runs image `ikulyk404/busyboxplus:curl` in the same namespace. Use it to call the ToDo app over the cluster network (pods have no Service in this task, so use the pod IP).

Get the ToDo pod IP:

```bash
TODOAPP_IP=$(kubectl get pod todoapp -n todoapp -o jsonpath='{.status.podIP}')
echo "$TODOAPP_IP"
```

Run `curl` from the busybox container:

```bash
kubectl exec -n todoapp busybox -- curl -s -i "http://${TODOAPP_IP}:8080/api/health/live/"
kubectl exec -n todoapp busybox -- curl -s -i "http://${TODOAPP_IP}:8080/api/health/ready/"
kubectl exec -n todoapp busybox -- curl -s -i "http://${TODOAPP_IP}:8080/"
```

Optional interactive shell in busybox:

```bash
kubectl exec -n todoapp -it busybox -- sh
curl -s -i http://<todoapp-pod-ip>:8080/api/
```

## Cleanup (optional)

```bash
kubectl delete -f .infrastructure/
```
