# ToDo Application - Kubernetes Deployment Guide

This guide provides instructions on how to deploy the ToDo application and verify its functionality within a Kubernetes cluster.

## 1. How to apply all manifests
All manifests are located in the `.infrastructure` folder. You must apply them in the following order to ensure the namespace is created before the resources:

1. **Create the Namespace:**
   ```bash
   kubectl apply -f .infrastructure/namespace.yml

2. Deploy the BusyBox pod: (This pod uses the ikulyk404/busyboxplus:curl image for testing):
 **kubectl apply -f .infrastructure/busybox.yml**

3. Deploy the ToDo application pod: (This pod uses the olegglv/todoapp:3.0.0 image with configured Liveness and Readiness probes)
 **kubectl apply -f .infrastructure/todoapp-pod.yml**

4. How to test using port-forward
The port-forward command allows you to access the application from your local machine's browser without a Public IP:

**Start port-forwarding:
kubectl port-forward pod/todoapp 8081:8080 -n todoapp**

5. How to test using the busyboxplus:curl container
Since you have a dedicated busybox pod running in the cluster, you can use it to test internal connectivity:
Enter the busybox container:
**kubectl exec -it busybox -n todoapp -- sh**
Run curl commands inside the cluster:
curl <ip todoapp>
Exit the container: exit