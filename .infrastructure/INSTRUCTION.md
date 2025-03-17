# Deployment Instructions for ToDo App in Kubernetes

## 1. Apply Kubernetes Manifests

```shell
kubectl apply -f .infrastructure/namespace.yml
kubectl apply -f .infrastructure/busybox.yml
kubectl apply -f .infrastructure/todoapp-service.yml
kubectl apply -f .infrastructure/todoapp-pod.yml
```

## 2. Verify Deployment Status

```shell
kubectl get pods -n todoapp
kubectl get services -n todoapp
```

## 3. Test Readiness & Liveness Probes

```shell
kubectl exec -it busybox -n todoapp -- curl http://todoapp:8000/api/readiness
kubectl exec -it busybox -n todoapp -- curl http://todoapp:8000/api/liveness
```

## 4. Test ToDo Application Using Port-Forward

Since the ToDo app is only accessible inside the cluster, use port-forward to make it available on your local machine.

1️⃣ Forward Port to Local Machine
Run this command:
```shell
kubectl port-forward pod/todoapp -n todoapp 8000:8000
```
Now, you can access the application from your browser:
👉 http://localhost:8000

2️⃣ Test API Endpoints Using curl
To verify that the application is running correctly, test these API endpoints:

Check Readiness Probe

```shell
curl http://localhost:8000/api/readiness
curl http://localhost:8000/api/liveness
```
