# Run manifests

kubectl apply -f .infrastructure/namespace.yml

kubectl apply -f .infrastructure/busybox.yml

kubectl apply -f .infrastructure/todoapp-pod.yml


# Check pods

kubectl get pods -n todoapp


# Port forward

kubectl port-forward pod/todoapp-pod 8000:8000 -n todoapp


# Busybox test

kubectl exec -it busybox -n todoapp -- sh

curl http://todoapp-pod:8000/readiness

curl http://todoapp-pod:8000/liveness