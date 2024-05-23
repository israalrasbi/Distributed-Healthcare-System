# -*- coding: utf-8 -*-
"""
Created on Sun May 12 01:13:13 2024

@author: hp
"""
from threading import Thread
from flask import Flask, request, send_from_directory, jsonify
import os

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Create uploads directory if it doesn't exist
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

def get_priority(file):
    priority_map = {'low': 0, 'medium': 1, 'high': 2}
    return priority_map.get(file.split('_')[-1].split('.')[0], 1)  # Default priority is medium

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400
    if file:
        filename = file.filename
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        return jsonify({'message': 'File uploaded successfully', 'filename': filename})

@app.route('/download/<filename>', methods=['GET'])
def download_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

@app.route('/list_files', methods=['GET'])
def list_files():
    files = os.listdir(app.config['UPLOAD_FOLDER'])
    files = sorted(files, key=lambda x: get_priority(x), reverse=True)  # Sort files by priority
    return jsonify({'files': files})

# Backup Server
backup_app = Flask(__name__)
UPLOAD_FOLDER_BACKUP = 'uploads_backup'
backup_app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER_BACKUP

# Create uploads_backup directory if it doesn't exist
if not os.path.exists(UPLOAD_FOLDER_BACKUP):
    os.makedirs(UPLOAD_FOLDER_BACKUP)

@backup_app.route('/upload', methods=['POST'])
def upload_file_backup():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400
    if file:
        filename = file.filename
        file.save(os.path.join(backup_app.config['UPLOAD_FOLDER'], filename))
        return jsonify({'message': 'File uploaded successfully', 'filename': filename})

@backup_app.route('/download/<filename>', methods=['GET'])
def download_file_backup(filename):
    return send_from_directory(backup_app.config['UPLOAD_FOLDER'], filename)

@backup_app.route('/list_files', methods=['GET'])
def list_files_backup():
    files = os.listdir(backup_app.config['UPLOAD_FOLDER'])
    files = sorted(files, key=lambda x: get_priority(x), reverse=True)  # Sort files by priority
    return jsonify({'files': files})

if __name__ == '__main__':
    # Start both servers in separate threads
    Thread(target=app.run, kwargs={'debug': True, 'port': 5000, 'use_reloader': False}).start()
    Thread(target=backup_app.run, kwargs={'debug': True, 'port': 5001, 'use_reloader': False}).start()