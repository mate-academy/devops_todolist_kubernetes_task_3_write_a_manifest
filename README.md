# Django ToDo list

1. Create namespace

```bash
kubectl apply -f ./.infrastructure/namespace.yml
```

2. Create todoapp api pod

```bash
kubectl apply -f ./.infrastructure/todoapp-pod.yml
```

3. Create busybox api pod

```bash
kubectl apply -f ./.infrastructure/busybox.yml
```

4. Port forwarding

```bash
kubectl port-forward pod/todoapp 8080:8080 -n todoapp
```

5. Open http://localhost:8080

6. Test with busybox

Get ip of todoapp pod

```bash
kubectl get pods -n todoapp -o wide
```

For example id = '10.1.0.16'
Open busybox shell

```bash
kubectl -n todoapp exec -it busybox -- sh
```

Do curl request to 10.1.0.16:8000

```bash
curl 10.1.0.16:8080
```
