# Instructions for Kubernetes Manifests

## Applying All Manifests

1. Ensure you are connected to your Kubernetes cluster.
2. Apply the namespace manifest:
   kubectl apply -f .infrastructure/namespace.yml
3. Apply the ToDo app pod manifest:
   kubectl apply -f .infrastructure/todoapp-pod.yml
4. Apply the BusyBox pod manifest:
   kubectl apply -f .infrastructure/busybox.yml

## Testing ToDo Application Using Port-Forward

1. Forward the port of the ToDo app pod to your local machine:
   kubectl port-forward pod/todoapp-pod -n todoapp 8080:8080
2. Open your browser and navigate to:
   http://localhost:8080
3. Verify that the ToDo application is accessible.

## Testing the Application Using BusyBox Container

1. Retrieve the APP_IP for the todoapp pod:
   kubectl get pod todoapp-pod -n todoapp -o wide
   The APP_IP will be listed under the "IP" column.
2. Execute a command in the BusyBox pod to test the readiness endpoint:
   kubectl exec -it busybox -n todoapp -- curl -X GET http://<APP_IP>:8080/api/ready
3. Execute a command in the BusyBox pod to test the liveness endpoint:
   kubectl exec -it busybox -n todoapp -- curl -X GET http://<APP_IP>:8080/api/health
4. Verify that both commands return a `200 OK` response.