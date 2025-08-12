kubectl apply -f .infrastructure/namespace.yml
kubectl apply -f .infrastructure/todoapp-pod.yml
kubectl apply -f .infrastructure/busybox.yml

kubectl port-forward pod/todoapp 8081:8080 -n todoapp

kubectl get pods -o wide -n todoapp
kubectl -n todoapp exec -it busybox -- sh
curl 10.1.0.36:8080/api/liveness/
curl 10.1.0.36:8080/api/readiness/
