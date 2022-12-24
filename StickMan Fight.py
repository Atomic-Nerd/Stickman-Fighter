import random
import pygame
import sys

pygame.init()

screen = pygame.display.set_mode((900, 600))

BG = pygame.image.load('BG.png')

WalkingMovesR = [pygame.image.load('Move/Move1R.png'), pygame.image.load('Move/Move2R.png'),
                 pygame.image.load('Move/Move3R.png')]
WalkingMovesL = [pygame.image.load('Move/Move1L.png'), pygame.image.load('Move/Move2L.png'),
                 pygame.image.load('Move/Move3L.png')]
HittingMovesR = [pygame.image.load('Hitting/Hitting1R.png'), pygame.image.load('Hitting/Hitting2R.png'),
                 pygame.image.load('Hitting/Hitting3R.png')]
HittingMovesL = [pygame.image.load('Hitting/Hitting1L.png'), pygame.image.load('Hitting/Hitting2L.png'),
                 pygame.image.load('Hitting/Hitting3L.png')]
FallingL = [pygame.image.load('Falling/FallL.png')]
FallingR = [pygame.image.load('Falling/FallR.png')]

DashR = [pygame.image.load('Dash/Dash1R.png'), pygame.image.load('Dash/Dash2R.png'),
         pygame.image.load('Dash/Dash3R.png'), pygame.image.load('Dash/Dash4R.png'),
         pygame.image.load('Dash/Dash5R.png'), pygame.image.load('Dash/Dash6R.png')]
DashL = [pygame.image.load('Dash/Dash1L.png'), pygame.image.load('Dash/Dash2L.png'),
         pygame.image.load('Dash/Dash3L.png'), pygame.image.load('Dash/Dash4L.png'),
         pygame.image.load('Dash/Dash5L.png'), pygame.image.load('Dash/Dash6L.png')]

DeadR = pygame.image.load("Dead/DEADR.png")
DeadL = pygame.image.load("Dead/DEADL.png")

BlockR = [pygame.image.load("Block/BlockR.png")]
BlockL = [pygame.image.load("Block/BlockL.png")]

P1WINS = pygame.image.load('Player1Wins.png')
P2WINS = pygame.image.load('Player2Wins.png')

MAINMENU = pygame.image.load('Menu/MainMenu.png')
PLAYBIG = pygame.image.load('Menu/PLAYBIG.png')
HOWBIG = pygame.image.load('Menu/HOWBIG.png')
LEADERBOARDBIG = pygame.image.load('Menu/LEADERBOARDBIG.png')
QUITBIG = pygame.image.load('Menu/QUITBIG.png')
INSTRUCTIONS = pygame.image.load('Menu/INSTRUCTIONS.png')
INSTRUCTIONSBACK = pygame.image.load('Menu/INSTRUCTIONSBACK.png')
LEADERBOARD = pygame.image.load('Menu/LEADERBOARD.png')
LEADERBOARDBACK = pygame.image.load('Menu/LEADERBOARDBACK.png')
USERNAMES = pygame.image.load('Menu/USERNAMES.png')
ARROW = pygame.image.load('Menu/ARROW.png')

green = (0, 128, 0)
blue = (0, 0, 255)
black = (0, 0, 0)
red = (255, 0, 0)

font = pygame.font.SysFont('comicsans', 40, True)
leaderboardfont = pygame.font.SysFont('comicsans', 50, True)
damagefont = pygame.font.SysFont('comicsans', 20, True)

DAMAGE20 = damagefont.render("-20", False, red)
DAMAGE40 = damagefont.render("-40", False, red)

endgame = False
vel = 10
DashHit = False
HeightSame = False
winner = " "
update = False
clock = -1
run = False
menu = True
Instructions = False
Leaderboard = False
Usernames = False
P1NAMEWRITING = True
P2NAMEWRITING = False

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


P1 = PlayerStats()
P2 = PlayerStats()

P1.X = 100
P2.X = 700

P1.Facing = 1
P2.Facing = 0

P1.Sprite = WalkingMovesR
P2.Sprite = WalkingMovesL

P1.TEXT = font.render("P1.", False, black)
P2.TEXT = font.render("P2.", False, black)

def Menu():
    if 240 < x < 600 and 173 < y < 235:
        screen.blit(PLAYBIG, (0, 0))
    elif 240 < x < 600 and 275 < y < 342:
        screen.blit(HOWBIG, (0, 0))
    elif 240 < x < 600 and 377 < y < 447:
        screen.blit(LEADERBOARDBIG, (0, 0))
    elif 240 < x < 600 and 488 < y < 552:
        screen.blit(QUITBIG, (0, 0))
    else:
        screen.blit(MAINMENU, (0, 0))

    pygame.display.update()


