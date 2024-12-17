## 1. How to Apply All Manifests

To apply all manifests for your application, follow these steps:

1. Create a namespace for the application:
   ```bash
   kubectl apply -f .infrastructure/namespace.yml
   ```

2. Apply the manifest to create the `busybox` container (for testing):
   ```bash
   kubectl apply -f .infrastructure/busybox.yml
   ```

3. Apply the pod manifest for your ToDo application:
   ```bash
   kubectl apply -f .infrastructure/todoapp-pod.yml
   ```

   This manifest will create a pod with the container for the ToDo application using the `fredisson11/todoapp:3.0.0` image.

4. Verify that the pod has been created:
   ```bash
   kubectl get pods -n todoapp
   ```

   If the pod is running correctly, its status should be `Running`.

---

## 2. How to Test the ToDo Application Using `port-forward`

1. Use the `kubectl port-forward` command to access the service:
   ```bash
   kubectl port-forward pod/todoapp-pod 8080:8080 -n todoapp
   ```

2. Open your browser and go to:
   ```
   http://localhost:8080
   ```

   This will allow you to test the ToDo application interface locally, through port 8080.

---

## 3. How to Test the Application Using the `busyboxplus:curl` Container

1. Use the `busyboxplus:curl` container to check the availability of the `/readiness` and `/liveness` endpoints.

2. For **liveness** check:
   ```bash
   kubectl run -i --tty --rm busybox --image=ikulyk404/busyboxplus:curl --restart=Never -- curl http://todoapp-pod:8080/liveness
   ```

3. For **readiness** check:
   ```bash
   kubectl run -i --tty --rm busybox --image=ikulyk404/busyboxplus:curl --restart=Never -- curl http://todoapp-pod:8080/readiness
   ```

   A successful response for each of these requests should be:

   ```
   Ready
   ```

   If you get a different status or message, it means the pod is not ready or is not functioning properly.

---

## 4. How to Test Kubernetes Deployment

After applying all manifests and testing, verify the status of your pod:

1. Use the command to check the pod status:
   ```bash
   kubectl get pods -n todoapp
   ```

2. Check the pod logs:
   ```bash
   kubectl logs todoapp-pod -n todoapp
   ```

   The logs will help you understand if there are any issues with the application.