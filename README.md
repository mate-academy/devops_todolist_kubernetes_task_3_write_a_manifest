## How to run the app

1. Create pods:

```
kubectl apply -f .infrastructure 
```

2.1. Test app using ports-forwarding:

```
kubectl port-forward pod/todoapp 8081:8080 -n todoapp
```

2.2. Test app using busybox:

2.2.1. Check the pod IP address:

```
kubectl get pods -n todoapp -o wide
```

2.2.2 Connect to the pod:

```
kubectl -n todoapp exec -it busybox -- sh
```

2.2.3 Check the app:

```
curl (ip of todoapp.pod):8080
```