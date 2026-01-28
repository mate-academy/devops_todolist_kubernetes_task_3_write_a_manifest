Усі Kubernetes-маніфести знаходяться в папці .infrastructure у корені репозиторію. Для запуску застосунку спочатку застосовується маніфест namespace командою kubectl apply -f .infrastructure/namespace.yml, після чого запускаються pod з busyboxplus:curl контейнером та pod з ToDo застосунком командами kubectl apply -f .infrastructure/busybox.yml і kubectl apply -f .infrastructure/todoapp-pod.yml. Статус pod-ів перевіряється командою kubectl get pods -n todoapp.

Для перевірки ToDo застосунку з локального комп’ютера використовується port-forward: kubectl port-forward pod/todoapp-pod 8080:8080 -n todoapp. Після цього readiness та liveness endpoint-и доступні за адресами http://localhost:8080/ready і http://localhost:8080/health.

Для перевірки роботи застосунку зсередини кластера використовується busyboxplus:curl контейнер. Необхідно зайти в pod командою kubectl exec -it busybox -n todoapp -- sh і виконати запити curl http://todoapp-pod:8080/ready та curl http://todoapp-pod:8080/health.

Після завершення роботи створено Pull Request з усіма змінами та прикріплено для перевірки на платформі.