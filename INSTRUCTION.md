#To create namespace run:
kubectl apply -f .infrastructure/namespace.yml

#to create pods run:
kubectl apply -f .infrastructure/busybox.yml
kubectl apply -f .infrastructure/todoapp-pod.yml

#check pod status with:
kubectl get pods -n todoapp -o wide
#to open pod on in your browser run
kubectl port-forward pod/todoapp-pod 8081:8000 -n todoapp

#to test busybox run
kubectl -n todoapp exec -it busyboxplus -- sh
#and run then:
 curl http://todoapp:8000/api/live/