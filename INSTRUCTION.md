## Deployment instruction forTodoapp.

### 1. Docker image Build and push.
    - go to project folder with Dockerfile
    - build docker image:
        docker build . -t timnord1993/todoapp:3.0.0
    - login in docker hub:
        docker login
    - push the image to docker hub:
        docker push timnord1993/todoapp:3.0.0
### 2. K8s namespaces creating.
    - K8s namespaces creating:
        kubectl apply -f .infrastructure/namespace.yml
    - check if namespace was created:
        kubectl get ns
### 3. Deployment of test-pod.
    - Deployment of test-pod:
        kubectl apply -f .infrastructure/busybox.yml
    - check if test pod was created:
        kubectl get pods -n todoapp
### 4. Deployment of app pod.
    - Deployment of app pod:
        kubectl apply -f .infrastructure/todoapp-pod.yml
### 5. Todo app test.
    - port-forwarding pod to local machine:
        kubectl port-forward pod/todoapp 8081:8080 -n todoapp
    - via curl on host:
        curl http://localhost:8081/api/liveness/
        curl http://localhost:8081/api/readiness/
    
    - to exit from busybox:
        exit
