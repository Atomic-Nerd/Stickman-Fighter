import random
import pygame

pygame.init()

screen = pygame.display.set_mode((900, 600))

BG = pygame.image.load('BG.png')
run = True
WalkingMovesR = [pygame.image.load('Move/Move1R.png'), pygame.image.load('Move/Move2R.png'), pygame.image.load('Move/Move3R.png')]
WalkingMovesL = [pygame.image.load('Move/Move1L.png'), pygame.image.load('Move/Move2L.png'), pygame.image.load('Move/Move3L.png')]
HittingMovesR = [pygame.image.load('Hitting/Hitting1R.png'), pygame.image.load('Hitting/Hitting2R.png'),
                 pygame.image.load('Hitting/Hitting3R.png')]
HittingMovesL = [pygame.image.load('Hitting/Hitting1L.png'), pygame.image.load('Hitting/Hitting2L.png'),
                 pygame.image.load('Hitting/Hitting3L.png')]
FallingL = [pygame.image.load('Falling/FallL.png')]
FallingR = [pygame.image.load('Falling/FallR.png')]

DashR = [pygame.image.load('Dash/Dash1R.png'),pygame.image.load('Dash/Dash2R.png'),pygame.image.load('Dash/Dash3R.png'),pygame.image.load('Dash/Dash4R.png'),pygame.image.load('Dash/Dash5R.png'),pygame.image.load('Dash/Dash6R.png')]
DashL = [pygame.image.load('Dash/Dash1L.png'),pygame.image.load('Dash/Dash2L.png'),pygame.image.load('Dash/Dash3L.png'),pygame.image.load('Dash/Dash4L.png'),pygame.image.load('Dash/Dash5L.png'),pygame.image.load('Dash/Dash6L.png')]

DeadR = pygame.image.load("Dead/DEADR.png")
DeadL = pygame.image.load("Dead/DEADL.png")

BlockR = [pygame.image.load("Block/BlockR.png")]
BlockL = [pygame.image.load("Block/BlockL.png")]

ENDGAME = pygame.image.load('EndGame.png')

black = (0,0,0)
red = (255,0,0)

font = pygame.font.SysFont('comicsans', 40, True)
damagefont = pygame.font.SysFont('comicsans', 20, True)

DAMAGE20 = damagefont.render("-20", False, red)
DAMAGE40 = damagefont.render("-40", False, red)

endgame = False
black = (0, 0, 0)
vel = 10
DashHit = False
HeightSame = False
winner = " "
update = False
clock = -1

class PlayerStats:
    HP = 200
    Pos = 0
    X = 0
    Y = 482
    Facing = 1
    Move = False
    Hit = False
    Attack = False
    KB = False
    Dash = False
    Jump = False
    Block = False
    BlockKB = False
    isJump = False
    jumpCount = 10
    DashCooldown = 0
    HitCooldown = 0
    Sprite = WalkingMovesR
    LostHP = 0
    HitCooldownSecond = 0
    DashCooldownSecond = 0
    HitTextCooldown = "READY"
    DashTextCooldown = "READY"
    TEXT = font.render("P1.", False, black)

