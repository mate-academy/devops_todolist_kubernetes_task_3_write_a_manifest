First of all, you have to apply manifests for create cluster:

Run kubectl apply namespace.yml - for creation namespace for cluster
Run kubectl apply busyb.yml - for creation pod with curl utility
Run kubectl apply todoapp-pod.yml - for creation pod with application
Great, after this 3 steps, you will have cluster with app!

If you want to test how application work in pods, you have 2 option:

Port-forward command: All you need is execute command kubectl port-forward pod/todoapp 8081:8080 -n todoapp and open application on localhost:8081

Curl:

In first, you need local ip address of your pod with app. Run this kubectl get pods -o wide -n todoapp
After you get local ip, you need go to curl shell utility. Run this kubectl -n todoapp exec -it busyb -- sh
Run curl {ip address your pod} in curl utility shell