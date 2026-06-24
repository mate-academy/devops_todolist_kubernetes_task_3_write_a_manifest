# How to run TODO list with Kubernetes

### Clone repository with project

```bash
git clone git@github.com:maxmlv/devops_todolist_kubernetes_task_3_write_a_manifest.git
cd devops_todolist_kubernetes_task_3_write_a_manifest
```

## Apply Kubernetes manifests

### Create `todoapp` namespace

```bash
kubectl apply -f .infrastructure/namespace.yml
```

### Create a pod `busybox`

```bash
kubectl apply -f .infrastructure/busybox.yml
```

This pod runs a container from the image `ikulyk404/busyboxplus:curl`. This container is useful for sending requests to the TODO app via `curl`.

### Create a pod `todoapp`

```bash
kubectl apply -f .infrastructure/todoapp-pod.yml
```

This pod runs a container from the image `maxmlv/todoapp:3.0.0` with readiness and liveness probes configured.

## How to test the application

### Check readiness and liveness probe responses from the app

You can see if the `todoapp` is ready for traffic and working properly.

```bash
kubectl describe pod todoapp -n todoapp
```
Look for the `Liveness` and `Readiness` lines in the output.

```bash
Containers:
  todoapp:
    Container ID:   containerd://55895357ad5c8c0426ab8dd25534d8fbb30bdd9ee8bf21aeb9e6b337a1cfcbf3
    Image:          maxmlv/todoapp:3.0.0
    Image ID:       docker.io/maxmlv/todoapp@sha256:fbc48b857a8b31cbdbb66a9a7d3f5ade83d5a10f6cf5f0c57400d03a2666bc87
    Port:           8080/TCP
    Host Port:      0/TCP
    State:          Running
      Started:      Wed, 24 Jun 2026 16:47:08 +0300
    Ready:          True
    Restart Count:  0
--> Liveness:       http-get http://:8080/api/healthz delay=60s timeout=1s period=5s #success=1 #failure=3
--> Readiness:      http-get http://:8080/api/readyz delay=5s timeout=1s period=5s #success=1 #failure=3
    Environment:    <none>
    Mounts:
      /var/run/secrets/kubernetes.io/serviceaccount from kube-api-access-77n24 (ro)
```

### via Port-forward

```bash
kubectl port-forward pod/todoapp 8081:8080 -n todoapp
```
Now the application is available at `127.0.0.1:8081`.

### via `busybox` Pod using `curl`

For this, we will need to know the `todoapp` pod's IP address:

```bash
kubectl get pods -n todoapp -o wide
```

```bash
Output example:

NAME      READY   STATUS    RESTARTS        AGE   IP            NODE                    NOMINATED NODE   READINESS GATES
busybox   1/1     Running   1 (9m42s ago)   69m   10.244.0.8    desktop-control-plane   <none>           <none>
todoapp   1/1     Running   0               33m   10.244.0.14   desktop-control-plane   <none>           <none>
```

Now we can connect to the `busybox` container.

```bash
kubectl exec -it busybox -n todoapp -- sh
```

Inside `busybox`, we can send a GET request via `curl`:

```bash
curl <todoapp IP address>:8080
```