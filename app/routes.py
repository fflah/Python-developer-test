from app import web
from app.controllers import BeritaController

web.add_resource(BeritaController.ViewController, '/')