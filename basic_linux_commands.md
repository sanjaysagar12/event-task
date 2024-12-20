
---

### **File and Directory Management**
1. **`ls`**  
   - Lists files and directories.  
   - Options:  
     - `ls -l`: Long format listing.  
     - `ls -a`: Includes hidden files.  

2. **`cd`**  
   - Changes directory.  
     - `cd /path/to/directory`: Move to a specific directory.  
     - `cd ..`: Move up one directory level.  
     - `cd ~`: Go to the home directory.  

3. **`pwd`**  
   - Prints the current working directory.  

4. **`mkdir`**  
   - Creates a new directory.  
     - `mkdir dirname`: Creates a directory named `dirname`.  

5. **`rm`**  
   - Removes files or directories.  
     - `rm filename`: Removes a file.  
     - `rm -r dirname`: Removes a directory and its contents.  

6. **`cp`**  
   - Copies files or directories.  
     - `cp source destination`: Copies a file.  
     - `cp -r source destination`: Copies a directory.  

7. **`mv`**  
   - Moves or renames files and directories.  
     - `mv oldname newname`: Renames a file.  
     - `mv file /new/location`: Moves a file to a new location.  

8. **`touch`**  
   - Creates an empty file.  
     - `touch filename`: Creates a file named `filename`.  

---

### **Viewing and Editing Files**
1. **`cat`**  
   - Displays file contents.  
     - `cat filename`: Outputs the contents of `filename`.  

2. **`nano`**  
   - Edits files in the terminal.  
     - `nano filename`: Opens the file in the `nano` text editor.  

3. **`vi` / `vim`**  
   - Edits files with advanced features.  
     - `vim filename`: Opens the file in the `vim` editor.  

---

### **File Permissions**
1. **`chmod`**  
   - Changes file permissions.  
     - `chmod 755 filename`: Sets read, write, execute permissions for the owner and read-execute for others.  

2. **`chown`**  
   - Changes file ownership.  
     - `chown user:group filename`: Sets ownership to a specific user and group.  

---

### **Process Management**


1. **`top`**  
   - Monitors system resources and processes in real-time.  

2. **`kill`**  
   - Terminates a process.  
     - `kill PID`: Kills the process with the given PID.  
---

### **Networking**
1. **`ping`**  
   - Checks network connectivity.  
     - `ping hostname`: Sends packets to a host.  

2. **`ifconfig`** / **`ip addr`**  
   - Displays network configuration.  

3. **`curl`**  
   - Transfers data from a URL.  
     - `curl http://example.com`: Fetches data from the given URL.  

4. **`wget`**  
   - Downloads files.  
     - `wget http://example.com/file.zip`: Downloads a file.  

---

### **Package Management (For Debian-based systems like Ubuntu)**
1. **`apt-get`**  
   - Manages packages.  
     - `sudo apt-get update`: Updates package list.  
     - `sudo apt-get install package`: Installs a package.  
     - `sudo apt-get remove package`: Removes a package.  

---

