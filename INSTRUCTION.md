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
if alredy fine forward port
kubectl port-forward pod/todoapp-pod 8080:8000 -n todoapp
go to page in browser http://localhost:8080