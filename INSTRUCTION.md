## to apply manifests execute commands:
1. namespace: `kubectl apply -f .\.infrastructure\namespace.yml`
2. busybox: `kubectl apply -f .\.infrastructure\busybox.yml`
3. todoapp: `kubectl apply -f .\.infrastructure\todoapp-pod.yml`

## to configure port forwarding execute `kubectl port-forward pod/todoapp 8001:8000 -n todoapp`
To get to API open `http://127.0.0.1:8001/api` in browser. 

## to curl api from CLI:
1. Execute `kubectl get pods -n todoapp -o wide` and get IP of `todoapp` application
2. execute command `kubectl exec -it busyboxplus -n todoapp -- sh`
3. execute command `curl {todoapp IP}:8000`