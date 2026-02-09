To go do directory which includes yaml files use command:
    cd ./.infrastructure

To apply namespace.yml use command:
    kubectl apply -f namespace.yml

To apply busybox.yml use command:
    kubectl apply -f busybox.yml

To apply todoapp-pod.yml use command:
    kubectl apply -f todoapp-pod.yml

To test ToDo application use command:
    kubectl port-forward pod/todoapp -n todoapp 8080:8080
    After this go to your browser and go to http://localhost:8080
    To stop port-forward use Ctrl + c

To test the application using the busyboxplus:curl container use command:
    To check IP of todoapp pod use command:
        kubectl get pods -n todoapp -o wide
    To go inside of busybox container use command:
        kubectl exec -it busybox -n todoapp -- sh
    While inside of container use command:
        curl <todoapp-pod-IP>:8080
