# Instructions for using manifests in the infrastructure file:



## Instructions for using manifest namespace.yml

Enter this command in the terminal to create the described namespace:

```bash
kubectl apply -f .infrastructure/namespace.yml
```

## Instructions for using manifest todoapp-pod.yml

Enter this command in the terminal to create the described Pod:
```bash
kubectl apply -f .infrastructure/todoapp-pod.yml
```

## Instructions for using manifest busybox.yml

Enter this command in the terminal to create the described Pod:
```bash
kubectl apply -f .infrastructure/busybox.yml
```
To test the application using the busybox container, you need to check the IP address of the todoapp application:
```bash
kubectl get pods -o wide -n todoapp
```
Next you need to open an interactive shell session inside pod:
```bash
kubectl exec -it -n todoapp busybox -- sh
```
Inside the container, execute the application verification request:
```bash
curl http://<IP-address todoapp>:8000
```
If everything works, `exit` command to exit the container


## Instructions for testing the ToDo application using the port-forward command

Open a terminal and enter the command to connect to your pod or service in Kubernetes:
```bash
kubectl port-forward pod/todoapp 8000:8000 -n todoapp
```
Leave this terminal open as the tunnel is only running while the command is running.

Open a browser and go to http://localhost:8000 to see your application's interface or response live.