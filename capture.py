# -*- encoding: utf-8 -*-
import AppKit
import os
import pyimgur

CAPTURE_FILE_NAME = 'capture.jpg'

def get_current_screen_rect():
    mouse_location = AppKit.NSEvent.mouseLocation()
    for screen in AppKit.NSScreen.screens():
        frame = screen.frame()
        if AppKit.NSMouseInRect(mouse_location, frame, False):
            frame.origin.x = int(frame.origin.x)
            # Calculating for y is needed for screencapture -R option.
            frame.origin.y = int(frame.origin.y + frame.size.height - AppKit.NSScreen.mainScreen().frame().size.height)
            frame.size.width = int(frame.size.width)
            frame.size.height = int(frame.size.height)
            return frame
    return None

def capture_current_screen():
    rect = get_current_screen_rect()
    if rect:
        rect_str = str(rect.origin.x) + ',' + str(rect.origin.y) + ',' + str(rect.size.width) + ',' + str(rect.size.height)
        os.system('screencapture -x -R' + rect_str + ' ' + CAPTURE_FILE_NAME)

def upload_to_imgur():
    # Read client id
    imgur_client_id_file = open('imgur_client_id')
    imgur_client_id = imgur_client_id_file.read().strip()
    imgur_client_id_file.close()

    im = pyimgur.Imgur(imgur_client_id)
    uploaded_image = im.upload_image(CAPTURE_FILE_NAME, title='Uploaded with OS X screencapture.')

    pb = AppKit.NSPasteboard.generalPasteboard()
    pb.clearContents()
    pb.writeObjects_(AppKit.NSArray.arrayWithObject_(uploaded_image.link))
    os.system("terminal-notifier -title 'Screencapture' -message 'Screencapture link is pasted into clipboard!'")

def remove_uploaded_file():
    os.system('rm ' + CAPTURE_FILE_NAME)

if __name__ == '__main__':
    capture_current_screen()
    upload_to_imgur()
    remove_uploaded_file()
