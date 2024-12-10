In order to apply all manifests from .infrastructure do:
kubectl apply -f namespace.yml
kubectl apply -f todoapp-pod.yml
kubectl apply -f alpine.yml

After applying the changes you can test the launched pod by making requests to it from the host machine, in order to do that first apply port forwarding as follows:
kubectl port-forward pod/todoapp-pod 8080:8080 -n todoapp

Or, alternatively send a request from anoteher pod in order to do that:
1. Get the IP of the pod running the todoapp server:
kubectl get pods -n todoapp -o wide
2. Exec into the alpine pod:
kubectl exec -it -n todoapp alpine-curl -- /bin/sh
3. Use the curl command to make a request to the server:
curl -v http://<ip-address>:8080/api/liveness
