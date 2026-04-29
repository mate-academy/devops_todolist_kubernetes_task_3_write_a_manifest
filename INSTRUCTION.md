# Instructions

## Apply manifests
kubectl apply -f .infrastructure/namespace.yml
kubectl apply -f .infrastructure/busybox.yml
kubectl apply -f .infrastructure/todoapp-pod.yml

## Test with port-forward
kubectl port-forward -n todoapp pod/todoapp 8000:8000
# Open http://localhost:8000/api/health/

## Test with busybox
kubectl exec -it -n todoapp busybox -- curl http://todoapp:8000/api/health/