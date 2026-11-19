# Todoapp in Kubernetes

## 1. Apply the manifests

The namespace must be created first, because the pods live inside it.

```
kubectl apply -f .infrastructure/namespace.yml
kubectl apply -f .infrastructure/busybox.yml
kubectl apply -f .infrastructure/todoapp-pod.yml
```

Check that both pods are `Running` and `READY 1/1`:

```
kubectl get pods -n todoapp
```

## 2. Test with port-forward

```
kubectl port-forward pod/todoapp 8000:8000 -n todoapp
```

Open in the browser, both pages must show `OK`:

- http://localhost:8000/api/liveness/
- http://localhost:8000/api/readiness/

Press Ctrl+C to stop the port-forward.

## 3. Test with the busyboxplus:curl container

Find the IP address of the todoapp pod (column IP):

```
kubectl get pod todoapp -n todoapp -o wide
```

Open a shell in the busybox pod:

```
kubectl exec -it busybox -n todoapp -- sh
```

Inside the shell run (replace POD_IP with the IP from the previous step):

```
curl http://POD_IP:8000/api/liveness/
curl http://POD_IP:8000/api/readiness/
exit
```

Both requests must return `OK`.