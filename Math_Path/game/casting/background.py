import pyray
from game.services.video_service import VideoService


screenWidth = 800
screenHeight = 650


class Background(VideoService):

    pyray.init_window(screenWidth, screenHeight,
                      "Path")

    image = pyray.load_image(
        "path.png")

    texture = pyray.load_texture_from_image(image)

    pyray.unload_image(image)

    while not pyray.window_should_close():

        pyray.begin_drawing()

        pyray.clear_background(pyray.WHITE)

        pyray.draw_texture(texture, int(screenWidth/2 - texture.width/2),
                           int(screenHeight/2 - texture.height/2), pyray.WHITE)

        pyray.end_drawing()

    pyray.unload_texture(texture)

    # clean up
    pyray.close_window()
