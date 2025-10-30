# створення namespace та перевірка 
kubectl apply -f .infrastructure/namespace.yml
kubectl get ns

# Запуск ToDo App pod
kubectl apply -f .infrastructure/todoapp-pod.yml
kubectl get pods -n todoapp

# Запуск pod з busybox+curl
kubectl apply -f .infrastructure/busybox.yml
kubectl get pods -n todoapp
# Для заходу в контейнер:
kubectl exec -it busybox-curl -n todoapp -- sh

# Тестування ToDo App через port-forward:
kubectl port-forward pod/todoapp 8000:8000 -n todoapp
# Відкрий у браузері:
http://localhost:8000/api/liveness/ → повинно показати OK
http://localhost:8000/api/readiness/ → повинно показати {"status": "ready"}

# Тестування ToDo App через busybox+curl
curl http://todoapp:8000/api/liveness/
curl http://todoapp:8000/api/readiness/

# Перевірка стану pod
kubectl get pods -n todoapp
kubectl describe pod todoapp -n todoapp
kubectl logs todoapp -n todoapp
