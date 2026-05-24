try:
    from PIL import Image
    print("Pillow OK - version:", Image.__version__ if hasattr(Image, '__version__') else "installed")
except ImportError as e:
    print("Pillow NO instalado:", e)
    import subprocess, sys
    subprocess.check_call([sys.executable, "-m", "pip", "install", "Pillow"])
    print("Pillow instalado. Corré el script de nuevo.")
