Testing the ToDo application using port-forward:
1. Run the following command to forward a local port to the app pod: kubectl port-forward pod/todoapp-pod 8081:8080 -n todoapp
2. Once the command is running, you can access the ToDo app by opening: http://localhost:8081
3. Keep the terminal open while testing. Press Ctrl + C to stop the forwarding when done. 

Testing the ToDo application using the busyboxplus:curl container:
1. You need to get the IP of the ToDo app using the following command: kubectl get pods -n todoapp -o wide
2. Connect to the busybox pod: kubectl -n todoapp exec -it busybox-pod -- sh
3. Inside the shell: curl todoapp-pod_IP:8080
