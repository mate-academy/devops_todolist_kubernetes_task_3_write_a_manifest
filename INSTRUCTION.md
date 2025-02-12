## Run instructions
1. Apply all manifests:
    ```bash
    kubectl apply -f namespace.yml
    kubectl apply -f busybox.yml
    kubectl apply -f todoapp-pod.yml
    ```
2. Check the status of the pods:
    ```bash
    kubectl get pods -n todoapp
    ```
3. Run the following command to get the IP address of the pod:
    ```bash
    kubectl get pods -n todoapp -o wide
    ```
4. Run the following command to get the logs of the pod:
    ```bash
    kubectl logs -n todoapp <pod-name>
    ```
5. To port forward the pod:
    ```bash
    kubectl port-forward -n todoapp todoapp 8080:8080
    ```
6. To delete the resources:
    ```bash
    kubectl delete -f namespace.yml
    kubectl delete -f busybox.yml
    kubectl delete -f todoapp-pod.yml
    ```
