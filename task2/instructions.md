### **Task: Write a Dockerfile for a Node.js Application**

In this task, you will write a `Dockerfile` to containerize a Node.js application.

---

### **Instructions:**

1. **Prepare the Application**:
   - Write a Node.js script (`app.js`) to create a simple HTTP server.
   - Create a `package.json` file to define the project and dependencies.

2. **Write the Dockerfile**:
   - Use the official Node.js image as the base image.
   - Set up a working directory inside the container.
   - Copy necessary application files (`package.json` and `app.js`) into the container.
   - Install the dependencies inside the container.
   - Expose the port `3000` on which your application will run.
   - Set the default command to start the application.

3. **Build the Docker Image**:
   - Use the `docker build` command to create an image using your `Dockerfile`.

4. **Run the Docker Container**:
   - Use the `docker run` command to start the container.
   - Map the container's port `3000` to any available port on your server by using the `-p` option. For example:
     ```bash
     docker run -d -p <host-port>:3000 --name node-container <image-name>
     ```
     Replace `<host-port>` with an available port on your server (e.g., `8080`) and `<image-name>` with the name of your Docker image.

5. **Test the Application**:
   - Open a browser or use a tool like `curl` to verify the application is running at:
     ```
     http://<server-ip>:<host-port>
     ```
     Replace `<server-ip>` with your server's IP address and `<host-port>` with the port you mapped.

6. **Clean Up (Optional)**:
   - Stop and remove the container when you're done:
     ```bash
     docker stop node-container
     docker rm node-container
     ```
   - Optionally, remove the Docker image:
     ```bash
     docker rmi <image-name>
     ```

---

Good luck! Let me know if you need further assistance.