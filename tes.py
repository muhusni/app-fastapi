import os

# Debugging prints to check environment variable values
print(f"DATABASE_USER_SSO: {os.getenv('DATABASE_USER_SSO', 'root')}")
print(f"DATABASE_PASSWORD_SSO: {os.getenv('DATABASE_PASSWORD_SSO', '')}")
print(f"DATABASE_CONNECTION_SSO: {os.getenv('DATABASE_CONNECTION_SSO', 'localhost')}")
print(f"DATABASE_PORT_SSO: {os.getenv('DATABASE_PORT_SSO', '3306')}")
print(f"DATABASE_SSO: {os.getenv('DATABASE_SSO', 'dbapp')}")

# Construct the DATABASE_URL
DATABASE_URL = f"mysql+pymysql://{os.getenv('DATABASE_USER_SSO', 'root')}:{os.getenv('DATABASE_PASSWORD_SSO', '')}@{os.getenv('DATABASE_CONNECTION_SSO', 'localhost')}:{os.getenv('DATABASE_PORT_SSO', '3306')}/{os.getenv('DATABASE_SSO', 'dbapp')}"

print(f"DATABASE_URL: {DATABASE_URL}")
