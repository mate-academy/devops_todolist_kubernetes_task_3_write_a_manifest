# Instruction
### How to Apply All Manifests
```
kubectl apply -f .infrastructure/namespace.yml
kubectl apply -f .infrastructure/busybox.yml
kubectl apply -f .infrastructure/todoapp-pod.yml
```
### Testing ToDo Application Using port-forward
```
kubectl port-forward pod/todoapp -n todoapp 8000:8000
```
- Visit http://localhost:8000 to access the application.
### Testing Application Using busyboxplus:curl
```
kubectl exec -it busybox -n todoapp -- curl http://todoapp:8000
kubectl exec -it busybox -n todoapp -- curl http://todoapp:8000/readiness
kubectl exec -it busybox -n todoapp -- curl http://todoapp:8000/liveness
```
or 

1. Retrieve the IP address of the TodoApp pod:
```
kubectl get pods -n todoapp -o wide
```
2. Access the BusyBox shell:
```
kubectl -n todoapp exec -it busybox -- sh
```
3. Send a curl request to the TodoApp:
```
curl <TodoApp_IP_address>:8080
```