## To apply all manifests execute the next commands in the same order:

```shell
  kubectl apply -f .infrastructure/namespace.yml
  kubectl apply -f .infrastructure/busybox.yml
  kubectl apply -f .infrastructure/todoapp-pod.yml
```


## To test app with port forwarding execute next command:

```shell
  kubectl port-forward -n todoapp pod/todoapp 8080:8080
```
And open [localhost](http://localhost:8080)


## To test app with busybox container execute next command to get ip addresses of containers:

```shell
  kubectl get pods -o wide -n todoapp
```
Run this command to connect to the container shell:

```shell
  kubectl -n todoapp exec -it busybox -- sh
```

And run curl command inside the busybox container:

```shell
    curl {todo-app-container-ip}:8080
```