def main(Player,Against):
    if Against.Dash == True and Against.Pos == 5:
        if Against.Facing == 1:
            if Against.X - 360 < Player.X < Against.X + 100 and HeightSame:
                Player.HP -= 40
                DashHit = True
        else:
            if Against.X - 100 < Player.X < Against.X + 360 and HeightSame:
                Player.HP -= 40
                DashHit = True

    if DashHit == True:
        screen.blit(DAMAGE40, (Player.X + 30, Player.Y - 70))
        update = True
        DashHit = False

    if Against.Hit == True and Against.Pos == 1:
        if Against.Facing == 0:
            betweenfirst = Against.X - 140
            betweenlast = Against.X + 40
            Player.KBF = "left"
        else:
            betweenfirst = Against.X - 40
            betweenlast = Against.X + 140
            Player.KBF = "right"
        if betweenfirst < Player.X < betweenlast and HeightSame:
            Player.Attack = True
            Player.KB = True
            Player.Pos = 0
            Player.HP -= 20
            screen.blit(DAMAGE20, (Player.X + 30, Player.Y - 70))
            update = True

    if update == True:
        pygame.display.update()
        update == False

    if Player.KB == True:
        if Player.KBF == "left":
            Falling = FallingL
            EndFall = WalkingMovesL
        else:
            Falling = FallingR
            EndFall = WalkingMovesR
        count = 0
        while count < 5:
            pygame.time.delay(30)
            Player.Sprite = Falling
            drawing()
            if Player.KBF == "left":
                if Player.X > 30:
                    Player.X -= 30
            else:
                if Player.X < 770:
                    Player.X += 30
            count += 1
        Player.Sprite = EndFall
        Player.KB = False

    if keys[
        pygame.K_a] and Player.X > vel and Player.Hit != True and Player.Move != True and Player.Attack != True and Player.KB != True and Player.Dash != True and Player.Jump != True and Player.Block != True:
        Player.Facing = 0
        Player.Move = True
        Player.Sprite = WalkingMovesL
        Player.X -= vel

    if keys[
        pygame.K_d] and Player.X < 900 - vel - 100 and Player.Hit != True and Player.Move != True and Player.Attack != True and Player.KB != True and Player.Dash != True and Player.Jump != True and Player.Block != True:
        Player.Facing = 1
        Player.Sprite = WalkingMovesR
        Player.Move = True
        Player.X += vel

    if keys[
        pygame.K_SPACE] and Player.Hit != True and Player.Attack != True and Player.KB != True and Player.Dash != True and Player.Jump != True and Player.HitCooldown == 0 and Player.Block != True:
        Player.Hit = True
        Player.HitCooldown = 15
        Player.First = True

    if keys[
        pygame.K_e] and Player.Hit != True and Player.Attack != True and Player.KB != True and Player.Dash != True and Player.DashCooldown == 0 and Player.Jump != True and Player.Block != True:
        Player.Dash = True
        Player.DashCooldown = 100
        Player.First = True

    if keys[
        pygame.K_q] and Player.Move != True and Player.Hit != True and Player.Attack != True and Player.KB != True and Player.Dash != True and Player.Jump != True:
        Player.Block = True
        Player.Pos = 0
        if Player.Facing == 0:
            Player.Sprite = BlockL
        else:
            Player.Sprite = BlockR
    else:
        Player.Block = False
        if Player.Facing == 0:
            Player.Sprite = WalkingMovesL
        else:
            Player.Sprite = WalkingMovesR

    if not (Player.isJump):
        if keys[pygame.K_w]:
            Player.isJump = True
    else:
        if Player.jumpCount >= -10:
            Player.Y -= (Player.jumpCount * abs(Player.jumpCount)) * 0.5
            Player.jumpCount -= 1
        else:
            Player.jumpCount = 10
            Player.isJump = False

    if Player.Attack == True:
        P1.Move = False
        P1.Pos = 0
        P1.Hit = False
        P1.Attack = False

    if Player.Move:
        Player.Pos += 1
        if Player.Sprite == WalkingMovesR:
            Player.X += vel
        else:
            Player.X -= vel
        if Player.Pos == 3:
            Player.Pos = 0
            Player.Move = False

    if Player.Hit == True:
        if Player.First == True:
            Player.Pos = -1
            Player.First = False
        if Player.Facing == 1:
            Player.Sprite = HittingMovesR
        else:
            Player.Sprite = HittingMovesL
        Player.Pos += 1
        if Player.Pos == 3:
            Player.Pos = 0
            Player.Hit = False
            if Player.Facing == 1:
                Player.Sprite = WalkingMovesR
            else:
                Player.Sprite = WalkingMovesL

    if Player.DashCooldown > 0:
        Player.DashCooldown -= 1

    if Player.HitCooldown > 0:
        Player.HitCooldown -= 1

    if Player.Dash == True:
        if Player.First == True:
            Player.Pos = -1
            Player.First = False
        if Player.Facing == 1:
            Player.Sprite = DashR
        else:
            Player.Sprite = DashL
        Player.Pos += 1
        if Player.Pos < 2:
            if Player.Facing == 1:
                if Player.X < 680:
                    Player.X += 120
            else:
                if Player.X > 120:
                    Player.X -= 120
        if Player.Pos == 6:
            Player.Pos = 0
            Player.Dash = False
            if Player.Facing == 1:
                Player.Sprite = WalkingMovesR
            else:
                Player.Sprite = WalkingMovesL

P1 = PlayerStats(P1,P2)
P2 = PlayerStats(P2,P1)

