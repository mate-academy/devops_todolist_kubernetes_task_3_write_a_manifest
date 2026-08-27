# Інструкція з розгортання та тестування ToDo App в Kubernetes

## 1. Застосування маніфестів

Виконайте наступні команди для створення Namespace та запуск ПОДів:


 1. Створення namespace
```
kubectl apply -f .infrastructure/namespace.yml
```

 2. Запуск додатка ToDo
```
kubectl apply -f .infrastructure/todoapp-pod.yml
```

 3. Запуск пода busybox
```
kubectl apply -f .infrastructure/busybox.yml
```
 Перевірити статус запусків:

```
kubectl get pods -n todoapp
```

## 2. Тестування додатка через Port-Forward

Для доступу до додатка з вашого локального браузера виконайте:
```
kubectl port-forward pod/todoapp 8000:8000 -n todoapp
```

Після цього додаток буде доступний за адресою:

Головна сторінка: http://localhost:8000

Readiness probe: http://localhost:8000/api/health/readiness/

Liveness probe: http://localhost:8000/api/health/liveness/

## 3. Тестування додатка з контейнера Busybox

Отримайте внутрішню IP-адресу пода todoapp:
```
kubectl get pod todoapp -n todoapp -o wide
```
Підключіться до контейнера busybox:
```
kubectl exec -it busybox -n todoapp -- sh
```

Усередині контейнера виконайте curl запити:

(Припустимо, IP-адреса: 10.244.0.5)

Перевірка головної сторінки/API

curl [http://10.244.0.5:8000/](http://10.244.0.5:8000/)

Перевірка readiness endpoint

curl [http://10.244.0.5:8000/api/health/readiness/](http://10.244.0.5:8000/api/health/readiness/)

Перевірка liveness endpoint

curl [http://10.244.0.5:8000/api/health/liveness/](http://10.244.0.5:8000/api/health/liveness/)

    

