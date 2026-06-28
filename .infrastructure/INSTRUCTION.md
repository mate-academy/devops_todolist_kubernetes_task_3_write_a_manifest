# Інструкції для запуску ToDoApp у Kubernetes

# Застосування маніфестів
kubectl apply -f .infrastructure/namespace.yml
kubectl apply -f .infrastructure/busybox.yml
kubectl apply -f .infrastructure/todoapp-pod.yml

# Тестування через port-forward
kubectl port-forward pod/todoapp 8000:8000 -n todoapp
# В іншому терміналі перевірте кінцеві точки
curl http://localhost:8000/api/ready/
curl http://localhost:8000/api/live/

# Тестування через busybox
kubectl exec -it busybox -n todoapp -- curl http://todoapp:8000/api/ready/
kubectl exec -it busybox -n todoapp -- curl http://todoapp:8000/api/live/

# Перевірити статус пода
kubectl get pods -n todoapp
kubectl describe pod todoapp -n todoapp

# Видалити всі ресурси
kubectl delete -f .infrastructure/todoapp-pod.yml -n todoapp
kubectl delete -f .infrastructure/busybox.yml -n todoapp
kubectl delete -f .infrastructure/namespace.yml

# Перевірити журнали
kubectl logs todoapp -n todoapp
