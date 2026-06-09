# Instructions

## Apply all manifests

kubectl apply -f .infrastructure/namespace.yml
kubectl apply -f .infrastructure/todoapp-pod.yml
kubectl apply -f .infrastructure/busybox.yml

## Test with port-forward

kubectl port-forward pod/todoapp 8080:8080 -n todoapp

Open in browser: http://localhost:8080

## Test using busyboxplus container

kubectl exec -it busybox -n todoapp -- curl http://todoapp:8080/api/health/
kubectl exec -it busybox -n todoapp -- curl http://todoapp:8080/api/ready/