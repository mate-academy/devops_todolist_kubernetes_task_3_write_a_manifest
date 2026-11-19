# Kubernetes Deployment and Testing Instructions

## 1. Apply Kubernetes manifests

All Kubernetes manifests are located in the `.infrastructure/` directory.

### 1.1 Create the namespace

```bash
kubectl create namespace todoapp
```

If the namespace already exists, this command may return an error. You can safely ignore it.

### 1.2 Apply the manifests

Apply all manifests from the directory:

```bash
kubectl apply -f .infrastructure/
```

### 1.3 Verify deployment

Check the created resources:

```bash
kubectl get all -n todoapp
```

Check individual Pods:

```bash
kubectl get pods -n todoapp -o wide
```

Check the application Pod details:

```bash
kubectl describe pod todoapp -n todoapp
```

Verify that the application container is running and that its liveness and readiness probes are successful.

---

## 2. Test the Todo application using port-forward

Port forwarding allows access to an application running inside the Kubernetes cluster through a local port.

### 2.1 Forward the application port

```bash
kubectl port-forward pod/todoapp 8080:8080 -n todoapp
```

This forwards local port `8080` to port `8080` on the Todo application Pod.

Keep this terminal running while testing the application.

### 2.2 Access the application

Open a browser and navigate to:

```text
http://127.0.0.1:8080
```

Alternatively, use curl:

```bash
curl http://127.0.0.1:8080
```

### 2.3 Test application endpoints

If the corresponding endpoints are registered in Django, test them using:

```bash
curl http://127.0.0.1:8080/api/live
curl http://127.0.0.1:8080/api/ready
```

Expected response: HTTP `200 OK`.

---

## 3. Test the application using the BusyBoxPlus container

The `ikulyk404/busyboxplus:curl` image provides a container with curl, allowing HTTP requests to be executed from inside the Kubernetes cluster.

### 3.1 Verify the BusyBox Pod

```bash
kubectl get pods -n todoapp
```

Make sure the `busybox` Pod is running.

### 3.2 Retrieve the Todo application Pod IP

```bash
kubectl get pod todoapp -n todoapp -o wide
```

Find the `IP` column. This is the internal IP address of the Todo application Pod.

### 3.3 Execute curl from the BusyBox container

Replace `<TODOAPP_POD_IP>` with the IP address obtained in the previous step.

Test the application:

```bash
kubectl exec busybox -n todoapp -- curl http://<TODOAPP_POD_IP>:8080
```

Test the readiness endpoint:

```bash
kubectl exec busybox -n todoapp -- curl -i http://<TODOAPP_POD_IP>:8080/api/ready
```

Test the liveness endpoint:

```bash
kubectl exec busybox -n todoapp -- curl -i http://<TODOAPP_POD_IP>:8080/api/live
```

The `-i` option displays the HTTP response headers, including the status code.

### 3.4 Open an interactive shell (optional)

You can also enter the BusyBox container:

```bash
kubectl exec -it busybox -n todoapp -- sh
```

Then execute HTTP requests directly:

```bash
curl -i http://<TODOAPP_POD_IP>:8080
```

Exit the container:

```bash
exit
```

---

## 4. Troubleshooting

Check Pod status:

```bash
kubectl get pods -n todoapp
```

Check application logs:

```bash
kubectl logs todoapp -n todoapp
```

Inspect application events:

```bash
kubectl describe pod todoapp -n todoapp
```

If a readiness or liveness probe fails, verify that the configured HTTP endpoints exist and return HTTP 200.

If the BusyBox container cannot reach the application, verify that both Pods are running and that the application listens on `0.0.0.0:8080`, rather than only `127.0.0.1:8080`.