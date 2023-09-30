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
            hand_x.append(event.x)
            hand_y.append(TUK_HEIGHT - 1 - event.y)
            if x > event.x:
                hand_check.append(1)
            else:
                hand_check.append(2)
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

running = True
x, y = TUK_WIDTH // 2, TUK_HEIGHT // 2
frame, idx = 0, 0
save_x, save_y = x, y

while running:
    clear_canvas()
    TUK_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
    for i in range(0, len(hand_check)):
        if hand_check[i] == 1 or hand_check[i] == 2:
            hand.draw(hand_x[i], hand_y[i])

    if len(hand_check) > 0:
        if hand_check[0] == 1:
            character.clip_draw(frame * 100, 100 * 0, 100, 100, x, y)
        elif hand_check[0] == 2:
            character.clip_draw(frame * 100, 100 * 1, 100, 100, x, y)

        t = idx / 500
        x = (1 - t) * save_x + t * hand_x[0]
        y = (1 - t) * save_y + t * hand_y[0]
        idx += 1
        if idx >= 500:
            idx = 0
            save_x, save_y = x, y
            hand_x.pop(0), hand_y.pop(0), hand_check.pop(0)
    else:
        character.clip_draw(frame * 100, 100 * 0, 100, 100, x, y)

    update_canvas()
    frame = (frame + 1) % 8
    handle_events()

close_canvas()
