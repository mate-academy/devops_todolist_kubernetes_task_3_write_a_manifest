## To apply all manifests run command:

```
kubectl apply -f .infrastructure/
```

## To test application using `port-forward` run this command:

```
kubectl -n todoapp port-forward pod/todoapp 8081:8000
```

## To get info about your pod ip adress

```
kubectl get pods -n todoapp -o wide
```

## To test application using `busy-box` run this commands:

```
kubectl -n todoapp exec -it busybox -- sh
```

You will find yourself in the shell (terminal), after this run the command: 

```
curl {ip of your pod}:8000
```