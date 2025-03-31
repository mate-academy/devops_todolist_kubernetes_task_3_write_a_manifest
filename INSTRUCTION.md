# Deployment and Testing Instructions

## Applying Manifests

1. Using this command to go to the folder with manifests:
``
cd .\.infrastructure\
``

2. Deploy the ToDo application, apply all Kubernetes manifests using the following command:

```bash
kubectl apply -f namespace.yml
   ```
```bash
kubectl apply -f busybox.yml
```
```bash
kubectl apply -f todoapp-pod.yml
```

## Testing the Application

### Using Port-Forward

To get access to the ToDo application via port-forwarding, execute:

```bash
kubectl port-forward pod/todoapp 8081/8080 -n todoapp
```

### Using busyboxplus:curl Container to test the application

1. Finding the IP addresses of pods, you need to run the command:

```bash
kubectl get pods -n todoapp -o wide
```

After that, you need to go into the pod itself and execute a curl request

```bash
kubectl -n todoapp exec -it busybox -- sh
```

```
curl (ip address todoapp pod):8080
```