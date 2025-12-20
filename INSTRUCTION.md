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

<!-- to test from app -->
<!-- get todo app IP from command below -->
kubectl get pod -n todoapp -o wide
<!-- acess busybox  -->
kubectl exec -n todoapp -it busybox -- sh
<!--run -->
curl http://<TODOAPP_IP_ADDRESS>:8000

<!-- to test from your laptop -->
<!-- add port forward -->
kubectl port-forward todoapp 8000:8000 -n todoapp

<!-- access app from your browser -->

http://localhost:8000/