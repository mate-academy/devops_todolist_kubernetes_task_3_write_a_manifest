# Kubernetes ToDo App

## Apply manifests

Create namespace:

kubectl apply -f .infrastructure/namespace.yml

Create busybox pod:

kubectl apply -f .infrastructure/busybox.yml

Create todoapp pod:

kubectl apply -f .infrastructure/todoapp-pod.yml

Check pods:

kubectl get pods -n todoapp

---

## Test application using port-forward

Run port-forward:

kubectl port-forward pod/todoapp 8080:8080 -n todoapp

Open in browser:

http://localhost:8080/ready

http://localhost:8080/health

---

## Test application using busybox container

Connect to busybox pod:

kubectl exec -it busybox -n todoapp -- sh

Run curl commands:

curl http://todoapp:8080/ready

curl http://todoapp:8080/health