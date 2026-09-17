1. Apply the manifests

kubectl apply -f .infrastructure/namespace.yml
kubectl apply -n todoapp -f .infrastructure/mateapp-pod.yml
kubectl apply -n todoapp -f .infrastructure/busybox.yml

2. Confirm both pods are running

kubectl get pods -n todoapp -o wide

3. Test the app with kubectl port-forward

kubectl port-forward -n todoapp pod/mateapp 8080:8080
# paste the link into your browser 
http://localhost:8080/

4. Test the app from inside the cluster using the busybox pod

kubectl get pods -n todoapp -o wide
kubectl exec -it -n todoapp busybox -- sh
# once inside, get an IP adress and curl $IP

5. Clean up

kubectl delete namespace todoapp