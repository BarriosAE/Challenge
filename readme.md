## Instalación

1. Clona el repositorio:
    ```sh
    git clone https://github.com:BarriosAE/Challenge.git
    cd Challenge
    ```

2. Crea un entorno virtual:
    ```sh
    python -m venv venv
    ```

3. Activa el entorno virtual:

    - En Windows:
        ```sh
        .\venv\Scripts\activate
        ```

    - En macOS y Linux:
        ```sh
        source venv/bin/activate
        ```

4. Instala las dependencias:
    ```sh
    pip install -r requirements.txt
    playwright install
    ```

## Ejecución de las pruebas

Para ejecutar las pruebas, asegúrate de que el entorno virtual esté activado y luego ejecuta:
```sh
pytest '.\tests\test_aliexpress.py'  