# Run ToDo app in Kubernetes

Image: `user2134567432/todoapp:3.0.0`

## 1. Apply manifests

```bash
kubectl apply -f .infrastructure/namespace.yml
kubectl apply -f .infrastructure/todoapp-pod.yml
kubectl apply -f .infrastructure/busybox.yml
kubectl get pods -n todoapp
```

## 2. Test with port-forward

```bash
kubectl port-forward pod/todoapp 8000:8000 -n todoapp
```

In another terminal:

```bash
curl http://localhost:8000/api/liveness/
curl http://localhost:8000/api/readiness/
```

## 3. Test with busyboxplus:curl

Save the `todoapp` pod IP to a variable:

```bash
POD_IP=$(kubectl get pod todoapp -n todoapp -o jsonpath='{.status.podIP}')
echo $POD_IP
```

Run requests from the `busybox` pod:

```bash
kubectl exec busybox -n todoapp -- curl http://$POD_IP:8000/api/liveness/
kubectl exec busybox -n todoapp -- curl http://$POD_IP:8000/api/readiness/
```