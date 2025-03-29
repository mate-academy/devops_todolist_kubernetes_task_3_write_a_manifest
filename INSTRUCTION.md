# Deployment and Testing Instructions

## Applying Manifests

First of all go to the folder with manifest using the comand:

1. `cd .\.infrastructure\`

Then to deploy the ToDo application, apply all Kubernetes manifests using the following command:

2. `kubectl apply -f namespace.yml`
3. `kubectl apply -f busybox.yml`
4. `kubectl apply -f todoapp-pod.yml`

## Testing the Application

### Using Port-Forward

To access the ToDo application via port-forwarding, execute:

`kubectl port-forward pod/todoapp 8081/8080 -n todoapp`

Now, you can test the application locally by opening a browser

### Using busyboxplus:curl Container

To Test the Application through pod(busyboxplus), first you need to find out their IP addresses, run the command

`kubeclt get pods -n todoapp -o wide`

After that, you need to go into the pod itself and execute a curl request

1. `kubectl -n todoapp exec -it busybox -- sh`
2. `curl (ip address todoapp pod):8080`
