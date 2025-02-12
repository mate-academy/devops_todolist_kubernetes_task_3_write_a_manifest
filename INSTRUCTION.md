## INSTRUCTION

### 1.First start all manifests 

#### Create namespace
```bush
kubectl apply -f .infrastructure/namespace.yml
```
#### Run pods

```bush
kubectl apply -f .infrastructure/busybox.yml
kubectl apply -f .infrastructure/todoapp-pod.yml
```

### 2. Check logs:

```bash
kubectl logs todoapp -n todoapp
```

### 3. Check Pods details
```bash
kubectl describe pods -n todoapp
```

### 4. Use the port-forward command:
```bash
kubectl port-forward -n todoapp todoapp 8080:8080
```
### 5. Test the application using the busyboxplus:curl container
```bash
kubectl get pods -n todoapp -o wide
```
You will see something like:

`todoapp`   1/1     Running   0          37m   `10.1.0.29`

copy todoapp IP `10.1.0.29`

enter the busybox pod
```bash
kubectl exec -it busybox -n todoapp -- sh
```
and write a comand
```bash
curl 'todoapp IP':8080
