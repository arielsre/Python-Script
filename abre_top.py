import subprocess
import time

# Definir el nombre del archivo para guardar el resultado del ping
archivo_resultado = "resultado_ping.txt"

# Comando para realizar el ping durante 1 minuto
comando_ping = f"top > {archivo_resultado}"

while True:
    try:
        # Abrir una nueva terminal y ejecutar el comando de ping
        proceso = subprocess.Popen(
            ['gnome-terminal', '--', 'bash', '-c', comando_ping])

        # Esperar 80 segundos
        time.sleep(80)  # Esperar 80 segundos

        # Terminar el proceso (cerrar la terminal)
        proceso.terminate()  # O puedes usar proceso.kill() para forzar la terminación

    except KeyboardInterrupt:
        # Si se presiona Ctrl+C, detener el bucle y salir del script
        break
