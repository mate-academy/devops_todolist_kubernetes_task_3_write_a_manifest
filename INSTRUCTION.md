1. To run app you should apply manifests using such commands in this order
    ```bash
    kubectl apply -f infrastructure/namespace.yml
    kubectl apply -f infrastructure/busybox.yml
    kubectl apply -f infrastructure/todoapp-pod.yml
    ```
2. To test this app using web interface do such commands
    ```bash
    kubectl port-forward pod/todoapp 8081:8080 -n todoapp
    ```
   Now the app is accessible by http://127.0.0.1:8081/
3. To test this app using curl
    ```bash
   kubectl get pods -n mateapp -o wide
    ```
   Run this command to get ip of todoapp node and copy it
    ```bash
    kubectl -n todoapp exec -it busybox -- sh
    ```
   Then get to shell of busybox node and make curl request `curl {node_ip}:8080`
