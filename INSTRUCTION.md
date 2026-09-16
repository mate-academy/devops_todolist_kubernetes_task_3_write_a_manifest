# ToDo App Kubernetes Instructions

## 1. Apply Kubernetes manifests

Create the namespace:

kubectl apply -f .infrastructure/namespace.yml

Create the ToDo application Pod:

kubectl apply -f .infrastructure/todoapp-pod.yml

Create the BusyBox Pod:

kubectl apply -f .infrastructure/busybox.yml

Check that the Pods are running:

kubectl get pods -n todoapp

Both Pods should have the Running status.


## 2. Test the application using port-forward

Forward local port 8000 to the ToDo application Pod:

kubectl port-forward pod/todoapp 8000:8000 -n todoapp

Open the application in a browser:

http://localhost:8000

Readiness endpoint:

http://localhost:8000/api/ready/

Liveness endpoint:

http://localhost:8000/api/health/


## 3. Test the application from the BusyBox Pod

Get the ToDo Pod IP address:

kubectl get pods -n todoapp -o wide

Enter the BusyBox container:

kubectl exec -it busybox -n todoapp -- /bin/sh

Use the ToDo Pod IP from the previous command to test readiness:

curl http://<TODOAPP_POD_IP>:8000/api/ready/

Expected response:

Ready

Test liveness:

curl http://<TODOAPP_POD_IP>:8000/api/health/

Expected response:

Healthy
