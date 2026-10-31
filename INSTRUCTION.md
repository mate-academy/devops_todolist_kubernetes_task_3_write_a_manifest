# instructions on how to apply all manifests
kubectl apply -f namespace.yml
kubectl apply -f busybox.yml
kubectl apply -f todoapp-pod.yml

# P.S. if busybox.yml doesn't work use
kubectl apply -f alpine.yml

# instructions on how to test ToDo application using the port-forward command
kubectl port-forward pod/todoapp 8000:8000 -n todoapp
# url for local browser: http://127.0.0.1:8000/

# instructions on how to test the application using the busyboxplus:curl container
# run
kubectl describe pods -n todoapp todoapp
# find line "IP: 10.244.0.31" 

kubectl exec -it -n todoapp busybox -- sh
# if busybox doesn't work
kubectl exec -it -n todoapp alpine -- sh
# run command 
curl 127.0.0.1:8000
# you'll see html code 
