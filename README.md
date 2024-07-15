How to apply all manifests:
kubectl apply -f .infrastructure/namespace.yml
kubectl apply -f .infrastructure/busybox.yml
kubectl apply -f .infrastructure/todoapp-pod.yml
Test ToDo application using the port-forward command:
kubectl port-forward pod/todoapp 8081:8080 -n todoapp
Test application using the busyboxplus:curl container
kubectl -n todoapp exec -it busybox -- sh
curl ip_pod_todoapp:8080