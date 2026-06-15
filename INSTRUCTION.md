1. How to apply all manifests.
Go to the folder with manifests and run commands:
cd .infrastructure
kubectl apply -f namespace.yml
kubectl apply -f busybox.yml
kubectl apply -f todoapp-pod.yml

2. How to test ToDo application using the `port-forward` command.
Use command: kubectl port-forward pod/todoapp 8081:8080 -n todoapp

3. How to test the application using the `busyboxplus:curl` container.
Run commands:
kubectl get pods -n todoapp -o wide
Find IP under container name todoapp-pod
kubectl exec -it busybox -n todoapp -- sh
curl http://<todoapp-pod-ip>:8080