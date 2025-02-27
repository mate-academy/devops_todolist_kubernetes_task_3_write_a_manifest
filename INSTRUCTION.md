First of all create a namespace for our app:

```
kubectl apply -f namespace.yml
```

Then start our app in our namespace called todoapp-namespace:
```
kubectl apply -f pytodoapp.yml
```

To forward the app port to your host port 8080 simply type in bash following command:
```
kubectl port-forward pod/todoapp 8080:8080 -n todoapp-namespace
```

Then optionaly you can start busybox with curl:
```
kubectl apply -f busybox.yml
```

define our todoapp IP in the namespace:
```
kubectl get pods -o wide -n todoapp-namespace
```

connect to curl in our pod:
```
kubectl -n todoapp-namespace exec -it busybox -- sh
```

and test the app with curl in the terminal:
```
curl <todoapp IP address>:8080
```
