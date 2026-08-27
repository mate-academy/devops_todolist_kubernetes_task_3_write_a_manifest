## Applying all manifests

Apply all Kubernetes manifests from the `.infrastructure` directory:

```bash
kubectl apply -f .infrastructure/
```

Check the pods:

```bash
kubectl get pods -n todoapp
```

Wait until the application pods are in the `Running` state and ready.

## Testing the ToDo application using port-forward

Forward the Kubernetes service port to the local machine:

```bash
kubectl port-forward -n todoapp pod/todoapp 8080:8080
```

After port forwarding is started, the application is available at:

```text
http://localhost:8080
```

## Testing the application using busyboxplus:curl

First you need to now your app's ip adresss:

```bash
kubectl get pods -n todoapp -o wide
```

Then connect to busybox:

```bash
kubectl -n todoapp exec -it busybox -- sh
```

Test the API:

```bash
curl <your-ip-address>:8080
```

Test the readiness endpoint:

```bash
curl <your-ip-address>:8080/api/ready/
```

Test the liveness endpoint:

```bash
curl <your-ip-address>:8080/api/live/
```

Exit the temporary container with:

```bash
exit
```
