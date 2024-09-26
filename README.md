## DEMO APPS
- Applications in this repository are mostly used for testing docker, kubernetes, helm and argocd  
- They don't do much and don't necessarily follow best practices

### Building images
- Docker images built for applications is used by local kubernetes cluster (e.g. docker-desktop)  
- To build an container image
  ```
  docker build -t demo-app-one:0.1.0 ./demo-app-one
  ```
- To test the container
  ```
  docker run -d -p 5000:5000 demo-app-one:0.1.0 
  ```
  Navigate to http://localhost:5000/ from browser

### demo-app-one
- Python/Flask app for kubernetes  
- Reads configuration from ./config/demo-app-one  
  This file will be created by a configmap and a volume mount in kubernetes cluster
