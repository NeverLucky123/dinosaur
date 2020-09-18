controller.B.onEvent(ControllerButtonEvent.Pressed, function on_b_pressed() {
    mySprite.x += -1
})
controller.A.onEvent(ControllerButtonEvent.Pressed, function on_a_pressed() {
    mySprite.x += 1
})
let mySprite : Sprite = null
mySprite = sprites.create(img`
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
    `, SpriteKind.Player)
mySprite.setPosition(10, 100)
forever(function on_forever() {
    
})
