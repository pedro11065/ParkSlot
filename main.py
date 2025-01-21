from src import create_app
import subprocess
from flask_cors import CORS

app = create_app();
CORS(app) 
app.app_context().push()



script_path = 'app.py'  # Substitua pelo caminho do seu script Python
# Comando para abrir um novo terminal (cmd) e rodar o script
subprocess.Popen(['start', 'cmd', '/K', f'python {script_path}'], shell=True)

app.run(debug=True) 