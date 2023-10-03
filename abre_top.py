import subprocess
import time

# resultado top
archivo_resultado = "resultado_top_main.txt"

# comando
comando_top = f"top >> {archivo_resultado}"

while True:
    try:

        proceso = subprocess.Popen(
            ['gnome-terminal', '--', 'bash', '-c', comando_top])

        time.sleep(80)

        proceso.terminate()

    except KeyboardInterrupt:

        break