def drawing():
    P1.LostHP = 200 - P1.HP
    P2.LostHP = 200 - P2.HP

    screen.blit(BG, (0, 0))

    screen.blit(P1.DashTextCooldown, (10, 70))
    screen.blit(P2.DashTextCooldown, (660, 70))

    screen.blit(P1.HitTextCooldown, (10, 40))
    screen.blit(P2.HitTextCooldown, (660, 40))

    screen.blit(P1.TEXT, (P1.X + 30, P1.Y - 50))
    screen.blit(P2.TEXT, (P2.X + 30, P2.Y - 50))

    if winner != "P2":
        screen.blit(P1.Sprite[P1.Pos], (P1.X, P1.Y))
    else:
        screen.blit(P2WINS, (305, 227))
        if P1.Facing == 1:
            screen.blit(DeadR, (P1.X, 590))
        else:
            screen.blit(DeadL, (P1.X, 590))

    if winner != "P1":
        screen.blit(P2.Sprite[P2.Pos], (P2.X, P2.Y))
    else:
        screen.blit(P1WINS, (305, 227))
        if P2.Facing == 1:
            screen.blit(DeadR, (P2.X, 550))
        else:
            screen.blit(DeadL, (P2.X, 550))

    pygame.draw.rect(screen, red, (10 + P1.HP, 10, P1.LostHP, 10))
    pygame.draw.rect(screen, green, (10, 10, P1.HP, 10))

    pygame.draw.rect(screen, red, (660 + P2.HP, 10, P2.LostHP, 10))
    pygame.draw.rect(screen, green, (660, 10, P2.HP, 10))

    pygame.draw.rect(screen, red, (P1.X + 30, P1.Y - 20, 36, 5))
    pygame.draw.rect(screen, blue, (P2.X + 30, P2.Y - 20, 36, 5))

    pygame.display.update()


