# Instructions

## Applying manifests

### 1. Creating namespace

```bash
kubectl apply -f .infrastructure/namespace.yml
```

### 2. Create busybox pod

```bash
kubectl apply -f .infrastructure/busybox.yml
```

### 3. Create todoapp pod

```bash
kubectl apply -f .infrastructure/todoapp-pod.yml
```

## Test using port-forwarding

### 1. Verify that pods are running and ready, 

```bash
kubectl get pods -n todoapp
```

### 2. Use port-forwarding

```bash
 kubectl port-forward pod/todoapp 8000:8000 -n todoapp
```

### 3. Open [http://localhost:8000](http://localhost:8000) at browser


## Test using curl

### 1. Verify that pods are running and ready, check todoapp pod IP

```bash
kubectl get pods -n todoapp -o wide
```

### 2. Connect to the busybox container and open an interactive sh shell

```bash
kubectl exec -it busybox -n todoapp -- sh
```

### 3. Run curl command using the todoapp IP from step 1

```bash
curl <todoapp_ip>:8000/api/healthy
```

```bash
curl <todoapp_ip>:8000/api/ready
```