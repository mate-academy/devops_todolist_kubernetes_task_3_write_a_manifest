# Інструкції для розгортання ToDo App у Kubernetes

## 1. Створення простору імен
```sh
 kubectl apply -f .infrastructure/namespace.yml
```
## 2. Розгортання BusyBox контейнера
```sh
 kubectl apply -f .infrastructure/busybox.yml
```
## 3. Розгортання ToDo App пода
``` sh
    kubectl apply -f .infrastructure/todoapp-pod.yml
```
## 4. Перевірка стану пода
``` sh
 kubectl get pods -n todoapp
```
## 5. Перевірка readiness та liveness
``` sh
 kubectl port-forward pod/todoapp 8080:8080 -n todoapp
curl http://localhost:8080/api/readiness/
curl http://localhost:8080/api/liveness/
```
## 6. Тестування з BusyBox
``` 
kubectl exec -it busybox -n todoapp -- curl http://todoapp:8080/api/readiness/
kubectl exec -it busybox -n todoapp -- curl http://todoapp:8080/api/liveness/
``` 