while menu:

    winner = ""
    P1NAME = ""
    P2NAME = ""
    P1NAMEWRITING = True

    # ==================== LEADERBOARD DATA =======================

    Leaderboardnames = open('SaveData/LeaderBoardNames', 'r+')
    Names = Leaderboardnames.read().splitlines()
    NameSave = Names

    Leaderboardscore = open('SaveData/LeaderBoardScore', 'r+')
    Scores = Leaderboardscore.read().splitlines()
    ScoreSave = Scores

    for i in range(0, len(Scores)):
        Scores[i] = int(Scores[i])
        ScoreSave[i] = int(ScoreSave[i])

    n = len(Scores)
    for i in range(n):

        for j in range(0, n - i - 1):

            if Scores[j] < Scores[j + 1]:
                Names[j], Names[j + 1] = Names[j + 1], Names[j]
                Scores[j], Scores[j + 1] = Scores[j + 1], Scores[j]

    LeaderboardListN = []
    #for i in range(0, 5):
        #LeaderboardListN.append(leaderboardfont.render(Names[i], False, black))

    LeaderboardListW = []
    #for i in range(0, 5):
        #LeaderboardListW.append(leaderboardfont.render(str(Scores[i]), False, black))

    Leaderboardscore.close()
    Leaderboardnames.close()

    # =================================================

    pygame.time.delay(50)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    x, y = pygame.mouse.get_pos()

    if event.type == pygame.MOUSEBUTTONDOWN:
        if 240 < x < 600 and 173 < y < 235:
            Usernames = True
        elif 240 < x < 600 and 275 < y < 342:
            Instructions = True
        elif 240 < x < 600 and 377 < y < 447:
            Leaderboard = True
        elif 240 < x < 600 and 488 < y < 552:
            sys.exit()

    while Instructions == True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        x, y = pygame.mouse.get_pos()

        if 10 < x < 116 and 10 < y < 60:
            screen.blit(INSTRUCTIONSBACK, (0, 0))
        else:
            screen.blit(INSTRUCTIONS, (0, 0))
        pygame.display.update()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if 10 < x < 116 and 10 < y < 60:
                Instructions = False

    while Usernames == True:

        pygame.time.delay(90)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        screen.blit(USERNAMES,(0,0))
        P1NAMETEXT = leaderboardfont.render(P1NAME,False,black)
        screen.blit(P1NAMETEXT,(134,248))

        P2NAMETEXT = leaderboardfont.render(P2NAME, False, black)
        screen.blit(P2NAMETEXT, (134, 445))

        pygame.display.update()

        if P1NAMEWRITING == True:
            screen.blit(ARROW, (25,235))
            pygame.display.update()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    P1NAME = P1NAME[0:-1]
                elif event.key == pygame.K_RETURN:
                    P1NAMEWRITING = False
                    P2NAMEWRITING = True
                else:
                    P1NAME += event.unicode

        if P2NAMEWRITING == True:
            screen.blit(ARROW, (25,435))
            pygame.display.update()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    P2NAME = P2NAME[0:-1]
                elif event.key == pygame.K_RETURN and P2NAME != "":
                    P2NAMEWRITING = False
                    run = True
                    Usernames = False
                else:
                    if event.key != pygame.K_RETURN:
                        P2NAME += event.unicode

        if run == True:
            P1NAMEWRITING = False
            P2NAMEWRITING = False
            if P1NAME not in NameSave:

                NameSave.append(P1NAME)
                ScoreSave.append(0)

            if P2NAME not in NameSave:

                NameSave.append(P2NAME)
                ScoreSave.append(0)

            Leaderboardnames = open('SaveData/LeaderBoardNames', 'r+') 
            Leaderboardnames.truncate(0)
            Leaderboardnames.close()

            Leaderboardnames = open('SaveData/LeaderBoardNames', 'r+')
            for i in range(0, len(ScoreSave)):
                Leaderboardnames.writelines(NameSave[i] + "\n")
            Leaderboardnames.close()

    while Leaderboard == True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        x, y = pygame.mouse.get_pos()

        if 10 < x < 116 and 10 < y < 60:
            screen.blit(LEADERBOARDBACK, (0, 0))
        else:
            screen.blit(LEADERBOARD, (0, 0))

        screen.blit(LeaderboardListN[0], (112,180))
        screen.blit(LeaderboardListW[0], (460,180))

        screen.blit(LeaderboardListN[1], (112, 244))
        screen.blit(LeaderboardListW[1], (460, 244))

        screen.blit(LeaderboardListN[2], (112, 311))

        screen.blit(LeaderboardListW[2], (460, 311))

        screen.blit(LeaderboardListN[3], (112, 375))
        screen.blit(LeaderboardListW[3], (460, 375))

        screen.blit(LeaderboardListN[4], (112, 442))
        screen.blit(LeaderboardListW[4], (460, 442))

        pygame.display.update()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if 10 < x < 116 and 10 < y < 60:
                Leaderboard = False

    if run != True:
        Menu()
    else:
        pygame.time.delay(50)

    while run:

        pygame.time.delay(50)

        clock += 1

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        keys = pygame.key.get_pressed()
        # ========================= TESTS =========================
        CoordsTest = False

        if CoordsTest:
            print("PLAYER ONE:")
            print("X =", P1.X)
            print("Y =", P1.Y)
            print("PLAYER TWO:")
            print("X =", P2.X)
            print("Y =", P2.Y)

        FacingTest = False

        if FacingTest:
            print("PLAYER ONE:", P1.Facing)
            print("PLAYER TWO:", P2.Facing)

        # =====================  COOLDOWNS  =========================

        P1.DashCooldownSecond = P1.DashCooldown / 10
        P2.DashCooldownSecond = P2.DashCooldown / 10

        if P1.DashCooldownSecond == 0:
            P1.DashCooldownSecond = "READY"
        if P2.DashCooldownSecond == 0:
            P2.DashCooldownSecond = "READY"

        P1.DashTextCooldown = font.render(f"Dash: {P1.DashCooldownSecond}", False, red)
        P2.DashTextCooldown = font.render(f"Dash: {P2.DashCooldownSecond}", False, blue)

        P1.HitCooldownSecond = P1.HitCooldown / 10
        P2.HitCooldownSecond = P2.HitCooldown / 10

        if P1.HitCooldownSecond == 0:
            P1.HitCooldownSecond = "READY"
        if P2.HitCooldownSecond == 0:
            P2.HitCooldownSecond = "READY"

        P1.HitTextCooldown = font.render(f"Swipe: {P1.HitCooldownSecond}", False, red)
        P2.HitTextCooldown = font.render(f"Swipe: {P2.HitCooldownSecond}", False, blue)

        # ===================== SAME HEIGHT =========================

        if P1.Y - 120 < P2.Y < P1.Y + 50 or P2.Y - 12 < P1.Y < P2.Y + 50:
            HeightSame = True
        else:
            HeightSame = False

        # =====================  PLAYER ONE =========================

        if P2.Dash == True and P2.Pos == 5:
            if P2.Facing == 1:
                if P2.X - 360 < P1.X < P2.X + 100 and HeightSame:
                    P1.HP -= 40
                    DashHit = True
            else:
                if P2.X - 100 < P1.X < P2.X + 360 and HeightSame:
                    P1.HP -= 40
                    DashHit = True

        if DashHit == True:
            screen.blit(DAMAGE40, (P1.X + 30, P1.Y - 70))
            update = True
            DashHit = False

        if P2.Hit == True and P2.Pos == 1:
            if P2.Facing == 0:
                betweenfirst = P2.X - 140
                betweenlast = P2.X + 40
                P1.KBF = "left"
            else:
                betweenfirst = P2.X - 40
                betweenlast = P2.X + 140
                P1.KBF = "right"
            if betweenfirst < P1.X < betweenlast and HeightSame:
                if P1.KBF == "right" and P1.Facing == 0 and P1.Block == True:
                    P1.BlockKB = True
                elif P1.KBF == "left" and P1.Facing == 1 and P1.Block == True:
                    P1.BlockKB = True
                else:
                    P1.Attack = True
                    P1.KB = True
                    P1.Pos = 0
                    P1.HP -= 20
                    screen.blit(DAMAGE20, (P1.X + 30, P1.Y - 70))
                    update = True

        if update == True:
            pygame.display.update()
            update == False

        if P1.BlockKB == True:
            if P1.KBF == "left":
                P1.Sprite = BlockR
            else:
                P1.Sprite = BlockL
            count = 0
            while count < 2:
                pygame.time.delay(30)
                drawing()
                if P1.KBF == "left":
                    if P1.X > 30:
                        P1.X -= 40
                else:
                    if P1.X < 770:
                        P1.X += 40
                count += 1
            P1.BlockKB = False

        if P1.KB == True:
            if P1.KBF == "left":
                Falling = FallingL
                EndFall = WalkingMovesL
            else:
                Falling = FallingR
                EndFall = WalkingMovesR
            count = 0
            while count < 5:
                pygame.time.delay(30)
                P1.Sprite = Falling
                drawing()
                if P1.KBF == "left":
                    if P1.X > 30:
                        P1.X -= 30
                else:
                    if P1.X < 770:
                        P1.X += 30
                count += 1
            P1.Sprite = EndFall
            P1.KB = False

        if keys[
            pygame.K_a] and P1.X > vel and P1.Hit != True and P1.Move != True and P1.Attack != True and P1.KB != True and P1.Dash != True and P1.Jump != True and P1.Block != True:
            P1.Facing = 0
            P1.Move = True
            P1.Sprite = WalkingMovesL
            P1.X -= vel

        if keys[
            pygame.K_d] and P1.X < 900 - vel - 100 and P1.Hit != True and P1.Move != True and P1.Attack != True and P1.KB != True and P1.Dash != True and P1.Jump != True and P1.Block != True:
            P1.Facing = 1
            P1.Sprite = WalkingMovesR
            P1.Move = True
            P1.X += vel

        if keys[
            pygame.K_SPACE] and P1.Hit != True and P1.Attack != True and P1.KB != True and P1.Dash != True and P1.Jump != True and P1.HitCooldown == 0 and P1.Block != True:
            P1.Hit = True
            P1.HitCooldown = 15
            P1.First = True

        if keys[
            pygame.K_e] and P1.Hit != True and P1.Attack != True and P1.KB != True and P1.Dash != True and P1.DashCooldown == 0 and P1.Jump != True and P1.Block != True:
            P1.Dash = True
            P1.DashCooldown = 100
            P1.First = True

        if keys[
            pygame.K_q] and P1.Move != True and P1.Hit != True and P1.Attack != True and P1.KB != True and P1.Dash != True and P1.Jump != True:
            P1.Block = True
            P1.Pos = 0
            if P1.Facing == 0:
                P1.Sprite = BlockL
            else:
                P1.Sprite = BlockR
        else:
            P1.Block = False
            if P1.Facing == 0:
                P1.Sprite = WalkingMovesL
            else:
                P1.Sprite = WalkingMovesR

        if not (P1.isJump):
            if keys[pygame.K_w]:
                P1.isJump = True
        else:
            if P1.jumpCount >= -10:
                P1.Y -= (P1.jumpCount * abs(P1.jumpCount)) * 0.5
                P1.jumpCount -= 1
            else:
                P1.jumpCount = 10
                P1.isJump = False

        if P1.Attack == True:
            P1.Move = False
            P1.Pos = 0
            P1.Hit = False
            P1.Attack = False

        if P1.Move:
            P1.Pos += 1
            if P1.Sprite == WalkingMovesR:
                P1.X += vel
            else:
                P1.X -= vel
            if P1.Pos == 3:
                P1.Pos = 0
                P1.Move = False

        if P1.Hit == True:
            if P1.First == True:
                P1.Pos = -1
                P1.First = False
            if P1.Facing == 1:
                P1.Sprite = HittingMovesR
            else:
                P1.Sprite = HittingMovesL
            P1.Pos += 1
            if P1.Pos == 3:
                P1.Pos = 0
                P1.Hit = False
                if P1.Facing == 1:
                    P1.Sprite = WalkingMovesR
                else:
                    P1.Sprite = WalkingMovesL

        if P1.DashCooldown > 0:
            P1.DashCooldown -= 1

        if P1.HitCooldown > 0:
            P1.HitCooldown -= 1

        if P1.Dash == True:
            if P1.First == True:
                P1.Pos = -1
                P1.First = False
            if P1.Facing == 1:
                P1.Sprite = DashR
            else:
                P1.Sprite = DashL
            P1.Pos += 1
            if P1.Pos < 2:
                if P1.Facing == 1:
                    if P1.X < 680:
                        P1.X += 120
                else:
                    if P1.X > 120:
                        P1.X -= 120
            if P1.Pos == 6:
                P1.Pos = 0
                P1.Dash = False
                if P1.Facing == 1:
                    P1.Sprite = WalkingMovesR
                else:
                    P1.Sprite = WalkingMovesL

        # ===================== PLAYER TWO ==========================

        if P1.Dash == True and P1.Pos == 5:
            if P1.Facing == 1:
                if P1.X - 360 < P2.X < P1.X + 100 and HeightSame:
                    P2.HP -= 40
                    DashHit = True
            else:
                if P1.X - 100 < P2.X < P1.X + 360 and HeightSame:
                    P2.HP -= 40
                    DashHit = True

        if DashHit == True:
            screen.blit(DAMAGE40, (P2.X + 30, P2.Y - 70))
            update = True
            DashHit = False

        if P1.Hit == True and P1.Pos == 1:
            if P1.Facing == 0:
                betweenfirst = P1.X - 140
                betweenlast = P1.X + 40
                P2.KBF = "left"
            else:
                betweenfirst = P1.X - 40
                betweenlast = P1.X + 140
                P2.KBF = "right"
            if betweenfirst < P2.X < betweenlast and HeightSame:
                if P2.KBF == "right" and P2.Facing == 0 and P2.Block == True:
                    P2.BlockKB = True
                elif P2.KBF == "left" and P2.Facing == 1 and P2.Block == True:
                    P2.BlockKB = True
                else:
                    P2.Attack = True
                    P2.KB = True
                    P2.Pos = 0
                    P2.HP -= 20
                    screen.blit(DAMAGE20, (P2.X + 30, P2.Y - 70))
                    update = True

        if update == True:
            pygame.display.update()
            update == False

        if P2.KB == True:
            if P2.KBF == "left":
                Falling = FallingL
                EndFall = WalkingMovesL
            else:
                Falling = FallingR
                EndFall = WalkingMovesR
            count = 0
            while count < 5:
                pygame.time.delay(30)
                P2.Sprite = Falling
                drawing()
                if P2.KBF == "left":
                    if P2.X > 30:
                        P2.X -= 30
                else:
                    if P2.X < 770:
                        P2.X += 30
                count += 1
            P2.Sprite = EndFall
            P2.KB = False

        if P2.BlockKB == True:
            if P2.KBF == "left":
                P2.Sprite = BlockR
            else:
                P2.Sprite = BlockL
            count = 0
            while count < 2:
                pygame.time.delay(30)
                drawing()
                if P2.KBF == "left":
                    if P2.X > 30:
                        P2.X -= 40
                else:
                    if P2.X < 770:
                        P2.X += 40
                count += 1
            P2.BlockKB = False

        if keys[
            pygame.K_j] and P2.X > vel and P2.Hit != True and P2.Move != True and P2.Attack != True and P2.KB != True and P2.Dash != True and P2.Jump != True and P2.Block != True:
            P2.Facing = 0
            P2.Move = True
            P2.Sprite = WalkingMovesL
            P2.X -= vel

        if keys[
            pygame.K_l] and P2.X < 900 - vel - 100 and P2.Hit != True and P2.Move != True and P2.Attack != True and P2.KB != True and P2.Dash != True and P2.Jump != True and P2.Block != True:
            P2.Facing = 1
            P2.Sprite = WalkingMovesR
            P2.Move = True
            P2.X += vel

        if keys[
            pygame.K_RSHIFT] and P2.Hit != True and P2.Attack != True and P2.KB != True and P2.Dash != True and P2.Jump != True and P2.HitCooldown == 0 and P2.Block != True:
            P2.Hit = True
            P2.HitCooldown = 15
            P2.First = True

        if keys[
            pygame.K_o] and P2.Hit != True and P2.Attack != True and P2.KB != True and P2.Dash != True and P2.DashCooldown == 0 and P2.Jump != True and P2.Block != True:
            P2.Dash = True
            P2.DashCooldown = 100
            P2.First = True

        if keys[
            pygame.K_u] and P2.Move != True and P2.Hit != True and P2.Attack != True and P2.KB != True and P2.Dash != True and P2.Jump != True:
            P2.Block = True
            P2.Pos = 0
            if P2.Facing == 0:
                P2.Sprite = BlockL
            else:
                P2.Sprite = BlockR
        else:
            P2.Block = False
            if P2.Facing == 0:
                P2.Sprite = WalkingMovesL
            else:
                P2.Sprite = WalkingMovesR

        if not (P2.isJump):
            if keys[pygame.K_i]:
                P2.isJump = True
        else:
            if P2.jumpCount >= -10:
                P2.Y -= (P2.jumpCount * abs(P2.jumpCount)) * 0.5
                P2.jumpCount -= 1
            else:
                P2.jumpCount = 10
                P2.isJump = False

        if P2.Attack == True:
            P2.Move = False
            P2.Pos = 0
            P2.Hit = False
            P2.Attack = False

        if P2.Move:
            P2.Pos += 1
            if P2.Sprite == WalkingMovesR:
                P2.X += vel
            else:
                P2.X -= vel
            if P2.Pos == 3:
                P2.Pos = 0
                P2.Move = False

        if P2.Hit == True:
            if P2.First == True:
                P2.Pos = -1
                P2.First = False
            if P2.Facing == 1:
                P2.Sprite = HittingMovesR
            else:
                P2.Sprite = HittingMovesL
            P2.Pos += 1
            if P2.Pos == 3:
                P2.Pos = 0
                P2.Hit = False
                if P2.Facing == 1:
                    P2.Sprite = WalkingMovesR
                else:
                    P2.Sprite = WalkingMovesL

        if P2.DashCooldown > 0:
            P2.DashCooldown -= 1

        if P2.HitCooldown > 0:
            P2.HitCooldown -= 1

        if P2.Dash == True:
            if P2.First == True:
                P2.Pos = -1
                P2.First = False
            if P2.Facing == 1:
                P2.Sprite = DashR
            else:
                P2.Sprite = DashL
            P2.Pos += 1
            if P2.Pos < 2:
                if P2.Facing == 1:
                    if P2.X < 680:
                        P2.X += 120
                else:
                    if P2.X > 120:
                        P2.X -= 120
            if P2.Pos == 6:
                P2.Pos = 0
                P2.Dash = False
                if P2.Facing == 1:
                    P2.Sprite = WalkingMovesR
                else:
                    P2.Sprite = WalkingMovesL

        if P1.HP <= 0 or P2.HP <= 0:
            if P1.HP <= 0:
                winner = "P2"
            else:
                winner = "P1"
            # ================= LEADERBOARD DATA =================
            Leaderboardscore = open('SaveData/LeaderBoardScore', 'r+')
            Leaderboardscore.truncate(0)
            Leaderboardscore.close()

            if P1.HP <= 0:
                NamePos = NameSave.index(P2NAME)
                ScoreSave[NamePos] = ScoreSave[NamePos] + 1
            else:
                NamePos = NameSave.index(P1NAME)
                ScoreSave[NamePos] = ScoreSave[NamePos] + 1

            Leaderboardscore = open('SaveData/LeaderBoardScore', 'r+')
            for i in range(0, len(ScoreSave)):
                Leaderboardscore.writelines(str(ScoreSave[i]) + "\n")

            Leaderboardscore.close()
            # =====================================================
            run = False
            endgame = True
            drawing()
            pygame.time.delay(1000)

        drawing()