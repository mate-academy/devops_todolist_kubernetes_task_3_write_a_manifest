# Deploying Django ToDo on Kubernetes

## Prerequisites

- A running Kubernetes cluster and a configured `kubectl`.
- Docker, if you need to rebuild the application image.
- Access to the Docker Hub images `aniapavliuk97/todoapp:3.0.0` and `ikulyk404/busyboxplus:curl`.

Run the following commands from the root directory of this repository.

## 1. Apply the Kubernetes manifests

Create the namespace first, then create the Busybox and Django Pods:

```bash
kubectl apply -f .infrastructure/namespace.yml
kubectl apply -f .infrastructure/busybox.yml
kubectl apply -f .infrastructure/todoapp-pod.yml
```

Verify that the namespace and Pods have been created:

```bash
kubectl get namespace todoapp
kubectl get pods -n todoapp -w
```

Wait until both `busybox` and `todoapp-pod` show `Running` and `1/1` in the `READY` column. Press `Ctrl+C` to exit watch mode.

The Django Pod may initially show `0/1` because the readiness endpoint returns HTTP 503 during the application's startup period. Once the readiness probe succeeds, the Pod becomes ready. The liveness probe checks whether the application is running and restarts the container if the configured failure threshold is reached.

## 2. Test the application using port-forward

Forward local port 8085 to port 8000 of the Django Pod:

```bash
kubectl port-forward -n todoapp pod/todoapp-pod 8085:8000
```

Keep this terminal open. In another terminal, test the application and its endpoints:

```bash
curl -i http://localhost:8085/
curl -i http://localhost:8085/api/readiness/
curl -i http://localhost:8085/api/liveness/
```

You can also open the application in a browser at http://localhost:8085/.

After the startup period, the readiness endpoint should return HTTP 200 with the response `Ready`. The liveness endpoint should return HTTP 200 with the response `Alive`.

Local port 8085 is used to avoid a conflict with port 8084, which may already be occupied by the locally running Docker container. Press `Ctrl+C` in the port-forward terminal when testing is finished.

## 3. Test the application from the Busybox Pod

Get the IP address of the Django Pod:

```bash
kubectl get pods -n todoapp -o wide
```

Store the current Pod IP in a shell variable:

```bash
POD_IP=$(kubectl get pod todoapp-pod -n todoapp -o jsonpath='{.status.podIP}')
```

Send HTTP requests from the Busybox Pod directly to the Django Pod using its IP address and port 8000:

```bash
kubectl exec -n todoapp busybox -- curl -i "http://${POD_IP}:8000/"
kubectl exec -n todoapp busybox -- curl -i "http://${POD_IP}:8000/api/readiness/"
kubectl exec -n todoapp busybox -- curl -i "http://${POD_IP}:8000/api/liveness/"
```

The readiness and liveness endpoints should both return HTTP 200 after the application is ready. These requests verify that the Django Pod is reachable from another Pod inside the Kubernetes cluster without using port-forward.

## 4. Troubleshooting

If a Pod is not ready or does not start, inspect its status, events and logs:

```bash
kubectl get pods -n todoapp
kubectl describe pod todoapp-pod -n todoapp
kubectl logs todoapp-pod -n todoapp
kubectl describe pod busybox -n todoapp
```

If the application container has restarted, inspect the previous container's logs:

```bash
kubectl logs todoapp-pod -n todoapp --previous
```

## 5. Clean up (optional)

Delete the Pods and the namespace created for this assignment:

```bash
kubectl delete -f .infrastructure/todoapp-pod.yml
kubectl delete -f .infrastructure/busybox.yml
kubectl delete -f .infrastructure/namespace.yml
```

Deleting the namespace also removes any other namespaced resources inside `todoapp`, so only do this when you no longer need them.
