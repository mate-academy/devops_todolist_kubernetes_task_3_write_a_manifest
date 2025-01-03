# Work with Kubernetes

1. Apply all manifests:

```bash
kubectl apply -f '.infrastructure/*.yml'
```

2. Forward ports:

```bash
kubectl port-forward pod/todoapp 8080:8080 -n todoapp
```

Now, you can access you application by the following URL `http://127.0.0.1:8080`.

3. Test the application using the the helper container:

- run the following command to get the container IP address:

```bash
kubectl get po -n todoapp -o wide
```

- connect to the helper container:

```bash
kubectl exec -it -n todoapp pod/busybox -- sh
```

- make a request to the app with a `curl` command:

```bash
curl <POD_IP_ADDRESS>:<PORT>/path
```
