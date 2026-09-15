# Instructions for Deploying and Testing ToDo App in Kubernetes

This guide describes how to apply the Kubernetes manifests for the ToDo application and how to test its functionality using `port-forward` and a `busyboxplus:curl` container.

## 1. Apply All Manifests

Ensure your Kubernetes cluster (e.g., Minikube) is running, then apply the manifests located under the `.infrastructure` folder in the correct order:

1. **Create the Namespace:**
   ```bash
   kubectl apply -f .infrastructure/namespace.yml

Deploy the ToDo Application Pod:


kubectl apply -f .infrastructure/todoapp-pod.yml
Deploy the Busybox Container (for testing):


kubectl apply -f .infrastructure/busybox.yml

2. Test ToDo Application Using port-forward
To access the ToDo application directly from your local machine via port forwarding:

Forward local port 8000 to port 8000 on the todapp pod within the todoapp namespace:


kubectl port-forward pod/todapp -n todoapp 8000:8000
Open your browser or use curl in another terminal window to access the landing page or API:

Landing page: http://localhost:8000/

API: http://localhost:8000/api/

Health Check: http://localhost:8000/api/health/

Readiness Check: http://localhost:8000/api/readiness/

3. Test the Application Using busyboxplus:curl
To test the application from inside the cluster using

Open an interactive shell inside the running busybox pod:

kubectl exec -it busybox -n todoapp -- sh
Once inside the container, use curl to send requests to the ToDo application pod (using its service name or internal IP, or querying localhost if testing directly):

curl http://todapp:8000/api/health/
curl http://todapp:8000/api/readiness/
Exit the container shell by typing:

exit