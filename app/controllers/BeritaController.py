from flask_restful import Resource
from flask import render_template, make_response
from app.helper import helper
import json
from app.models.BeritaModel import BeritaModel
from app import db
import requests

class ViewController(Resource):
    def get(self):
        view = render_template('index.html')
        return make_response(view)
    
    def post(self):
        try:
            scrape_berita = helper.Scrape()
            # save data berita to db
            for value in scrape_berita['data']:
                berita_model = BeritaModel(url=value['url'], judul=value['judul'], waktu_tayang=value['waktu_tayang'], konten=value['konten'])
                db.session.add(berita_model)
                db.session.commit()
            
            view = render_template('index.html', data_berita=json.dumps(scrape_berita))
            return make_response(view)
        except requests.exceptions.RequestException as e:
            return 'No internet Connection, please connect with internet'

