# Instructions

## Applying the manifests

1. First, create the namespace:

```bash
kubectl apply -f .infrastructure/namespace.yml
```

2. Once the namespace exists, create the pods from their manifests:

```bash
kubectl apply -f .infrastructure/busybox.yml
```

```bash
kubectl apply -f .infrastructure/todoapp-pod.yml
```

3. Check that the pods are up and inspect their status:

```bash
kubectl get pods -n todoapp
```

Note: `todoapp-pod` may briefly show `0/1` in the READY column right after creation. This is expected — the pod stays `NotReady` until its readiness probe succeeds.


## Testing

Once both pods are running, verify the application.

### Testing via the busyboxplus:curl container

1. Get the pod IPs:

```bash
kubectl get pods -n todoapp -o wide
```

2. Open a shell inside the busybox pod:

```bash
kubectl -n todoapp exec -it busybox -- sh
```

3. Send a request to the ToDo app:

```bash
curl <todoapp_pod_ip>:8080
```

You should get the application's HTML page in response.

### Testing via port-forward

Forward a local port to the pod:

```bash
kubectl port-forward pod/todoapp-pod 8080:8080 -n todoapp
```

Then open `http://localhost:8080` in your browser.

The mapping is `<local_port>:<pod_port>`. Here `8080` is the port the application listens on inside the container — check the `Dockerfile` if your app uses a different one.