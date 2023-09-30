from pico2d import *

TUK_WIDTH, TUK_HEIGHT = 800, 600
open_canvas(TUK_WIDTH, TUK_HEIGHT)
TUK_ground = load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')
hand = load_image('hand_arrow.png')
dir_check = 0
hand_x, hand_y, hand_check = [], [], []

def handle_events():
    global running
    global x, y
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_MOUSEBUTTONDOWN:
            hand_x.append(event.x), hand_y.append(TUK_HEIGHT - 1 - event.y)
            hand_check.append(1)
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False
    pass

running = True
x, y = TUK_WIDTH // 2, TUK_HEIGHT // 2
frame = 0
#hide_cursor()

while running:
    clear_canvas()
    TUK_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
    character.clip_draw(frame * 100, 100 * 1, 100, 100, x, y)
    for i in range(0, len(hand_check)):
        if hand_check[i] == 1:
            hand.draw(hand_x[i], hand_y[i])
    update_canvas()
    frame = (frame + 1) % 8

    handle_events()
    delay(0.08)

close_canvas()




