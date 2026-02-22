# INSTRUCTION

## 1. Apply Kubernetes manifests

Create namespace:

`kubectl apply -f .infrastructure/namespace.yml`

Create busybox pod:

`kubectl apply -f .infrastructure/busybox.yml`

Create todo application pod:

`kubectl apply -f .infrastructure/todoapp-pod.yml`

Verify resources:

`kubectl get pods -n todoapp`

---

## 2. Test ToDo application using port-forward

Forward port from pod to local machine:

`kubectl port-forward pod/todoapp 8000:8000 -n todoapp`

Open in browser:

http://localhost:8000

Test health endpoints:

http://localhost:8000/api/health/live/
http://localhost:8000/api/health/ready/

---

## 3. Test application using busybox container

Enter busybox pod:

`kubectl exec -it busybox -n todoapp -- sh`

Get ToDo app pod IP (in another terminal):

`kubectl get pod todoapp -n todoapp -o wide`

Call application from inside cluster using the ToDo pod IP:

```bash
curl -i http://<TODOAPP_POD_IP>:8000/api/health/live/
curl -i http://<TODOAPP_POD_IP>:8000/api/health/ready/
```

Exit container:

`exit`
