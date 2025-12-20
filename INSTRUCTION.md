<!-- go to infrastructure folder within cloned directory-->

cd infrastructure

<!-- create namespace -->
kubectl apply -f ./namespace.yml

<!-- check namespace is in the list -->
kubectl get namespaces  

<!-- create pods -->
kubectl apply -f ./busybox.yml  
kubectl apply -f ./todoapp-pod.yml

<!-- check pods is in the list -->
kubectl get pods -n todoapp

<!-- add port forward -->
kubectl port-forward todoapp 8000:8000 -n todoapp

<!-- access app from your browser -->

http://localhost:8000/