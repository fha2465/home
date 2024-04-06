try:
      import os
      import platform
      import subprocess 
      import sys
      import socket

      server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      server_socket.bind((ip, port))
      server_socket.listen(5)
      print(f"Listening for incoming connections on {ip}:{port}...")
      client_socket, client_address = server_socket.accept()
      print(f"Connection established with {client_address[0]}:{client_address[1]}")
                # Here you can add further actions upon successful connection
except Exception as e:
       print(f"An error occurred: {e}")
       sys.exit(1)

