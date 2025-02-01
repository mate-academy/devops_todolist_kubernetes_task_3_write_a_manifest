To apply the todoapp-pod.yml manifest run the following command:
kubectl apply -f .infrastructure/todoapp-pod.yml

To apply the busybox.yml manifest run:
kubectl apply -f .infrastructure/busybox.yml

To test ToDo application using the port-forward command run:
kubectl port-forward pod/todoapp 8080/8080
Once the command is executed, you can open in browser http://127.0.0.1:8080

To test the application using the busyboxplus:curl container do the following steps:
1. run kubectl get pods -o wide -n todoapp to find the IP address of the todoapp pod
    busybox   1/1     Running   9 (5m21s ago)   16h     10.1.0.8   docker-desktop   <none>           <none>
    todoapp   1/1     Running   0               5m49s   10.1.0.9   docker-desktop   <none>           <none>
    in this case the IP is 10.1.0.9
2. to open a command prompt on the busybox container run
   kubectl -n todoapp exec -it busybox --sh
3. run curl <todoapp IP>:8080 to test the app replacing <todoapp IP> with the IP obtained on the first step
