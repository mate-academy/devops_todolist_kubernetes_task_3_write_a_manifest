# Instructions

## Prerequisites

Before applying the Kubernetes manifests, make sure that the following tools are installed and configured:

Docker

kubectl

kind or another running Kubernetes cluster

A Docker Hub account

Access to the 

[alexey211204/todoapp:3.0.0](https://hub.docker.com/repository/docker/alexey211204/todoapp/general) and [ikulyk404/busyboxplus:curl](https://hub.docker.com/r/ikulyk404/busyboxplus) images 

Verify that the Kubernetes cluster is running and that kubectl can connect to it:

kubectl cluster-info

You can also verify the cluster nodes:

kubectl get nodes

## Run the application

To run application use following commands:

To set up namespace
```bash
kubectl apply -f .infrastructure/namespace.yml
```

It creates or updates the ToDo application Pod in the todoapp namespace based on the manifest.
```bash
kubectl apply -f .infrastructure/todoapp-pod.yml
```
It creates or updates the busybox application Pod in the todoapp namespace based on the manifest.
```bash
kubectl apply -f .infrastructure/busybox.yml
```

# Cheaks

## To use your browser for cheacking if the TODOAPP is working firstly you need to run following command:

```bash
kubectl port-forward pod/todoapp 8081:8080 -n todoapp
```
then open [this page](http://127.0.0.1:8081/)

## To use busybox you could run this command:

```bash
kubectl exec -it -n todoapp busybox -- sh  
```
then you can to use one of the following commands:

```bash
curl http://<TODOAPP_POD_IP>:8080/
``` 
if everything is OK you will see "Ready"
```bash
curl http://<TODOAPP_POD_IP>:8080/api/readiness/
``` 

if everything is OK you will see "Alive"
```bash
curl http://<TODOAPP_POD_IP>:8080/api/liveness/
``` 