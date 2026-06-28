# How to deploy and test the ToDo app:

## 1. Creation the namespace 
```
kubectl apply -f .infrastructure/namespace.yml
```

## 2. Check does the namespace created 
```
kubectl get namespace todoapp
```
it will return "Active" if it exists

## 3. Apply the busybox pod:
```
kubectl apply -f .infrastructure/busybox.yml
```

## 4. Apply the todoapp pod: 
```
kubectl apply -f .infrastructure/todoapp-pod.yml
```

## 5. Verify both pods are running
```
kubectl get pods -n todoapp
```

## 6. Test via kubectl port-forward
- create the temporary tunnel 
```
kubectl port-forward -n todoapp pod/todoapp 8000:8000
```
- test it with curl:
```
curl http://localhost:8000/api/ready/

```
- exit with Ctrl-C

---

## 7. Test via busyboxplus:curl pod
- open a shell inside the busybox pod:
```
kubectl exec -it -n todoapp busybox -- sh
```
- run curl from inside the pod:
```
curl http://todoapp:8000/api/ready/
```
- exit the shell:
```
exit
```
