# Applying all manifests:
kubectl apply -f ./infrastructure 

# A command to test application using the port-forward command:
kubectl port-forward pod/todoapp 8081:8080 -n todoapp

# Validate performance:
http://localhost

# Testing application using busybox container:
# Check ip address of todoapp.pod:

kubectl get pods -n todoapp -o wide

# Use this prompt to connect to the pod:

kubectl -n todoapp exec -it busybox -- sh

# Test this prompt:

curl (ip of todoapp.pod):8080
# Replace (ip of todoapp.pod) with the IP received via "kubectl get pods -n todoapp -o wide"
