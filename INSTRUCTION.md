1. **Створіть Namespace**:
   - Виконайте команду для створення Namespace `todoapp`:

     kubectl apply -f .infrastructure/namespace.yml

   - Перевірте, чи Namespace створений:

     kubectl get namespaces


2. **Створіть Pod для додатку `todoapp`**:
   - Застосуйте маніфест Pod:

     kubectl apply -f .infrastructure/todoapp-pod.yml

   - Перевірте, чи Pod успішно створений:

     kubectl get pods -n todoapp


3. **Створіть Pod для тестування (`busybox`)**:
   - Застосуйте маніфест Pod:

     kubectl apply -f .infrastructure/busybox.yml

   - Переконайтеся, що Pod успішно створений:

     kubectl get pods -n todoapp


---

#### **Як тестувати додаток за допомогою команди `port-forward`**
1. **Прокиньте порт Pod локально**:
   - Виконайте команду:

     kubectl port-forward pod/todoapp 8000:8000 -n todoapp


2. **Перевірте доступність ендпоінтів**:
   - **Readiness Probe**:

     curl http://127.0.0.1:8000/api/readiness

     Очікувана відповідь: `ready`.

   - **Liveness Probe**:

     curl http://127.0.0.1:8000/api/liveness

     Очікувана відповідь: `live`.


#### **Як тестувати додаток за допомогою Pod `busybox`**
1. **Перевірте ендпоінти з Pod `busybox`**:
   - Перевірте Readiness Probe:

     kubectl exec -it busybox -n todoapp -- curl http://todoapp:8000/api/readiness

     Очікувана відповідь: `ready`.

   - Перевірте Liveness Probe:

     kubectl exec -it busybox -n todoapp -- curl http://todoapp:8000/api/liveness

     Очікувана відповідь: `live`.

2. **Перевірте інші маршрути (за потреби)**:
   - Наприклад, головну сторінку:

     kubectl exec -it busybox -n todoapp -- curl http://todoapp:8000/



#### Примітки
1. Усі маніфести (`namespace.yml`, `todoapp-pod.yml`, `busybox.yml`) мають бути розташовані у папці `.infrastructure`.
2. Використовуйте команди `kubectl logs` для перегляду логів Pod, якщо виникають помилки:
   ```bash
   kubectl logs <pod-name> -n todoapp

