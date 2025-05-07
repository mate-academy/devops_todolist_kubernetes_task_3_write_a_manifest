## 1. Run the following commands from the project root:

kubectl apply -f .infrastructure/namespace.yml
kubectl apply -f .infrastructure/busybox.yml
kubectl apply -f .infrastructure/todoapp-pod.yml


## 2. To test the application from local browser or curl, use:

kubectl port-forward -n todoapp pod/todoapp 8000:8000


## 3. Test application from inside the cluster

kubectl exec -it -n todoapp busybox-curl -- sh

Inside the shell:
curl 10.1.0.21:8000/api/health/live
curl 10.1.0.21:8000/api/health/ready

