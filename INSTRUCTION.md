# ToDo App — Kubernetes Deployment Instructions

## Prerequisites
- `kubectl` installed and configured
- Docker image `dmytro0908/todoapp:3.0.0` pushed to Docker Hub

## Apply manifests

Run the following commands to deploy the application:

```bash
kubectl apply -f .infrastructure/namespace.yml
kubectl apply -f .infrastructure/busybox.yml
kubectl apply -f .infrastructure/todoapp-pod.yml

**Check the status of the pods:

bash
kubectl get pods -n todoapp
Test ToDo app via port-forward
To test the application on your local machine, use the kubectl port-forward command. This maps your local port 8000 to the pod's port 8000:

bash
kubectl port-forward pod/todoapp 8000:8000 -n todoapp
After running the command, open your web browser and navigate to:
http://localhost:8000

You can also test the readiness and liveness endpoints using curl in another terminal:

bash
curl http://localhost:8000/api/healthz/readiness/
curl http://localhost:8000/api/healthz/liveness/
Test the app using busyboxplus:curl container
To test the application from inside the cluster using the busybox container, follow these steps:

Exec into the busybox container:

bash
kubectl exec -it busybox -n todoapp -- /bin/sh
Inside the container, use curl to test the ToDo application.
(Note: Since there is no Kubernetes Service defined, you can reach the app using the pod's IP address. To find the IP, run kubectl get pod todoapp -n todoapp -o wide in another terminal and look at the IP column. Replace <POD_IP> with that IP.)

bash
curl http://<POD_IP>:8000/api/healthz/readiness/
curl http://<POD_IP>:8000/api/healthz/liveness/
If successful, you will see ready and alive as the output.

Cleanup
bash
kubectl delete -f .infrastructure/todoapp-pod.yml
kubectl delete -f .infrastructure/busybox.yml
kubectl delete -f .infrastructure/namespace.yml