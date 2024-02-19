from http.server import BaseHTTPRequestHandler, HTTPServer
import json

# Datos de usuario y contraseña "correctos" para este ejemplo
USUARIO_CORRECTO = "mortadelo"
CONTRASENA_CORRECTA = "filemon"

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):

    def do_OPTIONS(self):
        # Enviar respuestas para solicitudes de pre-vuelo (preflight)
        self.send_response(200, "ok")
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()

    def do_POST(self):
        # Permitir solicitudes de cualquier origen
                   

        # Solo permitir la ruta /login para la autenticación
        if self.path == '/login':
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)

            # Intenta parsear los datos JSON recibidos
            try:
                datos = json.loads(post_data)
                usuario = datos.get('username')
                contrasena = datos.get('password')

                # Verificar si el usuario y la contraseña son correctos
                if usuario == USUARIO_CORRECTO and contrasena == CONTRASENA_CORRECTA:
                    self.send_response(200)
                    self.send_header('Content-type', 'application/json')
                    self.send_header('Access-Control-Allow-Origin', '*')   
                    self.end_headers()
                    self.wfile.write(json.dumps({"mensaje": "Login correcto"}).encode())
                else:
                    self.send_response(401)
                    self.send_header('Content-type', 'application/json')
                    self.end_headers()
                    self.wfile.write(json.dumps({"mensaje": "Usuario o contraseña incorrectos"}).encode())

            except json.JSONDecodeError:
                self.send_response(400)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps({"mensaje": "Formato de solicitud incorrecto"}).encode())
        else:
            self.send_response(404)
            self.end_headers()

def run(server_class=HTTPServer, handler_class=SimpleHTTPRequestHandler, port=5000):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f'Servidor iniciado en el puerto {port}...')
    httpd.serve_forever()

if __name__ == '__main__':
    run()
