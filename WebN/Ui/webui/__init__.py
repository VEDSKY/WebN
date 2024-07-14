from webui import webui
import socket  # To get local IP

from WebN.Ui.webui.Templates.MainFrame import *

from WebN.Ui.webui.Templates.NoInternet import *

force_reload = False


def get_local_ip():
    # The IP address of the local machine is found by creating a socket connection.
    # The socket connects to an external address, but does not send any data.
    try:
        print(F'[Info][WebSocket][Connecting]')
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        print(F'[Info][WebSocket][Connected]')
        local_ip = s.getsockname()[0]
        print(F'[Info][WebSocket][Local IP is: {local_ip}]')
    except Exception:
        # Failed, return 'localhost'
        local_ip = 'localhost'
        print(F'[Warning][WebSocket][Invalid local IP {local_ip}]')
    finally:
        print(F'[Info][WebSocket][Closing WebSocket]')
        s.close()
    return local_ip


def has_internet(host="8.8.8.8", port=53, timeout=3):
    print(f'[Info][WebSocket][Checking for internet connection]')
    """
    Host: 8.8.8.8 (google-public-dns-a.google.com)
    OpenPort: 53/tcp
    Service: domain (DNS/TCP)
    """
    try:
        socket.setdefaulttimeout(timeout)
        socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect((host, port))
        print(f'[Info][WebSocket][Connected to: {socket.AF_INET}, {socket.SOCK_STREAM}]')
        print(f'[Info][WebSocket][Connected to internet.]')
        return True
    except socket.error as ex:
        print(f'[Error][WebSocket Exceptions][Exception: {ex}]')
        print(f'[Warning][WebSocket][No internet connection]')
        return False


def all_events(e: webui.event):
    if e.event_type == webui.eventType.CONNECTED:
        print('[Info][WebUI events][Successfully connected]')
    elif e.event_type == webui.eventType.DISCONNECTED:
        print('[Info][WebUI events][Successfully disconnected]')
    else:
        print(f'[Info][WebUI events][Element: {e.element}]')
        print(f'[Info][WebUI events][Window: {e.window}]')
        print(f'[Info][WebUI events][Event num: {e.event_num}]')
        print(f'[Info][WebUI events][Bind ID: {e.bind_id}]')


def exit_app(e: webui.event):
    webui.exit()


def reload_app(e: webui.event):
    global force_reload
    force_reload = True
    exit_app(e)


def reload():
    while force_reload:
        StartUI()


def StartUI():
    global force_reload
    if has_internet():
        html = MainFrame
    else:
        html = NoInternet

    # New window
    WebNMainFrame = webui.window()

    # Make the window URL accessible from public networks
    WebNMainFrame.set_public(True)

    # Wait forever (Otherwise WebUI will timeout after 30s)
    webui.set_timeout(15000)

    # Bind
    WebNMainFrame.bind('', all_events)
    WebNMainFrame.bind('Exit', exit_app)
    WebNMainFrame.bind('reload_button', reload_app)

    # Start the window without any browser
    WebNMainFrame.show(html, webui.browser.ChromiumBased)

    # Get URL of the window
    url = WebNMainFrame.get_url()

    # Get local IP
    local_ip = get_local_ip()

    # Replace `localhost` with IP
    link = url.replace('localhost', local_ip)

    # Print
    print(f'[Info][WebUI events][The GUI available in localhost: {link}]\n'
          f'[Description][WebUI][GUI available on this device only!]')

    # Wait until all windows are closed
    webui.wait()
    if force_reload:
        print(f'[Info][WebUI events][Force reloading]')
        reload()
        force_reload = False
    else:
        print(f'[Info][WebUI events][Closed]')
