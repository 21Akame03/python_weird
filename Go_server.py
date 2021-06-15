import subprocess
import time
import typer
import os

app = typer.Typer(name="Goserver", add_completion=False, help="Golang Dev Server CLI Monitor (GDSCM)")
     
def checkServerStatus():
    proc = subprocess.Popen(["ps", "-a"], stdout=subprocess.PIPE)
    return proc.communicate()

def checkPath(path):
    global abspath
    abspath = os.path.abspath(path)
    if not os.path.exists(abspath):
        print(f"The path {path} does not exist")
        raise typer.Exit(code=1)

def runServer() :
    print (f"Server module dir: {abspath}")
    os.chdir(abspath)
    os.system(f"go run {abspath}")
    

@app.command()
def Start(path: str = typer.Argument(..., help="Path of the module", callback = checkPath)):
    """ Starts a dev server of Golang at provided path"""

    restart_counter = 0
    runServer()

    while True and restart_counter < 4:
        out, err = checkServerStatus()

        if out and "go" in str(out):
            print("\033[1;32;40m ######## -----> Server running ")

        else:
            print(f"\033[1;31;40m Server is offline: \n   {err}")
            print(f"\n\033[1;34;40m {runServer()} \033")
            restart_counter += 1
        
        time.sleep(5)

@app.command()
def getPackages():
    """ Use go get to download packages"""
    print("get")
   
if __name__ == "__main__":
    app()