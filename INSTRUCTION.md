## 1. Apply Kubernetes manifests
Run the following commands from the project root directory to deploy all resources:

1. **Create Namespace:**
   ```bash
   kubectl apply -f .infrastructure/namespace.yml
   ```

2. **Create Pod ToDo::**
    ```bash
   kubectl apply -f .infrastructure/todoapp-pod.yml -n todoapp
    ```

3. **Create Pod Pod BusyBox:**
    ```bash
   kubectl apply -f .infrastructure/busybox.yml -n todoapp
    ```

## 2. Test using Port-Forward

1. **Make command:**
    ```bash
   kubectl port-forward pod/todoapp 8080:8080 -n todoapp
    ```
2. **Check in Browser:**
    ```bash
   http://localhost:8080
    ```

## 3. Test using BusyBox

1. **Connect to conteiner BusyBox:**
    ```bash
   kubectl exec -it busy -n todoapp -- sh
    ```
2. **endpoints liveness та readiness:**
    ```bash
   curl http://todoapp:8080/api/health/
   curl http://todoapp:8080/api/ready/
    ```


## 4. Check the status of Pod

   ```bash
   kubectl get pods -n todoapp
   ```
You shoud see: 1/1 READY