# ToDo App Kubernetes Deployment

## 0. Build and push Docker image
```bash
docker build -t baga56789/todoapp:3.0.0 .
docker push baga56789/todoapp:3.0.0

## 1. How to apply manifests
kubectl apply -f .infrastructure/namespace.yml
kubectl apply -f .infrastructure/todoapp-pod.yml
kubectl apply -f .infrastructure/busybox.yml

## 2. Test using port-forward
kubectl port-forward pod/todoapp-pod 8000:8000 -n todoapp
# After running this, open http://localhost:8000 in your browser.

## 3. Test using busyboxplus:curl
kubectl exec -it busybox-curl -n todoapp -- sh
# Inside the container, run:
curl http://todoapp-pod:8000/api/liveness/
curl http://todoapp-pod:8000/api/readiness/