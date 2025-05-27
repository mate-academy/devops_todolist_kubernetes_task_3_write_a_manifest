## Apply manifests
kubectl apply -f .infrastructure/namespace.yml
kubectl apply -f .infrastructure/busybox.yml
kubectl apply -f .infrastructure/todoapp-pod.yml

## Port forward
kubectl port-forward pod/todoapp 8080:8080 -n todoapp

## Test with busybox
kubectl exec -it busybox -- curl http://todoapp:8080/health
