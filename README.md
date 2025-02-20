# Overwatch eSports Watcher
Script que automatiza el ponerse a ver una transmisión de la ow_esports en Twitch.  

El script principal es `ow_esports-watcher.py`.  

## Features
 - Abre un navegador y accede a una transmisión.  
 - Reclama los botines por mirar durante 15 minutos.  
 - Notifica cuando comienza una predicción.  
 - Apaga el equipo cuando una transmisión finaliza.  
 - Realiza notificaciones mediante Pushover (Inicio, predicción y final).  
  
## Setup
 1. Descarga e instala las librerias Python necesarias a través de `requirements.txt`:  
        `pip install -r requirements.txt`  
 2. Luego toca modificar `config.json` dentro de la carpeta `/OWEW`:  
        `title`: Nombre para identificar la ventana. (Ni símbolos, ni números)  
        `configuration.PUSHOVER`: Credenciales de [Pushover: USER y APP TOKEN](https://pushover.net/api), junto con el dispositivo que recibirá notificación.  
        `configuration.MONITOR`: Configuración de pantalla y áreas.  
        `configuration.MONITOR.SCREEN`: Pantalla a utilizar. (Configuración de pantalla)  
        `configuration.MONITOR.AREA`: Definiciones de áreas para cada pantalla. (Hay dos configuraciónes, para dos monitores uno al lado del otro. Pero puedes agregar más)  
        `configuration.SHUTDOWN_TIME`: Tiempo de espera para el apagado al final de la transmision. (300s=5minutos por defecto)  
        `configuration.WAIT_TIME`: Tiempo de espera entre verificaciones de estado. (120s=2minutos por defecto)  
        `configuration.CHANNEL_NAME`: Dirección del canal a ir.  
        `configuration.webbrowser`: Para generar la instancia del navegador.  
        `configuration.webbrowser.binary`: Ruta del ejecutable del navegador preferido.  
        `configuration.webbrowser.arguments`: Línea de argumentos para ejecutar el binario. (Actualmente, inicia con el Perfil 1 seleccionado)  

### Configuración de áreas para `config.json`
Esto es tedioso, pues depende para cada usuario. Lo importante es saber las ubicaciones que queremos monitorear.  
Puedes obtener las coordenadas X, Y de tu cursor con el siguiente script de PowerShell:
```powershell
[console]::WindowWidth=20; [console]::WindowHeight=5; [console]::BufferWidth=[console]::WindowWidth;
Add-Type -AssemblyName System.Windows.Forms
while (1) {
    $X = [System.Windows.Forms.Cursor]::Position.X
    $Y = [System.Windows.Forms.Cursor]::Position.Y

    Write-Host -NoNewline "`rX: $X | Y: $Y"
}
```
> Si usas Vivaldi, en un monitor FULL HD (1920x1080), sin escalado (100%), la página de Twitch tiene el Chat y el panel izquierdo activo y el taskbar no se oculta automáticamente: Es posible que la configuración por defecto de las áreas funcione correctamente. (Un ejemplo en la siguiente imagen)  

Para esta tarea, te adjunto un pantallazo que explica todo.  
![Pantallazo](https://dev.crizacio.com/docs/assets/images/OWES-main-screenshot.png)  
  
### Opciones
El script acepta varios argumentos de entrada para una personalizacion o para controlar el comportamiento.  

 - `-w CANAL` o `--watch CANAL`: Indica el nombre del `CANAL` de Twitch a ver. Defecto: `ow_esports`. Ejemplo: `-w playoverwatch`
 - `-s PANTALLA` o `--screen PANTALLA`: Indica el índice de la `PANTALLA` a utilizar. Defecto: `0` (pantalla principal). Ejemplo: `-s 1` (pantalla secundaria)
 - `-c TIEMPO` o `--check TIEMPO`: Indica el tiempo de intervalo antes de verificar los bonuses, predicciones o finalización. Defecto `120` (segundos). Ejemplo `-c 300` (300 segundos o 5 minutos)
 - `-a` o `--awake`: Si se indica, al finalizar la transmisión el script se detendrá sin suspender el equipo. Actualmente, el equipo entrará en modo suspensión después de 5 minutos.
 - `-n` o `--next`: Si se indica, se omitirá el setup del navegador.


## Como funciona
gg
