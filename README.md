1. Apply manifests by commands
   `kubectl apply -f ./.infrastructure/namespace.yml`
   `kubectl apply -f ./.infrastructure/busybox.yml`
   `kubectl apply -f ./.infrastructure/todoapp-pod.yml`

1. Port-forwarding
   run `kubectl port-forward pod/todoapp-pod 8081:8080 -n todoapp`
   visit `http://0.0.0.0:8081/api/health/`
   visit `http://0.0.0.0:8081/api/ready/` after ~ 40s refresh page to get updated status

1. Test app via curl
   get todoapp-pod ip `kubectl get pods -n todoapp -o wide`
   open todo app in interactive mode `kubectl -n todoapp exec -it curlpod -- sh`
   make a request `curl [ip from step 1]:8080/api/health/`
   make a request `curl [ip from step 1]:8080/api/ready/` after ~ 40s make another request to get updated status
