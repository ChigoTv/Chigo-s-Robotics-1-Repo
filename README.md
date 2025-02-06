# Chigo-s-Robotics-1-Repo
# Robotics 1 (IE 482) Repository

Hello to whoever may be reading this file!  

My name is Chigozie Eke, and this is my **Robotics 1 (IE 482)** repository.   

Stay tuned for project updates, code, and learning material related to robotics!  

# Running Python on Windows PowerShell

This guide will help you (and me) navigate using Python in **Windows PowerShell**, including setting up your environment, troubleshooting possible errors, and installing required packages when necessary.

---

##  **Basic PowerShell Navigation**
PowerShell operates with a directory structure similar to a command-line interface (CLI), which is a text-based way to interact with a computer's operating system. CLIs are used to run programs, manage files, and perform other tasks. Here are some essential commands that I found helpful while working through this (With the massive amount of help from Angelo and Professor Murray):

```powershell
# Change directory (navigate to a folder, in this case "Downloads")
cd Downloads

# List files in the current directory
ls

**# If you try to change into a directory that does not exist, you will see an error:
**
cd code
# cd : Cannot find path 'C:\Users\Chigo\Downloads\code' because it does not exist.

python --version
Python 3.13.1

ModuleNotFoundError: No module named 'numpy'

pip install numpy --user
---------------------------------------
# Running Python on Windows PowerShell

This guide will help you navigate using Python in **Windows PowerShell**, including setting up your environment, troubleshooting errors, and installing required packages.

---

## **Running Python in PowerShell**
### **1 Check if Python is Installed**
Run the following command to verify Python installation:

```powershell
python --version
```
If Python is not installed, use this command:
```
pip install Python 3.13.1
```

If Python is installed, you will see an output like:
```
Python 3.13.1
```

If you see an error like `python3: The system cannot find the path specified`, try using `python` instead of `python3`.

### **2 Running Python**
To start the Python interpreter, use:

```powershell
python
```

You will enter the Python shell:
```
Python 3.13.1 (tags/v3.13.1:0671451, Dec 3 2024) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
```
Exit the Python shell by typing:
```python
exit()
```

---

##  **Common Errors & Fixes**
### **1 ModuleNotFoundError: No module named 'numpy'**
If you get an error like this:
```python
ModuleNotFoundError: No module named 'numpy'
```
You need to install the missing package:
```powershell
pip install numpy --user
```

### **2 AttributeError: module 'cv2' has no attribute 'TrackerCSRT_create'**
This error suggests that OpenCV may be outdated or incorrectly installed. Reinstall it with:

```powershell
pip uninstall opencv-python
pip install opencv-contrib-python --user
```

### **3 Access Denied When Installing a Package**
If you see:
```
ERROR: Could not install packages due to an OSError: [WinError 5] Access is denied
```
Try installing with the `--user` flag:

```powershell
pip install package-name --user
```

### **4 KeyError: 'HOME'**
If you see:
```python
KeyError: 'HOME'
```
Windows does not set a `HOME` environment variable by default. Use `USERPROFILE` instead:

```python
import os
HOME_DIRECTORY = os.environ.get('USERPROFILE', 'C:\\Users\\YourUsername')
```

##  **Getting Your IP Address**
To retrieve your **local** IP address, run:
```powershell
Get-NetIPAddress -AddressFamily IPv4 | Select-Object IPAddress
```

For **public** IP:
```powershell
Invoke-RestMethod -Uri "https://api64.ipify.org?format=text"
```

##  **Updating Localhost Configuration**
1. Open PowerShell as **Administrator**.
2. Run:
   ```powershell
   notepad C:\Windows\System32\drivers\etc\hosts
   ```
3. Add your IP:
   ```
   192.168.1.100  localhost
   ```
---

Now you're ready to run Python smoothly on **Windows PowerShell**! 

