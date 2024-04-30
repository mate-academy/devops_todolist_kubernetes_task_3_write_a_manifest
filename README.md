# Django ToDo list

## To test the app we need to apply all manifests.
1. Get into the directory `infrastructure` to apply manifests using `cd` command
2. Use `kubectl apply -f namespace.yml`
3. Use `kubectl apply -f busybox.yml`
4. Use `kubectl apply -f todoapp-pod.yml`



## Testing the app using `port-forward` command
1. Use `kubectl port-forward pod/todoapp 8081:8080 -n mateapp`

## Testing the app using `busyboxplus:curl` command
1. Find the ip of the necessary pod using `kubectl get pods -o wide -n mateapp`
2. Get inside the busybox container `kubectl -n mateapp exec -it busybox -- sh`
3. Find the ip address of the app (in our case it is called todoapp) and use the command `curl your_ip:8080`. It should look like 'curl 10.1.0.15:8080'
