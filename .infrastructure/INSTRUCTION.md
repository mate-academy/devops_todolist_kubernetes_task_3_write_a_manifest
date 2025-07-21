# Інструкція

1. Застосувати маніфести:
```bash
kubectl apply -f .infrastructure/namespace.yml
kubectl apply -f .infrastructure/
```

2. Тестування через port-forward:
```bash
kubectl port-forward pod/todoapp 8000:8000 -n todoapp
```
Відкрийте http://localhost:8000

3. Тестування через busybox:
```bash
kubectl exec -it busybox -n todoapp -- curl http://todoapp:8000
```