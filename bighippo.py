def center_window(app, window, width: int, height: int):
    screen = app.primaryScreen()
    screen_geometry = screen.geometry()
    x = (screen_geometry.width() - width) // 2
    y = int((screen_geometry.height() - height) / 2.2)
    window.setGeometry(x, y, width, height)
