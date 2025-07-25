To create any pod you should use command 
```
kubectl apply -f <manifest>
```
To see all pods in the namespace you should use command
```
kubectl get pods -n <namespace>
```
You can also take more deliberate description of pod:
```
kubectl describe pod <pod name> -n <namespace>
```
You can watch pod ip using command:
```
kubectl get pods -n <namespace> -o wide
```
You can connect to pod using command 
```
kubectl -n <namespace> exec -it <pod> -- sh
```
You can also redirect ports using command:
```
kubectl port-forward pod/<pod name> <port>:<port> -n <namespace>
```

To test our application you shoud connect to testing pod terminal and curl other pod ip(we shoud take other pod id)