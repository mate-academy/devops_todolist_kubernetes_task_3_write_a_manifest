## apply all manifests
kubectl apply -f .infrastructure/namespace.yml
kubectl apply -f .infrastructure/busybox.yml
kubectl apply -f .infrastructure/todoapp-pod.yml

## test ToDo application using the port-forward command
kubectl port-forward pod/todoapp-pod 8081:8080 -n todoapp


## test the application using the busyboxplus:curl container
kubectl exec -it busybox -n todoapp -- sh 
curl http://10.244.0.5:8080/api/health/