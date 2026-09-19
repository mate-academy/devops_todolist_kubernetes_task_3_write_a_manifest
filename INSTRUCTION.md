# Instruction

## Apply manifests

Apply all manifests from the `.infrastructure` folder in the following order:

```
kubectl apply -f .infrastructure/namespace.yml
kubectl apply -f .infrastructure/busybox.yml
kubectl apply -f .infrastructure/todoapp-pod.yml
```

Check that both pods are up and running in the `todoapp` namespace:

```
kubectl get pods -n todoapp
```

## Test the ToDo application using port-forward

Forward the local port to the `todoapp` pod:

```
kubectl port-forward -n todoapp pod/todoapp 8000:8000
```

Open [http://localhost:8000](http://localhost:8000) in a browser to check the landing page, or [http://localhost:8000/api/](http://localhost:8000/api/) for the API.

## Test the application using the busyboxplus:curl container

Get the IP address of the `todoapp` pod:

```
kubectl get pod todoapp -n todoapp -o jsonpath='{.status.podIP}'
```

Open a shell inside the `busybox` pod:

```
kubectl exec -it -n todoapp busybox -- sh
```

From inside the `busybox` pod, curl the ToDo application using the IP address obtained above:

```
curl http://<todoapp-pod-ip>:8000/
curl http://<todoapp-pod-ip>:8000/api/health
curl http://<todoapp-pod-ip>:8000/api/ready
```

A successful response confirms that the ToDo application is reachable from inside the cluster.
