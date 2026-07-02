# Firstly we create a namespace using this command:

```bash
kubectl apply -f .infrastructure/namespace.yml
```

# Now, when we are sure that namespace was created we can apply pods by using this command:

```bash
kubectl apply -f .infrastructure/
```

# Then checking status of pods that we just applied:

```bash
kubectl get pods -n todoapp
```

# This command help you to test ToDo application:

```bash
kubectl port-forward pod/todoapp-pod 8000:8000 -n todoapp
```

# To test the application from inside the cluster using the busybox container:
# Firstly, connect to the running busybox container interactively:
```bash
kubectl exec -it busybox -n todoapp -- sh
```
# Inside the busybox terminal, use curl to check the application's liveness endpoint:

curl http://todoapp-pod:8000/api/liveness/

# To exit the busybox container terminal, simply type:

exit

