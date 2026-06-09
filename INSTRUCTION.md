kubectl port-forward pod/todoapp-pod 8080:8000 -n todoapp
Clone repository
git clone <repository>
Start Kubernetes, open console and go to folder with file repository
go to folder ".infrastructure"
create namespace
kubectl apply -f namespace.yml
create busybox app
kubectl apply -f busybox.yml
create todoapp app
kubectl apply -f todoapp-pod.yml
check app in pod
kubectl get pods -n todoapp
and view detal information on todoapp app 
kubectl describe pods -n todoapp todoapp-pod
then check listen port using busybox app
run kubectl get pods -n todoapp -o wide
find IP todoapp-pod and remember
then run kubectl -n todoapp exec -it busybox -- sh
and run 
curl http://<remember IP todoapp-pod>:8000/api/readiness
curl http://<remember IP todoapp-pod>:8000/api/liveness
or use name
curl http://todoapp-pod:8000/api/readiness
curl http://todoapp-pod:8000/api/liveness
if alredy fine forward port to local port
kubectl port-forward pod/todoapp-pod 8080:8000 -n todoapp
go to page in browser http://localhost:8080