from ftplib import FTP

ftp_server = 'ftp.example.com'
ftp_port = 21
ftp_username = 'ftpuser'
ftp_password = 'ftppassword'

def configure_ftp():
    ftp = FTP()
    ftp.connect(ftp_server, ftp_port)
    ftp.login(ftp_username, ftp_password)
    print(f"Connected to {ftp_server}")

    ftp.retrlines('LIST')

    local_file = 'localfile.txt'
    remote_file = 'remotefile.txt'
    with open(local_file, 'rb') as f:
        ftp.storbinary(f'STOR {remote_file}', f)

    ftp.quit()
    print("FTP configuration complete.")

if __name__ == "__main__":
    configure_ftp()
