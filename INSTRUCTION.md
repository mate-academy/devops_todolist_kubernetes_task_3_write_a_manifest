Use the following links below:

1. Link to the Docker Hub repository with an app image:
    https://hub.docker.com/repository/docker/nosenkoalena501/todoapp/general

2. All instructions:
    - how to apply all manifests:
        kubectl apply -f .infrastructure/namespace.yml
        kubectl apply -f .infrastructure/busybox.yml
        kubectl apply -f .infrastructure/todoapp-pod.yml

    - how to test ToDo application using the port-forward command:
        kubectl port-forward pod/todoapp 8081:8080 -n todoapp

    -  how to test the application using the busyboxplus:curl container
        kubectl get pods -o wide -n todoapp
        kubectl exec -n todoapp -it busyboxplus -- sh 
        curl 10.244.0.6
        curl http://10.244.0.6