# Todoapp

## Setup

1. Clone the repository.
2. Ensure you have Docker, Kubernetes installed and running.
    ```

## Applying Kubernetes Manifests

1. Make sure you have kubectl configured to your Kubernetes cluster.
2. Apply the Kubernetes manifests by running the following command in the terminal:
    ```bash
    kubectl apply -f infrastructure/

## Testing

### Using Port Forwarding

1. Forward the port from the todoapp pod to your local machine:
    ```bash
    kubectl port-forward pod/todoapp 8081:8080 -n todoapp
    ```
2. Open your browser and visit http://localhost:8081 to access the Todoapp.

### Using Busybox Container

Before proceeding, obtain the IP address of the busybox pod by running:

```bash
    kubectl get pods -n todoapp -o wide
```

1. Access the shell of the busybox pod:
    ```bash
    kubectl exec -it pod/busybox -- sh
    ```
2. Test the connection to the ToDo app:
    ```bash
    curl <busybox_pod_ip>:8080
    ```
Replace <busybox_pod_ip> with the actual IP address obtained from the previous command.
