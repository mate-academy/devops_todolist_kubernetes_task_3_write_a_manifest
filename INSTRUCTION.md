# ToDo Application Deployment Instructions

All Kubernetes manifests are located under the `.infrastructure` folder at the root of this repository.

## 1. Apply all manifests
To create the namespace and deploy the pods to your cluster run the following commands:

```bash
kubectl apply -f .infrastructure/namespace.yml
kubectl apply -f .infrastructure/todoapp-pod.yml
kubectl apply -f .infrastructure/busybox.yml