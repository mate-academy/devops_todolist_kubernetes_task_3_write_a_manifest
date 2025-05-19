# Instructions for Deploying and Testing the ToDo Application

## Applying the Manifests

1. Ensure you have `kubectl` installed and configured to access your Kubernetes cluster.
2. Apply the manifests in the following order:

```bash
kubectl apply -f .infrastructure/namespace.yml
kubectl apply -f .infrastructure/busybox.yml
kubectl apply -f .infrastructure/todoapp-pod.yml