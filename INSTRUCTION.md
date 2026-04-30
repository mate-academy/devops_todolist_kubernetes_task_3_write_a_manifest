kubectl apply -f .infrastructure/namespace.yml
kubectl apply -f .infrastructure/todoapp-pod.yml
kubectl apply -f .infrastructure/busybox.yml


kubectl port-forward pod/todoapp-pod 8000:8000
# потім відкрити http://localhost:8000

kubectl exec -it busybox -- curl http://todoapp:8000/api/todos/