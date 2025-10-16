1. Apply all manifests 

kubectl apply -f namespace.yml
kubectl apply -f busybox.yml -n todoapp
kubectl apply -f todoapp-pod.yml -n todoapp

2. Test ToDo application with port-forward

kubectl port-forward pod/todoapp -n todoapp 8000:8000
 
  http://localhost:8000
 
  http://localhost:8000/api/

3. Test readiness and liveness endpoints

readiness
curl http://localhost:8000/api/readiness/
liveness
curl http://localhost:8000/api/liveness/

4. Test application using busyboxplus:curl pod

kubectl exec -it busybox -- /bin/sh

curl http://todoapp:8000/
curl http://todoapp:8000/api/readiness/
curl http://todoapp:8000/api/liveness/

5. Delete all resources

kubectl delete namespace todoapp

This file should be located in the root of the repository.
The names of the pods and files should match those in .infrastructure.
