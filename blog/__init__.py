import pymysql

# since mysql-python doesn't support python3, we need to use pymysql and modify the version info
pymysql.version_info = (1, 3, 13, "final", 0)
pymysql.install_as_MySQLdb()