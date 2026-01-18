# Instruction

### How to deploy:

1. `kubectl apply -f .infrastructure/namespace.yml`
2. `kubectl apply -f .infrastructure/todoapp-pod.yml`
3. `kubectl apply -f .infrastructure/busybox.yml`

### How to test:

- **Port-forward:** `kubectl port-forward pod/todoapp 8080:8000 -n todoapp`
- **Internal check (busybox):**

1. `kubectl exec busybox -n todoapp -- sh`
2. `kubectl get pod todoapp -n todoapp -o wide`
3. `curl http://<TODOAPP_IP>:8000/api/health/live/`
