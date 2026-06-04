# TodoApp Kubernetes Deployment — Instructions

## Prerequisites

- `kubectl` installed and configured to connect to your cluster
- All manifests are located in the `.infrastructure/` folder

---

## 1. Apply All Manifests

Apply the manifests in the following order (namespace first, then pods):

```bash
# 1. Create the namespace
kubectl apply -f .infrastructure/namespace.yml

# 2. Start the busyboxplus helper pod
kubectl apply -f .infrastructure/busybox.yml

# 3. Deploy the TodoApp pod
kubectl apply -f .infrastructure/todoapp-pod.yml
```

Verify everything is running:

```bash
kubectl get all -n todoapp
```

---

## 2. Test the TodoApp Using `port-forward`

Forward a local port to the TodoApp pod running inside the cluster:

```bash
kubectl port-forward pod/todoapp -n todoapp 8080:8080
```

Then open a new terminal or browser and send a request:

```bash
curl http://localhost:8080
```

Or simply navigate to `http://localhost:8080` in your browser.

Press `Ctrl+C` to stop the port-forward when done.

---

## 3. Test the Application Using the `busyboxplus:curl` Container

Exec into the running `busybox` pod and use `curl` to reach the TodoApp by its Pod IP:

```bash
# Get the TodoApp pod's cluster IP
kubectl get pod todoapp -n todoapp -o wide

# Exec into the busybox pod
kubectl exec -it busybox -n todoapp -- sh

# Inside the container — replace <TODOAPP_POD_IP> with the IP from the step above
curl http://<TODOAPP_POD_IP>:8080
```

---

## 4. Check Probe Status

To verify that the readiness and liveness probes are working correctly:

```bash
kubectl describe pod todoapp -n todoapp
```

Look for the `Conditions` section (readiness) and `Events` section (liveness failures, if any).
