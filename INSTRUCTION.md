# Instructions for Deploying and Testing ToDo Application

## 1. Applying Kubernetes manifests

All manifests are located in the `.infrastructure` folder.

To apply all manifests at once, run:

```bash
kubectl apply -f .infrastructure/
```

## 2. Testing ToDo application using port-forward

To access the ToDo app running inside the cluster on your local machine, use port-forward:

```bash
kubectl port-forward pod/todoapp-pod 8080:8080
```

Now you can open in your browser:

```arduino
http://localhost:8080/
```

Or test readiness and liveness endpoints:

```bash
curl http://localhost:8080/api/readiness
curl http://localhost:8080/api/liveness
```

## 3. Testing the application using busyboxplus:curl container

You can run a temporary pod with busyboxplus:curl image to test connectivity inside the cluster.
Run:

```bash
kubectl run curl-pod --rm -i --tty --image=ikulyk404/busyboxplus:curl -- /bin/sh
```

Inside the pod shell, you can curl the ToDo app pod by its service name or IP, for example:

```bash
curl http://todoapp-pod:8080/api/readiness
curl http://todoapp-pod:8080/api/liveness
```

To exit the pod shell:

```bash
exit
```

# Notes:

Make sure your Kubernetes cluster is running and kubectl is configured.

Replace pod names or ports if they differ in your setup.
