# Інструкції для розгортання ToDo додатку в Kubernetes

## Як застосувати маніфести

1.  Створіть namespace:

    ```
    kubectl apply -f .infrastructure/namespace.yml
    ```

2.  Створіть busybox-под:

    ```
    kubectl apply -f .infrastructure/busybox.yml
    ```

3.  Створіть todoapp-под:

    ```
    kubectl apply -f .infrastructure/todoapp-pod.yml
    ```

## Тестування

**a) Через port-forward:**

```
kubectl port-forward pod/todoapp 8000:8000
```

Відкрийте [http://localhost:8000](http://localhost:8000) у браузері.

**b) Через busybox:**

```
kubectl exec -it busybox -- curl http://todoapp:8000
```
```
