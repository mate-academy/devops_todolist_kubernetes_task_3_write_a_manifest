# ToDo application Kubernetes instructions

## Apply Kubernetes manifests

Create the namespace:

```bash
kubectl apply -f .infrastructure/namespace.yml
```

Create the BusyBox pod:

```bash
kubectl apply -f .infrastructure/busybox.yml
```

Create the ToDo application pod:

```bash
kubectl apply -f .infrastructure/todoapp-pod.yml
```

Check that the pods are running:

```bash
kubectl get pods -n todoapp
```

Expected result:

```text
NAME          READY   STATUS    RESTARTS
busybox       1/1     Running   0
todoapp-pod   1/1     Running   0
```

## Test the application using port-forward

Forward local port 8000 to the ToDo application pod:

```bash
kubectl port-forward -n todoapp pod/todoapp-pod 8000:8000
```

Open the application in a browser:

```text
http://localhost:8000
```

Test the readiness endpoint:

```bash
curl http://localhost:8000/api/readiness/
```

Expected response:

```text
OK
```

Test the liveness endpoint:

```bash
curl http://localhost:8000/api/liveness/
```

Expected response:

```text
OK
```

Stop port-forward with:

```text
Ctrl+C
```

## Test the application from BusyBox

Get the ToDo pod IP address:

```bash
kubectl get pods -n todoapp -o wide
```

Enter the BusyBox container:

```bash
kubectl exec -it -n todoapp busybox -- sh
```

Send a request to the ToDo application using the IP address of `todoapp-pod`:

```bash
curl http://<TODOAPP_POD_IP>:8000/api/readiness/
```

Expected response:

```text
OK
```

Test the liveness endpoint:

```bash
curl http://<TODOAPP_POD_IP>:8000/api/liveness/
```

Expected response:

```text
OK
```

Exit the BusyBox container:

```bash
exit
```

## Delete resources

Delete the namespace and all resources inside it:

```bash
kubectl delete namespace todoapp
```
