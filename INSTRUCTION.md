# ToDo app in Kubernetes

## 1. Build and push the image

```bash
docker build -t kkurama/todoapp:3.0.0 .
docker push kkurama/todoapp:3.0.0
```

## 2. Apply the manifests

```bash
kubectl apply -f .infrastructure/namespace.yml
kubectl apply -f .infrastructure/todoapp-pod.yml
kubectl apply -f .infrastructure/busybox.yml
```

Check that both pods are `Running` and `1/1` ready:

```bash
kubectl get pods -n todoapp -o wide
```

## 3. Test with port-forward

```bash
kubectl port-forward pod/todoapp 8080:8080 -n todoapp
```

Open in a browser or in another terminal:

```bash
curl http://localhost:8080/api/health/
curl http://localhost:8080/api/ready/
```

Both should return `OK`. The app itself is available at http://localhost:8080.

## 4. Test from the busybox pod

Get the IP of the ToDo pod:

```bash
kubectl get pod todoapp -n todoapp -o wide
```

Run curl from the busybox container (replace `<TODOAPP_POD_IP>` with the IP from the previous command):

```bash
kubectl exec -it busybox -n todoapp -- curl http://<TODOAPP_POD_IP>:8080/api/health/
kubectl exec -it busybox -n todoapp -- curl http://<TODOAPP_POD_IP>:8080/api/ready/
```

Both should return `OK`.