Use command:
`alias kub=kubectl`
this will make less typing for local session

Apply manifests in following order:
 - `kubectl apply -f ./.infrastructure/namespace.yml`
 - `kubectl apply -f ./.infrastructure/busybox.yml`
 - `kubectl apply -f ./.infrastructure/todoapp-pod.yml`

In order to test the app from local browser use following command to enable port forwarding:
    `kubectl port-forward pod/todoapp 8081:8080 -n todoapp`
when forwarding started - user browser to navigate to `127.0.0.1:8081` and you will be redirected to pod.

 to use busybox:curl run following commands:
- get ip address of needed pod with command:
    `kubectl get pods -n todoapp -o wide`
- `kubectl -n todoapp exec -it busybox -- sh`
- `curl ip.address:8080`
- `exit` to exit pods shell
