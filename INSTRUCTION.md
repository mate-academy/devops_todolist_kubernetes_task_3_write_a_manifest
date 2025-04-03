## Application of all manifests
Open terminal and change dir `cd .infrastructure` 
### Create namespace
```
kubectl apply -f namespace.yml
```

### Run pod todoapp-pod
```
kubectl apply -f todoapp-pod.yml
```

### Run pod busybox
```
kubectl apply -f busybox.yml
```

### Check the status of the pods
```
kubectl get pods -n todoapp
```

## Testing via `port-forward`
```
kubectl port-forward -n todoapp todoapp-pod 8080:8080
```
Then open browser and enter or `localhost:8080` - you will see page of app either `localhost:8080/api/ready/` - you will see `ready`

## Testing via busybox
Firstly check ip of `todoapp-pod` using command: `kubectl get pods -n todoapp -o wide`.

```
kubectl -n todoapp exec -it busybox -- sh
```

And in pod run this:
```
curl {todoapp-pod IP}:8080/api/health/
```
```angular2html
curl {todoapp-pod IP}:8080/api/ready/
```