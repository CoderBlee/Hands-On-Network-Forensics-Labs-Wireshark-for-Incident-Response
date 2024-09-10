import volatility
from volatility.plugins import taskmods

# Example function to list processes from memory image
def list_processes(memory_image):
    config = volatility.conf.ConfObject()
    config.PROFILE = "WinXPSP2x86"
    config.LOCATION = f"file://{memory_image}"
    session = volatility.framework.contexts.Context(config)
    pslist = taskmods.PsList(session)
    for process in pslist.pslist():
        print(f"Process: {process.ImageFileName}")
