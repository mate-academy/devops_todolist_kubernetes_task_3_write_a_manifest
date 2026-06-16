# Instructions for Deploying and Testing the ToDo App in Kubernetes

## 1. How to apply all manifests
First, you need to create the namespace, and then deploy the pods:
```bash
kubectl apply -f .infrastructure/namespace.yml
kubectl apply -f .infrastructure/