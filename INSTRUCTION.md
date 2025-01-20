# Instructions for deploying and testing ToDo application

## Apply manifests
1. Create the namespace:
   ```bash
   kubectl apply -f .infrastructure/namespace.yml

2. Deploy busybox pod:
    ```bash
   kubectl apply -f .infrastructure/busybox.yml

3. Deploy ToDo app pod::
    ```bash
   kubectl apply -f .infrastructure/todoapp-pod.yml
   
## Test ToDo application
 
1. Forward port to access the application locally:
    ```bash
    kubectl port-forward pod/todoapp -n todoapp 8000:8000
   
2. Test readiness and liveness endpoints:
    ```bash
   curl http://localhost:8000/readiness
   curl http://localhost:8000/liveness

## Test application using busybox

1. Execute a command in busybox pod:
    ```bash
   kubectl exec -it busybox -n todoapp -- sh

2. Test the application from inside the busybox pod:
    ```bash
   curl http://todoapp:8000/readiness
   curl http://todoapp:8000/liveness


