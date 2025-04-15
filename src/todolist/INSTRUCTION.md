# Instructions for Deploying and Testing the ToDo Application

## Applying Kubernetes Manifests

To deploy the ToDo application, use the following steps:

1. Make sure you have `kubectl` installed and configured to interact with your Kubernetes cluster.
2. Navigate to the folder containing the Kubernetes manifests.
3. Apply all the manifests using the following command:

   ```bash
   kubectl apply -f <manifest-directory>/
   ```

   Replace `<manifest-directory>` with the path to the directory where the Kubernetes manifests are located.

   Example:
   ```bash
   kubectl apply -f manifests/
   ```

4. Verify the resources have been created successfully:

   ```bash
   kubectl get all
   ```

---

## Testing the ToDo Application

### Option 1: Using Port-Forward Command

To test the ToDo application locally by forwarding the service port to your machine:

1. Identify the service name associated with the application:

   ```bash
   kubectl get svc
   ```

2. Use the `kubectl port-forward` command to forward the service port. For example, if the service name is
   `todo-service` and it exposes port `8080`:

   ```bash
   kubectl port-forward svc/todo-service 8080:8080
   ```

3. Open your browser or use a tool like `curl` to make requests to the application locally:

   ```bash
   curl http://localhost:8080
   ```

---

### Option 2: Testing Using a `busyboxplus:curl` Container

If you prefer testing from within the cluster, you can use a `busyboxplus:curl` pod to send requests:

1. Create a temporary pod running `busyboxplus:curl`:

   ```bash
   kubectl run curl-pod --image=radial/busyboxplus:curl -it --rm
   ```

2. Once inside the pod, you can make requests to the ToDo application service. Replace `<service-name>` with the name of
   the application's service and `<port>` with its port:

   ```sh
   curl http://<service-name>:<port>
   ```

   Example:
   ```sh
   curl http://todo-service:8080
   ```

3. Exit the pod when you are done testing by typing `exit`.

---

By following the steps above, you can apply the configurations and test the ToDo application using multiple methods.