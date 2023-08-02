# README

Simple mitmproxy to bypass besst login. How to use.

1. Install Docker Desktop
2. Reboot
3. Run the container:

```sh
docker build -t mitmproxy . && docker run -p 8080:8080 -it mitmproxy
```

4. Create (or change) besst shortcut to:

`"C:\Program Files (x86)\BAFANG\BESST\BESST.exe" --proxy-server=127.0.0.1:8080`

5. Run besst (via the shortcut).

## Credits 

Credits to this project: https://github.com/OpenSourceEBike/Bafang_M500_M600