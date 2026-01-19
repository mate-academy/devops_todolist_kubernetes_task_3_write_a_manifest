Run namespace.yml: kubectl apply -f .infrastructure/namespace.yml

Run busybox.yml: kubectl apply -f .infrastructure/busybox.yml -n todoapp

Run todoapp-pod.yml: kubectl apply -f .infrastructure/todoapp-pod.yml -n todoapp

Test port-forward: kubectl port-forward pod/todoapp 8081:8080 -n todoapp

Get todoapp ip: kubectl get pods -o wide

Test busybox curl: kubectl -n todoapp exec -it busybox -- sh
curl <todoapp-pods-ip>:8080