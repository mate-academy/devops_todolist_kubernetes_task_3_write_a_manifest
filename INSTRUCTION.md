# Instructions for deploying and testing ToDo application

# How to apply the manifests:

kubectl apply -f todoapp-pod.yml -n todoapp
kubectl apply -f busybox.yml -n todoapp

# Testing the ToDo application:

kubectl port-forward pod/todoapp 8081:8080 -n todoapp

# After this, open your browser and go to:
# http://localhost:8081

# Using the busyboxplus:curl container to test:

kubectl -n todoapp exec -it busybox -- sh
curl <ip pod>:<port