P1.X = 100
P2.X = 700

P1.Facing = 1
P2.Facing = 0

P1.Sprite = WalkingMovesR
P2.Sprite = WalkingMovesL

P1.TEXT = font.render("P1.", False, black)
P2.TEXT = font.render("P2.", False, black)

def drawing():
    P1.LostHP = 200 - P1.HP
    P2.LostHP = 200 - P2.HP

    screen.blit(BG, (0, 0))

    screen.blit(P1.DashTextCooldown, (10, 70))
    screen.blit(P2.DashTextCooldown, (660, 70))

    screen.blit(P1.HitTextCooldown, (10, 40))
    screen.blit(P2.HitTextCooldown, (660, 40))

    screen.blit(P1.TEXT, (P1.X+30, P1.Y-50))
    screen.blit(P2.TEXT, (P2.X+30, P2.Y-50))

    if winner != "P2.":
        screen.blit(P1.Sprite[P1.Pos], (P1.X, P1.Y))
    else:
        if P1.Facing == 1:
            screen.blit(DeadR,(P1.X,590))
        else:
            screen.blit(DeadL,(P1.X,590))

    if winner != "P1.":
        screen.blit(P2.Sprite[P2.Pos], (P2.X, P2.Y))
    else:
        if P2.Facing == 1:
            screen.blit(DeadR,(P2.X,550))
        else:
            screen.blit(DeadL,(P2.X,550))

    pygame.draw.rect(screen, (255, 0, 0), (10 + P1.HP, 10, P1.LostHP, 10))
    pygame.draw.rect(screen, (0, 128, 0), (10, 10, P1.HP, 10))

    pygame.draw.rect(screen, (255, 0, 0), (660 + P2.HP, 10, P2.LostHP, 10))
    pygame.draw.rect(screen, (0, 128, 0), (660, 10, P2.HP, 10))

    pygame.draw.rect(screen, (255,0,0), (P1.X+30, P1.Y-20, 36, 5))
    pygame.draw.rect(screen, (0, 0, 255), (P2.X + 30, P2.Y - 20, 36, 5))

    if endgame == True:
        screen.blit(ENDGAME, (305, 227))
    pygame.display.update()


while run:

    pygame.time.delay(50)

    clock += 1

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    # ===================== COORDS TEST =========================
    CoordsTest = False

    if CoordsTest:
        print ("PLAYER ONE:")
        print ("X =",P1.X)
        print ("Y =",P1.Y)
        print ("PLAYER TWO:")
        print ("X =",P2.X)
        print ("Y =",P2.Y)

    # =====================  COOLDOWNS  =========================

    P1.DashCooldownSecond = P1.DashCooldown/10
    P2.DashCooldownSecond = P2.DashCooldown/10

    if P1.DashCooldownSecond == 0:
        P1.DashCooldownSecond = "READY"
    if P2.DashCooldownSecond == 0:
        P2.DashCooldownSecond = "READY"

    P1.DashTextCooldown = font.render(f"Dash: {P1.DashCooldownSecond}", False, red)
    P2.DashTextCooldown = font.render(f"Dash: {P2.DashCooldownSecond}" ,False, red)

    P1.HitCooldownSecond = P1.HitCooldown / 10
    P2.HitCooldownSecond = P2.HitCooldown / 10

    if P1.HitCooldownSecond == 0:
        P1.HitCooldownSecond = "READY"
    if P2.HitCooldownSecond == 0:
        P2.HitCooldownSecond = "READY"

    P1.HitTextCooldown = font.render(f"Swipe: {P1.HitCooldownSecond}", False, red)
    P2.HitTextCooldown = font.render(f"Swipe: {P2.HitCooldownSecond}", False, red)

    # ===================== SAME HEIGHT =========================

    if P1.Y-120 < P2.Y < P1.Y+50 or P2.Y-12 < P1.Y < P2.Y+50:
        HeightSame = True
    else:
        HeightSame = False

    # =====================   PLAYERS  ==========================

    main(P1,P2)
    main(P2,P1)

    # ====================== DEAD CHECK =========================
    if P1.HP <= 0 or P2.HP <= 0:
        if P1.HP <= 0:
            winner = "P2."
        else:
            winner = "P1."
        run = False
        endgame = True

    drawing()

while endgame == True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            endgame = False

    drawing()