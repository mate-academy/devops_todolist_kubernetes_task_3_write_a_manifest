Start:
image user2134567432/todoapp:3.0.0

apply manifest:
kubectl apply -f .infrastructure/namespace.yml
kubectl apply -f .infrastructure/todoapp-pod.yml
kubectl apply -f .infrastructure/busybox.yml

check: kubectl get pods -n todoapp
check: kubectl port-forward pod/todoapp 8000:8000 -n todoapp

curl http://localhost:8000/api/liveness/
curl http://localhost:8000/api/readiness/

check ip: kubectl get pod todoapp -n todoapp -o wide

kubectl exec -it busybox -n todoapp -- curl http://<IP_pode>:8000/api/liveness/
kubectl exec -it busybox -n todoapp -- curl http://<IP_pode>:8000/api/readiness/