# Instructions for Deploying and Testing Todo App

## 1. How to apply all manifests
Виконайте наступні команди з кореневої директорії проєкту для розгортання інфраструктури:

```bash
# Створення простору імен (Namespace)
kubectl apply -f .infrastructure/namespace.yml

# Запуск основного поду з Django ToDo додатком
kubectl apply -f .infrastructure/todoapp-pod.yml

# Запуск допоміжного поду busybox для тестування мережі
kubectl apply -f .infrastructure/busybox.yml
```

Перевірити статус запуску подів можна за допомогою команди:
```bash
kubectl get pods -n todoapp
```
*Зачекайте, поки обидва поди перейдуть у статус `Running` із показником `READY 1/1`.*

## 2. Testing using the `port-forward` command
Щоб перевірити роботу програми через браузер вашого локального комп'ютера, виконайте команду:

```bash
kubectl port-forward pod/todoapp-pod 8000:8000 -n todoapp
```
Залиште цей термінал відкритим та перейдіть у браузері за посиланнями:
* Головна сторінка: [http://localhost:8000/](http://localhost:8000/)
* REST API: [http://localhost:8000/api/](http://localhost:8000/api/)
* Readiness Probe: [http://localhost:8000/api/health/ready/](http://localhost:8000/api/health/ready/)

## 3. Testing using the `busyboxplus:curl` container
Для перевірки доступності програми всередині самого кластера Kubernetes:

```bash
# 1. Дізнайтеся внутрішню IP-адресу поду todoapp-pod
kubectl get pod todoapp-pod -n todoapp -o jsonpath='{.status.podIP}'

# 2. Зробіть запит з поду busybox (замініть <POD_IP> на отриману адресу, наприклад 10.244.0.7)
kubectl exec -it busybox-curl -n todoapp -- curl http://<POD_IP>:8000/api/health/ready/
```