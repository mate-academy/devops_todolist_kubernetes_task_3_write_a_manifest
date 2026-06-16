# Infrastructure Deployment Guide

This guide explains how to deploy the ToDo application and verify its status within the Kubernetes cluster.

## 1. Apply Manifests

Run the following commands sequentially to create the namespace, application pod, and test utility pod:

```bash
kubectl apply -f .infrastructure/namespace.yml
kubectl apply -f .infrastructure/todoapp-pod.yml
kubectl apply -f .infrastructure/busybox.yml