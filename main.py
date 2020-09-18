def on_b_pressed():
    mySprite.x += -1
controller.B.on_event(ControllerButtonEvent.PRESSED, on_b_pressed)

def on_a_pressed():
    mySprite.x += 1
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)

mySprite: Sprite = None
mySprite = sprites.create(img("""
        . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . 3 3 3 . . . . . . . 
            . . . . . . . 3 . . . . . . . . 
            . . . . . . . 3 . . . . . . . . 
            . . . 3 3 3 3 3 3 3 3 3 . . . . 
            . . . . . . . 3 . . . . . . . . 
            . . . . . . . 3 . . . . . . . . 
            . . . . . . . 3 . . . . . . . . 
            . . . . . . . 3 . . . . . . . . 
            . . . . . . . 3 . . . . . . . . 
            . . . . . . . 3 . . . . . . . . 
            . . . . . . . 3 . . . . . . . . 
            . . . . . . . 3 . . . . . . . . 
            . . . . . . . 3 . . . . . . . .
    """),
    SpriteKind.player)
mySprite.set_position(10, 100)

def on_forever():
    pass
forever(on_forever)
