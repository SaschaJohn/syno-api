import os

from synology_api import core_sys_info

ip = os.environ["IP"]
port = os.environ["PORT"]
user = os.environ["USER"]
password = os.environ["PASSWORD"]

session = core_sys_info.SysInfo(ip, port, user, password, secure=False, cert_verify=True, dsm_version=6, debug=True, otp_code=None)
session.shutdown(1)