## To complete the task I did following steps

Troubleshooting of the problems met during solving are included

#### I. modified `src\api\views.py` and `src\api\urls.py`

#### II. created following manifests:

* `src\.infrastructure\busybox.yml`

  At first I tried to use `radial/busyboxplus:curl` image, but it appears to be deprecated and K8S declines any attempts to pull it

  So I used `curlimages/curl:latest` image, which follows same single purpose and has small size of 10MB

  Now we have logical issue with the manifest name and its content - But the task was to use `busybox` name for manifest
* `src\.infrastructure\todoapp-pod.yml`

  above mentioned manifest gave me following troubles:

  1. proper path to `liveness` & `readiness` endpoints

      after some explorations I found tht url path's mentioned in `src\api\urls.py` module refer to `localhost:8080/api/`, not `localhost:8080/`
      which was the point why I had troubles
  2. proper settings for Period / Delay

      even though I reveived proper respond on my requests (status codes: 200, with proper messages) - I had warning in events report:

      ```
      Events:
        Type     Reason     Age   From               Message
        ----     ------     ----  ----               -------
        Normal   Scheduled  21m   default-scheduler  Successfully assigned todoapp/todoapppod to docker-desktop
        Normal   Pulled     21m   kubelet            Container image "yegorv/todoapp:3.0.0" already present on machine
        Normal   Created    21m   kubelet            Created container todoappcontainer
        Normal   Started    21m   kubelet            Started container todoappcontainer
        Warning  Unhealthy  21m   kubelet            Readiness probe failed: HTTP probe failed with statuscode: 503
      ```

      rectifying this I found out tht kubectl makes only 3 attempts by default with described period - if during this attempts there was no success -> the warning will be displayed for the timebeing of Pod

      to rectidy it I simply increased period, but I suppose increasing number of attempts also applicable
* `src\.infrastructure\namespace.yml`

  Here everything is as per ReadMe

#### III. Built the todoapp image, retagged, pushed to repo

#### IV. Applied the manifests

1. opened the terminal in the `.infrustructure/`
2. run commands
    `kubectl apply -f namespace.yml`
    `kubectl apply -f busybox.yml`
    `kubectl apply -f todoapp-pod.yml`

#### V. Tested the port - forwarding

1. run the command `kubectl port-forward pod/todoapppod 8081:8080 -n todoapp`
2. accessed following path in browser: `127.0.0.1:8081/api/liveness/` 

    received status code 200
    and message: "Live"
3. accessed following path in browser: `127.0.0.1:8081/api/readiness/`

    received status code 503
    and message: "Not Ready"
4. after 1 minute wait accessed following path in browser: `127.0.0.1:8081/api/readiness/`

    received status code 200
    and message: "Ready"

#### VI. Tested inter-pod communication via curl request

1. got the `todoapppod` Pod ip with the following command

    `kubectl get pods -n todoapp -o wide`
2. accessed the shell of the container `curlcontainer` in Pod `curlpod` via following command

    `kubectl -n todoapp exec -it curlpod -- sh`
3. made following HTTP requests

    * `curl 10.1.0.15:8080/api/liveness/`

      with in-terminal reply message "Live"
    * `curl 10.1.0.15:8080/api/readiness/`

      with in-terminal appropriate timely reply messages "Not Ready" & "Ready"