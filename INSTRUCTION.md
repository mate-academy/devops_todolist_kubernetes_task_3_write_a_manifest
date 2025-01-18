# How to run the app

1. Create pods:

```
kubectl apply -f .infrastructure 
```

2. Test app using ports-forwarding:

```
kubectl port-forward pod/todoapp 8000:8080 -n todoapp
```

3. Test app using busybox:

4. Check the pod IP address:

```
kubectl get pods -n todoapp -o wide
```

5. Connect to the pod:

```
kubectl exec -it busybox -n todoapp -- curl http://todoapp:8000/readiness
kubectl exec -it busybox -n todoapp -- curl http://todoapp:8000/liveness
```

6. Check the app:

```
curl (ip of todoapp.pod):8080
```