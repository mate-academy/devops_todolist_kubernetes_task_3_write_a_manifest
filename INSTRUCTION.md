# Deploy and test the ToDo application

Run these commands from the repository root. You need a running Kubernetes
cluster, `kubectl` configured to access it, and the application image available
in Docker Hub.

The commands below use the repository's current directory name, `.infrasctructure`.

## Apply all manifests

Before applying, ensure `todoapp-pod.yml` has `readinessProbe` aligned with
`livenessProbe` under the application container. Use `/api/liveness/` and
`/api/readiness/` as their respective HTTP paths, matching the application routes.

Create the namespace first, then apply both pod manifests:

```sh
kubectl apply -f .infrastructure/namespace.yml
kubectl apply -f .infrastructure/todoapp-pod.yml
kubectl apply -f .infrastructure/busybox.yml
kubectl wait --for=condition=Ready pod/todoapp -n todoapp --timeout=120s
kubectl get pods -n todoapp -o wide
```

If the application does not become ready, inspect its events and logs:

```sh
kubectl describe pod todoapp -n todoapp
kubectl logs todoapp -n todoapp
```

## Test with port forwarding

Forward local port 8000 to the application pod:

```sh
kubectl port-forward -n todoapp pod/todoapp 8000:8000
```

Keep this terminal running. Open <http://localhost:8000/> in a browser to test
the ToDo interface, or <http://localhost:8000/api/> to explore the API.
In another terminal, check the health endpoints (use `curl.exe` in PowerShell):

```sh
curl -i http://localhost:8000/api/liveness/
curl -i http://localhost:8000/api/readiness/
```

Both endpoints should return HTTP `200` and the body `OK`.
Press `Ctrl+C` in the forwarding terminal when finished.

## Test with the busyboxplus:curl container

The `busybox.yml` manifest uses `ikulyk404/busyboxplus:curl`. Start an interactive
shell in that pod:

```sh
kubectl exec -it -n todoapp busybox -- /bin/sh
```

If the pod has exited or is restarting because its shell does not stay open,
create a temporary interactive pod using the same image instead:

```sh
kubectl run busybox-curl-test -n todoapp --rm -it --restart=Never --image=ikulyk404/busyboxplus:curl -- /bin/sh
```

From a separate local terminal, obtain the application pod IP:

```sh
kubectl get pod todoapp -n todoapp -o jsonpath='{.status.podIP}'
```

Inside the container shell, replace `POD_IP` with that address and run:

```sh
curl -i http://POD_IP:8000/
curl -i http://POD_IP:8000/api/
curl -i http://POD_IP:8000/api/liveness/
curl -i http://POD_IP:8000/api/readiness/
```

The landing page and API should return HTTP `200` with HTML or API content.
Both health endpoints should return HTTP `200` with `OK`. These requests test
connectivity inside the cluster and do not require port forwarding or a Service.
Pod IPs can change when pods are recreated; retrieve the IP again if necessary.

Run `exit` to leave the container shell. The temporary test pod, if used, is
removed automatically.
