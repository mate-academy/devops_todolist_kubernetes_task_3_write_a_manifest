1. How to apply Namespace manifest.

Go to devops_todolist_kubernetes_task_3_write_a_manifest\.infrastructure directory:

    cd \.infrastructure

Create Namespace from namespace.yml manifest:

    kubectl apply -f namespace.yml


2. How to apply Busyboxplus manifest.

Go to devops_todolist_kubernetes_task_3_write_a_manifest\.infrastructure directory:

    cd \.infrastructure

Create Busyboxplus pod from busybox.yml manifest:

    kubectl apply -f busybox.yml


3. How to apply Todoapp manifest.

Go to devops_todolist_kubernetes_task_3_write_a_manifest\.infrastructure directory:

    cd \.infrastructure

Create Todoapp pod from todoapp-pod.yml manifest:

    kubectl apply -f todoapp-pod.yml


4. How to test ToDo application using the `port-forward` command.

    kubectl port-forward pod/todoapp-pod 8081:8080 -n todoapp


5. How to test the application using the `busyboxplus:curl` container.

Use dynamic IP retrieval in powershell terminal for test the app:

    kubectl exec -n todoapp busyboxplus -- curl "$(kubectl get pods -n todoapp -o jsonpath='{.items[?(@.metadata.name==\"todoapp-pod\")].status.podIP}'):8080"
