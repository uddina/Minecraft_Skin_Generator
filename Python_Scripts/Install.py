import subprocess

subprocess.run(["pip", "install", "-r", "requirements.txt"], check=True)

print("Installed Requirements!")