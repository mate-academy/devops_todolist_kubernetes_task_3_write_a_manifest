kubectl apply -f .infrastructure/namespace.yml

kubectl apply -f .infrastructure/busybox.yml

kubectl apply -f .infrastructure/todoapp-pod.yml

kubectl port-forward pod/todoapp 8081:8080 -n todoapp
open http://localhost:8081

kubectl get pods -o wide -n todoapp
kubectl exec -it -n todoapp busybox -- sh
copy <todoapp-pod-ip>
root@busybox:/]$ curl http://<todoapp-pod-ip>:8080/health