# 1) How to apply all manifests:

    kubectl apply -f .infrastructure/namespace.yml
    kubectl apply -f .infrastructure/busybox.yml
    kubectl apply -f .infrastructure/todoapp-pod.yml

After created pods you can check all your pods with command:

    kubectl get pods -n todoapp

# 2) How to test ToDo application:

    kubectl port-forward pod/todoapp-pod 8000:8000 -n todoapp

Open your browser and check:

    http://localhost:8000

You can also check livenessProbe and readinessProbe:
    
    http://localhost:8000/api/liveness
    http://localhost:8000/api/ready

# 3)  How to test the application using the busyboxplus:curl container:

    kubectl exec -it busybox -n todoapp -- sh

After you will be inside container busybox, here you can test your endpoints:

    curl http://todoapp-pod:8000
    curl http://todoapp-pod:8000/api/liveness
    curl http://todoapp-pod:8000/api/ready

After test, you can exit from container:

    exit 