#!/usr/bin/env python
import os

from app import create_app

api_mode = os.getenv('FLASK_ENV') or 'develop'
app = create_app(api_mode)
