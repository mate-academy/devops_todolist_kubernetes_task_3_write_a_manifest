# Instructions

This document describes how to build the ToDo app image, apply the Kubernetes
manifests in `.infrastructure/`, and verify that everything works.

## 1. Build and push the image

From the root of the repository (where the `Dockerfile` lives):

```
docker build -t <your-dockerhub-username>/todoapp:3.0.0 .
docker push <your-dockerhub-username>/todoapp:3.0.0
```

Make sure `.infrastructure/todoapp-pod.yml` references the same image name/tag
you just pushed (`image: <your-dockerhub-username>/todoapp:3.0.0`).

## 2. Apply the manifests

Apply them in this order — the namespace must exist before the pods that use it:

```
kubectl apply -f .infrastructure/namespace.yml
kubectl apply -f .infrastructure/busybox.yml
kubectl apply -f .infrastructure/todoapp-pod.yml
```

Check that both pods are up and running:

```
kubectl get pods -n todoapp -o wide
```

You should see:

```
NAME      READY   STATUS    RESTARTS   AGE
busybox   1/1     Running   0          Xm
todoapp   1/1     Running   0          Xm
```

`todoapp` may briefly show `0/1 Running` right after creation — this is
expected, since the readiness probe has a 5 second initial delay before its
first check. If it doesn't turn `1/1` within a minute, check the logs:

```
kubectl logs -n todoapp todoapp --tail=20
kubectl describe pod todoapp -n todoapp
```

## 3. Test the ToDo application with `port-forward`

Forward a local port to the `todoapp` pod:

```
kubectl port-forward -n todoapp pod/todoapp 8000:8000
```

Then, in a browser or with `curl`, open:

```
http://localhost:8000/
```

You should see the ToDo app landing page. You can also check the probe
endpoints directly:

```
curl http://localhost:8000/api/readiness/
curl http://localhost:8000/api/liveness/
```

Both should return `OK` with an HTTP 200 status.

## 4. Test the application from inside the cluster using `busyboxplus:curl`

Exec into the `busybox` pod:

```
kubectl exec -it -n todoapp busybox -- /bin/sh
```

From inside the pod, get the `todoapp` pod's IP (run this from another
terminal, outside the busybox shell):

```
kubectl get pod todoapp -n todoapp -o jsonpath='{.status.podIP}'
```

Then, from within the busybox shell, curl that IP:

```
curl http://<todoapp-pod-ip>:8000/
curl http://<todoapp-pod-ip>:8000/api/readiness/
curl http://<todoapp-pod-ip>:8000/api/liveness/
```

All requests should succeed, confirming the ToDo app pod is reachable from
within the cluster and its readiness/liveness endpoints are healthy.

## 5. Cleanup

```
kubectl delete -f .infrastructure/todoapp-pod.yml
kubectl delete -f .infrastructure/busybox.yml
kubectl delete -f .infrastructure/namespace.yml
```
