## How to apply all manifests
Use command:
```
kubectl apply -f .infractructure/
```

## How to test application using the port-forward command
Use this command:
```
kubectl port-forward pod/todoapp 8081:8080 -n todoapp
```
# Content will appear at: 
```
localhost:8081
```

## How to test application using 'busybox' container
First of all, we need to get ip address of 'busybox' pod:
```
kubectl get pods -n todoapp -o wide
```

# Next we need to connect to the pod
```
kubectl -n todoapp exec -it busybox -- sh
```

# Finally, use this command:
```
curl {ip_address_of_busybox_pod}
