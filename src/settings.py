import configparser
import os
configs = configparser.ConfigParser()

configs.read(os.path.abspath(os.path.join(os.path.dirname(__file__), 'configs.ini')))

FASTAPI_HOST = configs['fastapi']['host']
FASTAPI_PORT = configs['fastapi']['port']
STREAMLIT_PORT = configs['streamlit']['port']


__all__ = ['FASTAPI_HOST', 'FASTAPI_PORT', 'STREAMLIT_PORT']
