# Instruction on how to apply manifests and test application

## How to apply all manifests

```
cd .\infrastructure\
kubectl apply -f namespace.yml  
kubectl apply -f todoapp-pod.yml  
kubectl apply -f busybox.yml  
```

## How to test ToDo application using the port-forward command

```
kubectl port-forward pod/todoapp-3-0-0  8081:8080 -n todoapp
```

Once the port forward is set up, you can access the service running on the pod using `http://localhost:8080`

## How to test application using the busyboxplus:curl container

```
kubectl get pods -o wide -n todoapp 
kubectl -n mateapp exec -it busybox -- sh
```

Find todoapp container ip and execute next commnad:
```
curl {todoapp IP}:8080
```
Replace {todoapp IP} with your todoapp container IP
