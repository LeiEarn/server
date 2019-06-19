#encoding:utf-8
from werkzeug.utils import secure_filename
import time
import os
import requests
import json
import uuid
import hashlib 
import bson.binary 
import bson.objectid 
import bson.errors 
from PIL import Image
import flask
from flask import (
    Blueprint, flash, redirect, request, session, g, url_for,
    Flask, render_template, jsonify, request, make_response, send_from_directory, abort
)
import datetime

bp = Blueprint('prove_bp', __name__, url_prefix='/prove')

