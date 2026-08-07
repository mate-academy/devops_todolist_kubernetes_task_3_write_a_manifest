# ToDo Application Deployment Instructions

## 1. Apply all manifests
To create the namespace and deploy the pods to your cluster run the following commands:

```bash
kubectl apply -f .infrastructure/namespace.yml
kubectl apply -f .infrastructure/todoapp-pod.yml
kubectl apply -f .infrastructure/busybox.yml