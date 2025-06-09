# Instructions

## 1. Apply All Manifests

To deploy all Kubernetes manifests in this directory, run:

```sh
kubectl apply -f .
```

## 2. Test the ToDo Application Using Port-Forward

Forward the application's service port to your local machine:

```sh
kubectl port-forward pod/todoapp 8000:8000 -n todoapp
```

Then, access the application at [http://localhost:8000](http://localhost:8000) in your browser or use `curl`:

```sh
curl http://localhost:8000
```

## 3. Test the Application Using busyboxplus:curl

Find IP of todoapp:

```sh
kubectl get pods -o wide -n todoapp
```

Get inside pod with busybox:

```sh
kubectl -n todoapp exec -it busybox -- sh
```

Inside the pod, test the application's service (replace `<service-ip>` from previous step):

```sh
curl http://<service-ip>:8000
```
