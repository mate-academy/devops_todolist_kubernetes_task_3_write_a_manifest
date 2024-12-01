## How to apply all manifests

```
cd infrastructure 
kubectl apply -f namespace.yml  
kubectl apply -f todoapp-pod.yml  
kubectl apply -f busybox.yml  
```

## How to test ToDo application using the port-forward command

```
kubectl port-forward pod/todoapp 8081:8080 -n todoapp
```


## How to test application using the busyboxplus:curl container

```
kubectl get pods -o wide -n todoapp 
kubectl -n mateapp exec -it busybox -- sh
curl {todoapp IP}:8080
```