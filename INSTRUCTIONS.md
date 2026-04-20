# INSTRUCTION FOR NOOBIE:

## Applying manifest to run pods on cluster:
Choose workdir .infrastructure and run commands below or use absolute path to manifests

1. Creating namespace resource:
    ``` kubectl apply -f namespace.yml```
2. Creating busybox pod:
    ```kubectl apply -n todoapp -f busybox.yml```
3. Creating todoapp pod:
    ```kubectl apply -n todoapp -f todoapp-pod.yml```


## Testing todoapp:

### 1. Using the port-forwarding:
Run command for port-forward port on localhost to port in pod:

``` kubectl port-forward -n todoapp pod/todoapp 8081:8080```

8081 it's localport, and try connect in browser with this url:
http://localhost:8081

### 2. From cluster network:
Get ip-address of todoapp pod:

``` kubectl get pods -o wide -n todoapp ```

and find ip-of-todoapp pod for using in curl URL below.
________________________

get shell from busybox:curl pod:

```kubectl -n todoapp exec -it busybox -- sh```
______________________

Try to get page of app:
``` curl <ip-of-todoapp>:8080 ```