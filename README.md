# Overwatch eSports Watcher
Script que automatiza el ponerse a ver una transmisión de la ow_esports en Twitch.  
  
#### Documentación
https://dev.crizacio.com/docs/Overwatch-eSports-Watcher-Bot  
  
### Features
 - Abre un navegador y accede a una transmisión.  
 - Reclama los botines por mirar durante 15 minutos.  
 - Notifica cuando comienza una predicción.  
 - Apaga el equipo cuando una transmisión finaliza.  
 - Realiza notificaciones mediante Pushover (Inicio, predicción y final).  
  
## Uso
 1. Descarga e instala las librerias Python necesarias a través de `requirements.txt`:  
        `pip install -r requirements.txt`  
 2. Luego toca modificar `config.json` dentro de la carpeta `/OWEW`:  
        `title`: Nombre para identificar la ventana. (Ni símbolos, ni números)  
        `configuration.PUSHOVER`: Credenciales de Pushover: USER y APP TOKEN, junto con el dispositivo que recibirá notificación.  
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
> Es posible (99% seguro) que mi configuración de área Bonus SI te funcione.  
> Es posible (99% seguro) que mi configuración de área Gambles SI te funcione.  
> Es posible (99% seguro) que mi configuración de área Finisher NO te funcione.  
  
Para esta tarea, te adjunto un pantallazo que explica todo.  
![Pantallazo](https://dev.crizacio.com/docs/assets/images/OWES-main-screenshot.png)  
  
## Como funciona
gg
