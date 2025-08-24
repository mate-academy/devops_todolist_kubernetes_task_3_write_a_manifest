Apply manifest to create a todoapp namespace by running the command:
kubectl apply -f ./infrastructure/namespace.yml
Apply manifest to run the busybox by running the command:
kubectl apply -f ./infrastructure/busybox.yml
Apply manifest to run the todoapp by running the command:
kubectl apply -f ./infrastructure/todoapp.yml
To test application use kubectl port-forward command:
kubectl port-forward whatmodeprog/todoapp:3.0.0 8080:8081 -n todoapp
To test application use curl command inside of busybox container:
 1) Check todoapp pod IP address using command: kubectl get pod todoapp -n todoapp -o wide
 2) Connect to the container using command: kubectl -n todoapp exec -it busybox -- sh
 3) Run curl command to check health endpoint: curl <todoapp-pod-IP>:8080/api/health
 4) Run curl command to check ready endpoint: curl <todoapp-pod-IP>:8080/api/ready