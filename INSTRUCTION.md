# ToDo app on Kubernetes

All manifests live in the `.infrastructure` folder.

## 1. Apply the manifests

Apply the namespace first, because both pods live in it:

```
kubectl apply -f .infrastructure/namespace.yml
kubectl apply -f .infrastructure/busybox.yml
kubectl apply -f .infrastructure/todoapp-pod.yml
```

Or apply the whole folder (kubectl creates the namespace first):

```
kubectl apply -f .infrastructure/
```

Check that both pods are running and the ToDo pod is ready (`READY 1/1`):

```
kubectl get pods -n todoapp
```

If the pod does not become ready, inspect it:

```
kubectl describe pod todoapp -n todoapp
kubectl logs todoapp -n todoapp
```

## 2. Test the ToDo app with `port-forward`

Forward local port 8000 to the pod:

```
kubectl port-forward pod/todoapp 8000:8000 -n todoapp
```

In another terminal (or in a browser) check the app and the probe endpoints:

```
curl http://localhost:8000/api/live/
curl http://localhost:8000/api/ready/
curl http://localhost:8000/api/
```

The landing page is available at http://localhost:8000/. Stop the forward with `Ctrl+C`.

## 3. Test the ToDo app using the `busyboxplus:curl` container

Get the IP address of the ToDo pod:

```
kubectl get pod todoapp -n todoapp -o wide
```

Or store it in a variable:

```
POD_IP=$(kubectl get pod todoapp -n todoapp -o jsonpath='{.status.podIP}')
echo $POD_IP
```

Run curl from inside the busybox pod:

```
kubectl exec -it busybox -n todoapp -- curl http://$POD_IP:8000/api/live/
kubectl exec -it busybox -n todoapp -- curl http://$POD_IP:8000/api/ready/
kubectl exec -it busybox -n todoapp -- curl http://$POD_IP:8000/api/
```

Alternatively open a shell in the busybox pod and run curl there:

```
kubectl exec -it busybox -n todoapp -- sh
curl http://<POD_IP>:8000/api/live/
```

## 4. Clean up

```
kubectl delete -f .infrastructure/
```