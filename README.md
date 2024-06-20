## To apply all manifests

Use commands:
```
kubectl apply -f .infrastructure/namespace.yml
```
```
kubectl apply -f .infrastructure/todoapp-pod.yml
```
```
kubectl apply -f .infrastructure/alpine.yml
```

## To test application using the port-forward command

Use this command:
```
kubectl port-forward pod/todoapp 8080:8080 -n todoapp
```

You can access the ToDo app in your browser at [http://localhost:8080](http://localhost:8080)

## To test application using 'Alpine' container

1. Get ip address of 'todoapp' pod:
```
kubectl get pods -n todoapp -o wide
```
2. Add the 'curl' package to the 'Alpine'
```
kubectl exec -it alpine -n todoapp -- apk --update add curl
```
3. Connect to 'Alpine'
```
kubectl exec -it alpine -n todoapp -- sh
```
4. Use commands:
```
curl http://{todoapp ip}:8080/api/liveness/
curl http://{todoapp ip}:8080/api/readiness/
```
