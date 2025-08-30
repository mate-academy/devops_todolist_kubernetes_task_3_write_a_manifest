# Инструкция по развертыванию ToDo приложения в Kubernetes

## Обзор

Данная инструкция описывает процесс развертывания Django ToDo приложения в Kubernetes кластере с использованием подготовленных манифестов.

## Предварительные требования

- Работающий Kubernetes кластер
- Установленный `kubectl` с настроенным доступом к кластеру
- Docker образ приложения `{yourname}/todoapp:3.0.0` должен быть доступен в Docker Hub

## Структура проекта

```
.infrastructure/
├── namespace.yml       # Создание namespace для приложения
├── busybox.yml        # Pod для тестирования с curl
└── todoapp-pod.yml    # Основной pod с ToDo приложением
```

## Шаг 1: Сборка и публикация Docker образа

### 1.1 Сборка образа

```bash
# Из корневой директории проекта
docker build -t {yourname}/todoapp:3.0.0 .
```

### 1.2 Публикация в Docker Hub

```bash
# Авторизация в Docker Hub
docker login

# Публикация образа
docker push {yourname}/todoapp:3.0.0
```

**Важно:** Замените `{yourname}` на ваш реальный username в Docker Hub в файле `.infrastructure/todoapp-pod.yml`

## Шаг 2: Применение манифестов

### 2.1 Создание namespace

```bash
kubectl apply -f .infrastructure/namespace.yml
```

Проверка создания namespace:

```bash
kubectl get namespaces | grep todoapp
```

### 2.2 Развертывание ToDo приложения

```bash
kubectl apply -f .infrastructure/todoapp-pod.yml
```

### 2.3 Развертывание тестового контейнера

```bash
kubectl apply -f .infrastructure/busybox.yml
```

### 2.4 Проверка состояния подов

```bash
kubectl get pods -n todoapp
```

Ожидаемый вывод:

```
NAME           READY   STATUS    RESTARTS   AGE
busybox-curl   1/1     Running   0          1m
todoapp-pod    1/1     Running   0          2m
```

## Шаг 3: Тестирование приложения с помощью port-forward

### 3.1 Настройка port-forward

```bash
kubectl port-forward -n todoapp pod/todoapp-pod 8000:8000
```

### 3.2 Тестирование endpoints

В новом терминале выполните:

```bash
# Проверка основного приложения
curl http://localhost:8000/

# Проверка API
curl http://localhost:8000/api/

# Проверка readiness probe
curl http://localhost:8000/api/health/readiness/

# Проверка liveness probe
curl http://localhost:8000/api/health/liveness/
```

Ожидаемые ответы health checks:

```json
# Readiness
{
  "status": "ready",
  "timestamp": "2024-01-01T12:00:00.000Z",
  "checks": {
    "database": "ok"
  }
}

# Liveness
{
  "status": "alive",
  "timestamp": "2024-01-01T12:00:00.000Z",
  "uptime": 1704110400.0
}
```

## Шаг 4: Тестирование с помощью busybox контейнера

### 4.1 Подключение к busybox контейнеру

```bash
kubectl exec -it -n todoapp busybox-curl -- /bin/sh
```

### 4.2 Тестирование из busybox контейнера

Внутри busybox контейнера выполните:

```bash
# Получение IP адреса todoapp-pod
nslookup todoapp-pod.todoapp.svc.cluster.local

# Или можно использовать прямой доступ по IP
# Сначала получите IP пода:
# kubectl get pod -n todoapp todoapp-pod -o wide

# Тестирование основного приложения (замените IP на актуальный)
curl http://<POD_IP>:8000/

# Тестирование API
curl http://<POD_IP>:8000/api/

# Тестирование health checks
curl http://<POD_IP>:8000/api/health/readiness/
curl http://<POD_IP>:8000/api/health/liveness/

# Тестирование с выводом заголовков
curl -I http://<POD_IP>:8000/api/health/readiness/
```

### 4.3 Получение IP адреса пода для тестирования

```bash
# Из основного терминала
kubectl get pod -n todoapp todoapp-pod -o wide
```

## Шаг 5: Мониторинг и отладка

### 5.1 Просмотр логов

```bash
# Логи ToDo приложения
kubectl logs -n todoapp todoapp-pod

# Логи с отслеживанием в реальном времени
kubectl logs -f -n todoapp todoapp-pod

# Логи busybox контейнера
kubectl logs -n todoapp busybox-curl
```

### 5.2 Проверка health checks

```bash
# Описание пода с информацией о пробах
kubectl describe pod -n todoapp todoapp-pod
```

### 5.3 Отладка проблем

```bash
# Подключение к контейнеру приложения
kubectl exec -it -n todoapp todoapp-pod -- /bin/bash

# Проверка переменных окружения
kubectl exec -n todoapp todoapp-pod -- env

# Проверка сетевого доступа
kubectl exec -it -n todoapp busybox-curl -- wget -qO- http://todoapp-pod:8000/api/health/liveness/
```

## Шаг 6: Очистка ресурсов

### 6.1 Удаление подов

```bash
kubectl delete -f .infrastructure/todoapp-pod.yml
kubectl delete -f .infrastructure/busybox.yml
```

### 6.2 Удаление namespace (удалит все ресурсы в нем)

```bash
kubectl delete -f .infrastructure/namespace.yml
```

## Устранение неполадок

### Проблема: Pod не запускается

1. Проверьте доступность образа: `docker pull {yourname}/todoapp:3.0.0`
2. Проверьте логи: `kubectl logs -n todoapp todoapp-pod`
3. Проверьте описание пода: `kubectl describe pod -n todoapp todoapp-pod`

### Проблема: Health checks не проходят

1. Убедитесь, что endpoints доступны через port-forward
2. Проверьте логи приложения на наличие ошибок
3. Проверьте, что приложение слушает на порту 8000

### Проблема: Нет доступа к приложению

1. Проверьте состояние пода: `kubectl get pods -n todoapp`
2. Убедитесь, что readiness probe прошел успешно
3. Проверьте сетевые политики кластера

## Дополнительная информация

- **Readiness Probe**: проверяет готовность приложения принимать трафик (проверка БД)
- **Liveness Probe**: проверяет, что приложение живо и отвечает
- **Namespace**: изолирует ресурсы приложения от других компонентов кластера
- **Resource Limits**: ограничивают потребление ресурсов подом

## Полезные команды

```bash
# Просмотр всех ресурсов в namespace
kubectl get all -n todoapp

# Просмотр событий в namespace
kubectl get events -n todoapp

# Просмотр использования ресурсов
kubectl top pod -n todoapp

# Проверка работы DNS
kubectl exec -it -n todoapp busybox-curl -- nslookup kubernetes.default.svc.cluster.local
```
