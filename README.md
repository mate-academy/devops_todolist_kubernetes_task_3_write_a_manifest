For using amazing todo application please follow instruction below

1. Create namespace for application

```
kubectl apply -f ./src/infrastructure/namespace.yml
```

2. Create 2 pods for application

```
kubectl apply -f ./src/infrastructure/todoapp-pod.yml
```

```
kubectl apply -f ./src/infrastructure/curl.yml
```

3. After you could read logs of running todoapp including readiness and liveness probe by executing

```
kubectl logs todoapp -n todoapp
```

4. Check for all working pods by executing command below

```
kubectl get pods -n todoapp -o wide
```

5. Find internal ip address for running todoapp, run interactive shell in curl pod by running command

```
kubectl exec -it -n todoapp curl -- sh
```

after check running todoapp pod inside cluster by running

```
curl <found internal ip>:8080
```

6. For enjoying fantastic todo application in browser, run port-forwarding setup

```
kubectl port-forward pod/todoapp 8081:8080 -n todoapp
```

Now you can enjoy fantastic todo application on http://localhost:8081/ or http://127.0.0.1:8081/
