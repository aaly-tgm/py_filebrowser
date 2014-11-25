import logging
from logging.handlers import RotatingFileHandler
import os
from flask import Flask, request, render_template, Blueprint
from FileBrowser import Filebrowser

app = Flask(__name__)
__author__ = 'Ahmed ALY'

@app.route('/index', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route('/requests', methods=['GET', 'POST'])
def requests():
    app.logger.warning('A warning occurred (%d apples)', 42)
    app.logger.error('An error occurred')
    app.logger.info('Info')
    f = Filebrowser()
    action = request.args.get('action', '')

    if action == 'back':
        back = request.args.get('back', '')
        f.setCurrentDir(back)

    if action == 'out':
        current = request.args.get('current', '')
        f.setCurrentDir(current)
        f.out()

    if action == 'forward':
        forward = request.args.get('forward', '')
        f.setCurrentDir(forward)

    if action == 'home':
        current = request.args.get('current', '')
        f.setCurrentDir(current)

    if action == 'createdir':
        current = request.args.get('current', '')
        dir = request.args.get('dir', '')
        f.setCurrentDir(current)
        f.create_dir(dir)

    if action == 'opendir':
        current = request.args.get('current', '')
        dir = request.args.get('dir', '')
        f.setCurrentDir(current + dir)

    if action == 'openfile':
        current = request.args.get('current', '')
        file = request.args.get('file', '')
        f.setCurrentDir(current)
        return f.open_file(file)

    if action == 'listelements':
        current = request.args.get('current', '')
        f.setCurrentDir(current)

    if action == 'renameFile':
        current = request.args.get('current', '')
        old_fileName = request.args.get('oldfileName', '')
        new_fileName = request.args.get('newfileName', '')

        f.setCurrentDir(current)
        f.rename_file(old_fileName, new_fileName)

    if action == 'renameDir':
        current = request.args.get('current', '')
        old_DirName = request.args.get('oldDirName', '')
        new_DirName = request.args.get('newDirName', '')

        f.setCurrentDir(current)
        f.rename_directory(old_DirName, new_DirName)

    if action != 'openfile':
        return f.listElements()

if __name__ == '__main__':
    handler = RotatingFileHandler('flask.log', maxBytes=10000, backupCount=1)
    handler.setLevel(logging.INFO)
    app.logger.addHandler(handler)
    app.run()
