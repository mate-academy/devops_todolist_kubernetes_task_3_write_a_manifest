# INSTRUCTION

### 1. Apply all manifests

First, create the namespace:

```bash
kubectl apply -f .infrastructure/namespace.yml
```

Then create the ToDo application pod and busybox pod:
```bash
kubectl apply -f .infrastructure/todoapp-pod.yml
kubectl apply -f .infrastructure/busybox.yml
```

---

### 2. Check that pods are running:

```bash
kubectl get pods -n todoapp
```

---

### 3. Test ToDo application 

* #### Using port-forwarding

Run port-forward for the ToDo application pod:
```bash
kubectl port-forward pod/todoapp 8080:8080 -n todoapp
```

Open the application in a browser:
```bash
http://localhost:8080
```

You can also test health and readiness endpoints:
```bash
http://localhost:8080/api/health/
http://localhost:8080/api/ready/
```


* #### Using the busyboxplus:curl container

Get pod IP address:
```bash
kubectl get pods -n todoapp -o wide
```

Connect to the busybox container:
```bash
kubectl exec -it busybox -n todoapp -- sh
```

Inside the busybox container, test the ToDo application using the ToDo pod IP and port 8080:
```bash
curl <TODOAPP_POD_IP>:8080
```

You can also test health and readiness endpoints:
```bash
curl <TODOAPP_POD_IP>:8080/api/health/
curl <TODOAPP_POD_IP>:8080/api/ready/
```