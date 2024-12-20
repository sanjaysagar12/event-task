### **Docker Container Management**
1. **`docker run`**  
   - Runs a container from an image.  
     - `docker run -d --name container_name image_name`: Runs a container in detached mode with a custom name.  
     - `docker run -it image_name`: Runs a container interactively with a terminal.  

2. **`docker ps`**  
   - Lists running containers.  
     - `docker ps -a`: Lists all containers, including stopped ones.  

3. **`docker stop`**  
   - Stops a running container.  
     - `docker stop container_name`: Stops the specified container.  

4. **`docker start`**  
   - Starts a stopped container.  
     - `docker start container_name`: Starts the specified container.  

5. **`docker restart`**  
   - Restarts a container.  
     - `docker restart container_name`: Restarts the specified container.  

6. **`docker rm`**  
   - Removes a container.  
     - `docker rm container_name`: Removes the specified container.  
     - `docker rm -f container_name`: Forces the removal of a running container.  

7. **`docker exec`**  
   - Executes a command inside a running container.  
     - `docker exec -it container_name bash`: Opens a bash shell inside the running container.  

---

### **Docker Image Management**
1. **`docker build`**  
   - Builds an image from a Dockerfile.  
     - `docker build -t image_name .`: Builds an image from the Dockerfile in the current directory.  

2. **`docker images`**  
   - Lists all available images.  
     - `docker images`: Shows a list of all images on your system.  

3. **`docker pull`**  
   - Pulls an image from a Docker registry.  
     - `docker pull image_name`: Pulls the specified image from Docker Hub or another registry.  

4. **`docker rmi`**  
   - Removes an image.  
     - `docker rmi image_name`: Removes the specified image.  
     - `docker rmi -f image_name`: Forcefully removes an image.  

5. **`docker tag`**  
   - Tags an image with a new name.  
     - `docker tag image_name new_image_name`: Tags an existing image with a new name or version.  

---

### **Docker Network Management**
1. **`docker network ls`**  
   - Lists all Docker networks.  

2. **`docker network create`**  
   - Creates a new Docker network.  
     - `docker network create network_name`: Creates a new network.  

3. **`docker network inspect`**  
   - Inspects a Docker network.  
     - `docker network inspect network_name`: Displays detailed information about the specified network.  

---

### **Docker Volume Management**
1. **`docker volume ls`**  
   - Lists all Docker volumes.  

2. **`docker volume create`**  
   - Creates a new volume.  
     - `docker volume create volume_name`: Creates a new volume.  

3. **`docker volume inspect`**  
   - Inspects a Docker volume.  
     - `docker volume inspect volume_name`: Shows detailed information about a volume.  

4. **`docker volume rm`**  
   - Removes a volume.  
     - `docker volume rm volume_name`: Removes the specified volume.  

---

### **Docker Compose (For Multi-Container Applications)**
1. **`docker-compose up`**  
   - Starts up containers defined in a `docker-compose.yml` file.  
     - `docker-compose up`: Starts the services in the background.  
     - `docker-compose up -d`: Starts the services in detached mode.  

2. **`docker-compose down`**  
   - Stops and removes containers defined in a `docker-compose.yml` file.  
     - `docker-compose down`: Stops and removes all services.  

3. **`docker-compose logs`**  
   - Shows logs from containers managed by Docker Compose.  
     - `docker-compose logs`: Displays logs for all containers.  

4. **`docker-compose ps`**  
   - Lists containers managed by Docker Compose.  
     - `docker-compose ps`: Shows the status of containers.  

---

### **Docker System Management**
1. **`docker system prune`**  
   - Cleans up unused containers, images, volumes, and networks.  
     - `docker system prune`: Removes unused resources.  

2. **`docker info`**  
   - Displays Docker system information, such as number of containers, images, and system details.  

3. **`docker version`**  
   - Displays the version of Docker installed.  

