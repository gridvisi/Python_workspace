import pygame
import math
from visual import *
'''按钮类'''
class Button(pygame.sprite.Sprite):
    def __init__(self, screen, x, y, width, height, action=None, color_not_active=(189, 195, 199), color_active=(189, 195, 199)):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.action = action
        self.screen = screen
        self.color_active = color_active
        self.color_not_active = color_not_active
    '''添加文字'''
    def addtext(self, text, size=20, font='Times New Roman', color=(0, 0, 0)):
        self.font = pygame.font.Font(font, size)
        self.text = self.font.render(text, True, color)
        self.text_pos = self.text.get_rect()
        self.text_pos.center = (self.x + self.width / 2, self.y + self.height / 2)
    '''是否被鼠标选中'''
    def selected(self):
        pos = pygame.mouse.get_pos()
        if (self.x < pos[0] < self.x + self.width) and (self.y < pos[1] < self.y + self.height):
            return True
        return False
    '''画到屏幕上'''
    def draw(self):
        if self.selected():
            pygame.draw.rect(self.screen, self.color_active, (self.x, self.y, self.width, self.height))
        else:
            pygame.draw.rect(self.screen, self.color_not_active, (self.x, self.y, self.width, self.height))
        if hasattr(self, 'text'):
            self.screen.blit(self.text, self.text_pos)


'''文字标签类'''
class Label(pygame.sprite.Sprite):
    def __init__(self, screen, x, y, width, height):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.screen = screen
    '''添加文字'''
    def addtext(self, text, size=20, font='Times New Roman', color=(0, 0, 0)):
        self.font = pygame.font.Font(font, size)
        self.text = self.font.render(text, True, color)
        self.text_pos = self.text.get_rect()
        self.text_pos.center = (self.x + self.width / 2, self.y + self.height / 2)
    '''画到屏幕上'''
    def draw(self):
        if hasattr(self, 'text'):
            self.screen.blit(self.text, self.text_pos)


def quitgame():
    pygame.quit()
    sys.exit()
#若点击开始游戏按钮，则开始游戏：

def startgame():
    game_levels = GameLevels(cfg, screen)
    game_levels.start()


'''小鸟'''
class Bird(pygame.sprite.Sprite):
    def __init__(self, screen, imagepaths, loc_info, velocity=None, color=(255, 255, 255), **kwargs):
        pygame.sprite.Sprite.__init__(self)
        assert len(loc_info) == 3
        assert len(imagepaths) == 1
        # 设置必要的属性常量
        self.color = color
        self.screen = screen
        self.loc_info = list(loc_info)
        self.imagepaths = imagepaths
        self.velocity = VelocityVector() if velocity is None else velocity
        self.type = 'bird'
        self.fly_path = []
        self.is_dead = False
        self.elasticity = 0.8
        self.is_loaded = False
        self.is_selected = False
        self.inverse_friction = 0.99
        self.gravity = VelocityVector(0.2, math.pi)
        # 屏幕大小
        self.screen_size = screen.get_rect().size
        self.screen_size = (self.screen_size[0], self.screen_size[1] - 50)
        # 导入图像
        self.image = pygame.image.load(imagepaths[0])
    '''画到屏幕上'''
    def draw(self):
        if not self.is_loaded:
            for point in self.fly_path:
                pygame.draw.ellipse(self.screen, self.color, (point[0], point[1], 3, 3), 1)
        position = self.loc_info[0] - self.loc_info[2], self.loc_info[1] - self.loc_info[2]
        self.screen.blit(self.image, position)
    '''判断有没有被鼠标选中'''
    def selected(self):
        pos = pygame.mouse.get_pos()
        dx, dy = pos[0] - self.loc_info[0], pos[1] - self.loc_info[1]
        dist = math.hypot(dy, dx)
        if dist < self.loc_info[2]:
            return True
        return False
    '''加载到弹弓上'''
    def load(self, slingshot):
        self.loc_info[0], self.loc_info[1] = slingshot.x, slingshot.y
        self.is_loaded = True
    '''重新设置位置'''
    def reposition(self, slingshot):
        pos = pygame.mouse.get_pos()
        if self.selected:
            self.loc_info[0], self.loc_info[1] = pos[0], pos[1]
            dx, dy = slingshot.x - self.loc_info[0], slingshot.y - self.loc_info[1]
            self.velocity.magnitude = min(int(math.hypot(dx, dy) / 2), 80)
            self.velocity.angle = math.pi / 2 + math.atan2(dy, dx)
    '''显示发射小鸟的路径'''
    def projectpath(self):
        if self.is_loaded:
            path = []
            bird = Bird(self.screen, self.imagepaths, self.loc_info, velocity=self.velocity)
            for i in range(30):
                bird.move()
                if i % 5 == 0: path.append((bird.loc_info[0], bird.loc_info[1]))
            for point in path:
                pygame.draw.ellipse(self.screen, self.color, (point[0], point[1], 2, 2))
    '''移动小鸟'''
    def move(self):
        # 根据重力改变小鸟的速度向量
        self.velocity = VectorAddition(self.velocity, self.gravity)
        self.loc_info[0] += self.velocity.magnitude * math.sin(self.velocity.angle)
        self.loc_info[1] -= self.velocity.magnitude * math.cos(self.velocity.angle)
        self.velocity.magnitude *= self.inverse_friction
        # 宽度超出屏幕
        if self.loc_info[0] > self.screen_size[0] - self.loc_info[2]:
            self.loc_info[0] = 2 * (self.screen_size[0] - self.loc_info[2]) - self.loc_info[0]
            self.velocity.angle *= -1
            self.velocity.magnitude *= self.elasticity
        elif self.loc_info[0] < self.loc_info[2]:
            self.loc_info[0] = 2 * self.loc_info[2] - self.loc_info[0]
            self.velocity.angle *= -1
            self.velocity.magnitude *= self.elasticity
        # 高度超出屏幕
        if self.loc_info[1] > self.screen_size[1] - self.loc_info[2]:
            self.loc_info[1] = 2 * (self.screen_size[1] - self.loc_info[2]) - self.loc_info[1]
            self.velocity.angle = math.pi - self.velocity.angle
            self.velocity.magnitude *= self.elasticity
        elif self.loc_info[1] < self.loc_info[2]:
            self.loc_info[1] = 2 * self.loc_info[2] - self.loc_info[1]
            self.velocity.angle = math.pi - self.velocity.angle
            self.velocity.magnitude *= self.elasticity

'''猪'''
class Pig(pygame.sprite.Sprite):
    def __init__(self, screen, imagepaths, loc_info, velocity=None, **kwargs):
        pygame.sprite.Sprite.__init__(self)
        assert len(loc_info) == 3
        assert len(imagepaths) == 3
        # 设置必要的属性常量
        self.screen = screen
        self.loc_info = list(loc_info)
        self.imagepaths = imagepaths
        self.velocity = VelocityVector() if velocity is None else velocity
        self.type = 'pig'
        self.is_dead = False
        self.elasticity = 0.8
        self.switch_freq = 20
        self.animate_count = 0
        self.inverse_friction = 0.99
        self.gravity = VelocityVector(0.2, math.pi)
        # 屏幕大小
        self.screen_size = screen.get_rect().size
        self.screen_size = (self.screen_size[0], self.screen_size[1] - 50)
        # 导入图像
        self.pig_images = []
        for imagepath in imagepaths: self.pig_images.append(pygame.image.load(imagepath))
        # 设置当前图像
        self.image = random.choice(self.pig_images[:2])
    '''画到屏幕上'''
    def draw(self):
        self.animate_count += 1
        if (self.animate_count % self.switch_freq == 0) and (not self.is_dead):
            self.animate_count = 0
            self.image = random.choice(self.pig_images[:2])
        position = self.loc_info[0] - self.loc_info[2], self.loc_info[1] - self.loc_info[2]
        self.screen.blit(self.image, position)
    '''移动猪'''
    def move(self):
        # 根据重力改变猪的速度向量
        self.velocity = VectorAddition(self.velocity, self.gravity)
        self.loc_info[0] += self.velocity.magnitude * math.sin(self.velocity.angle)
        self.loc_info[1] -= self.velocity.magnitude * math.cos(self.velocity.angle)
        self.velocity.magnitude *= self.inverse_friction
        # 宽度超出屏幕
        if self.loc_info[0] > self.screen_size[0] - self.loc_info[2]:
            self.loc_info[0] = 2 * (self.screen_size[0] - self.loc_info[2]) - self.loc_info[0]
            self.velocity.angle *= -1
            self.velocity.magnitude *= self.elasticity
        elif self.loc_info[0] < self.loc_info[2]:
            self.loc_info[0] = 2 * self.loc_info[2] - self.loc_info[0]
            self.velocity.angle *= -1
            self.velocity.magnitude *= self.elasticity
        # 高度超出屏幕
        if self.loc_info[1] > self.screen_size[1] - self.loc_info[2]:
            self.loc_info[1] = 2 * (self.screen_size[1] - self.loc_info[2]) - self.loc_info[1]
            self.velocity.angle = math.pi - self.velocity.angle
            self.velocity.magnitude *= self.elasticity
        elif self.loc_info[1] < self.loc_info[2]:
            self.loc_info[1] = 2 * self.loc_info[2] - self.loc_info[1]
            self.velocity.angle = math.pi - self.velocity.angle
            self.velocity.magnitude *= self.elasticity
    '''猪死掉了'''
    def setdead(self):
        self.is_dead = True
        self.image = self.pig_images[-1]


'''地图里的木块'''
class Block(pygame.sprite.Sprite):
    def __init__(self, screen, imagepaths, loc_info, velocity=None, **kwargs):
        pygame.sprite.Sprite.__init__(self)
        assert len(loc_info) == 3
        assert len(imagepaths) == 2
        # 设置必要的属性常量
        self.type = 'block'
        self.screen = screen
        self.loc_info = list(loc_info)
        self.imagepaths = imagepaths
        self.velocity = VelocityVector() if velocity is None else velocity
        self.elasticity = 0.7
        self.is_destroyed = False
        self.inverse_friction = 0.99
        self.gravity = VelocityVector(0.2, math.pi)
        # 导入图像
        self.block_images = []
        for imagepath in imagepaths: self.block_images.append(pygame.transform.scale(pygame.image.load(imagepath), (100, 100)))
        # 屏幕大小
        self.screen_size = screen.get_rect().size
        self.screen_size = (self.screen_size[0], self.screen_size[1] - 50)
        # 设置当前图像
        self.image = self.block_images[0]
        self.rect = self.image.get_rect()
        self.rotate_angle = math.radians(0)
    '''画到屏幕上'''
    def draw(self):
        pygame.transform.rotate(self.image, self.rotate_angle)
        self.screen.blit(self.image, (self.loc_info[0] - self.rect.width // 2, self.loc_info[1]))
    '''设置为损坏状态'''
    def setdestroy(self):
        self.is_destroyed = True
        self.image = self.block_images[1]
    '''移动木块'''
    def move(self):
        # 根据重力改变木块的速度向量
        self.velocity = VectorAddition(self.velocity, self.gravity)
        self.loc_info[0] += self.velocity.magnitude * math.sin(self.velocity.angle)
        self.loc_info[1] -= self.velocity.magnitude * math.cos(self.velocity.angle)
        self.velocity.magnitude *= self.inverse_friction
        # 宽度超出屏幕
        if self.loc_info[0] > self.screen_size[0] - self.rect.width:
            self.loc_info[0] = 2 * (self.screen_size[0] - self.rect.width) - self.loc_info[0]
            self.velocity.angle *= -1
            self.rotate_angle = -self.velocity.angle
            self.velocity.magnitude *= self.elasticity
        elif self.loc_info[0] < self.rect.width:
            self.loc_info[0] = 2 * self.rect.width - self.loc_info[0]
            self.velocity.angle *= -1
            self.rotate_angle = -self.velocity.angle
            self.velocity.magnitude *= self.elasticity
        # 高度超出屏幕
        if self.loc_info[1] > self.screen_size[1] - self.rect.height:
            self.loc_info[1] = 2 * (self.screen_size[1] - self.rect.height) - self.loc_info[1]
            self.velocity.angle = math.pi - self.velocity.angle
            self.rotate_angle = math.pi - self.velocity.angle
            self.velocity.magnitude *= self.elasticity
        elif self.loc_info[1] < self.rect.height:
            self.loc_info[1] = 2 * self.rect.height - self.loc_info[1]
            self.velocity.angle = math.pi - self.velocity.angle
            self.rotate_angle = math.pi - self.velocity.angle
            self.velocity.magnitude *= self.elasticity


'''弹弓'''
class Slingshot(pygame.sprite.Sprite):
    def __init__(self, screen, x, y, width, height, color=(66, 73, 73), line_color=(100, 30, 22), **kwargs):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.color = color
        self.width = width
        self.height = height
        self.screen = screen
        self.line_color = line_color
        self.type = 'slingshot'
    '''画到屏幕上'''
    def draw(self, bird=None):
        pygame.draw.rect(self.screen, self.color, (self.x, self.y + self.height * 1 / 3, self.width, self.height * 2 / 3))
        if bird is not None and bird.is_loaded:
            pygame.draw.line(self.screen, self.line_color, (self.x, self.y + self.height / 6), (bird.loc_info[0], bird.loc_info[1] + bird.loc_info[2] / 2), 10)
            pygame.draw.line(self.screen, self.line_color, (self.x + self.width, self.y + self.height / 6), (bird.loc_info[0] + bird.loc_info[2], bird.loc_info[1] + bird.loc_info[2] / 2), 10)
        pygame.draw.rect(self.screen, self.color, (self.x - self.width / 4, self.y, self.width / 2, self.height / 3), 5)
        pygame.draw.rect(self.screen, self.color, (self.x + self.width * 3 / 4, self.y, self.width / 2, self.height / 3), 5)


'''墙'''
class Slab(pygame.sprite.Sprite):
    def __init__(self, screen, imagepaths, x, y, width, height, color=(255, 255, 255)):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.color = color
        self.width = width
        self.height = height
        self.screen = screen
        self.imagepaths = imagepaths
        if self.width > self.height:
            self.image = pygame.image.load(self.imagepaths[0])
        else:
            self.image = pygame.image.load(self.imagepaths[1])
        self.image = pygame.transform.scale(self.image, (self.width, self.height))
        self.type = 'wall'
    '''画到屏幕上'''
    def draw(self):
        self.screen.blit(self.image, (self.x, self.y))


'''开始游戏'''
def start(self):
    # 导入所有游戏精灵
    game_sprites = self.loadlevelmap()
    birds, pigs, blocks, walls = game_sprites['birds'], game_sprites['pigs'], game_sprites['blocks'], game_sprites['walls']
    slingshot = Slingshot(self.screen, 200, self.screen_size[1] - 200, 30, 200)
    birds[0].load(slingshot)
    score_label = Label(self.screen, 50, 10, 100, 50)
    score_label.addtext(f'SCORE: {self.score}', 25, self.cfg.FONTPATH['Comic_Kings'], (236, 240, 241))
    birds_remaining_label = Label(self.screen, 120, 50, 100, 50)
    birds_remaining_label.addtext(f"BIRDS REMAINING: {len(birds)}", 25, self.cfg.FONTPATH['Comic_Kings'], (236, 240, 241))
    pigs_remaining_label = Label(self.screen, 110, 90, 100, 50)
    pigs_remaining_label.addtext(f"PIGS REMAINING: {len(pigs)}", 25, self.cfg.FONTPATH['Comic_Kings'], (236, 240, 241))
    carles_label = Label(self.screen, self.screen_size[0] - 270, self.screen_size[1] - 20, 300, 100)
    carles_label.addtext('CARLES', 60, self.cfg.FONTPATH['arfmoochikncheez'], (113, 125, 126))
    # 游戏主循环
    clock = pygame.time.Clock()
    blocks_to_remove, pigs_to_remove = [], []
    while True:
        # --按键检测
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quitgame()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    self.quitgame()
                elif event.key == pygame.K_r:
                    self.start()
                elif event.key == pygame.K_p or event.key == pygame.K_ESCAPE:
                    self.pauseinterface()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if birds[0].selected():
                    birds[0].is_selected = True
            elif event.type == pygame.MOUSEBUTTONUP:
                if birds[0].is_selected:
                    birds[0].is_selected = False
                    birds[0].start_flying = True
        # --背景颜色填充
        color = self.cfg.BACKGROUND_COLOR
        for i in range(3):
            color = (color[0] + 5, color[1] + 5, color[2] + 5)
            pygame.draw.rect(self.screen, color, (0, i * 300, self.screen_size[0], 300))
        pygame.draw.rect(self.screen, (77, 86, 86), (0, self.screen_size[1], self.screen_size[0], 50))
        # --判断游戏是否结束，若没有则导入新的小鸟
        if (not birds[0].is_loaded) and self.still(pigs + birds + blocks):
            birds.pop(0)
            if self.status(pigs, birds) == 2:
                self.score += len(birds) * 100
                self.switchlevelinterface()
            elif self.status(pigs, birds) == 1:
                self.failureinterface()
            birds[0].load(slingshot)
            birds[0].start_flying = False
        # --重置小鸟的位置
        if birds[0].is_selected:
            birds[0].reposition(slingshot)
        if hasattr(birds[0], 'start_flying') and birds[0].start_flying:
            birds[0].is_loaded = False
        # --弹弓
        slingshot.draw(birds[0])
        # --判断猪是否撞上木桩
        for i in range(len(pigs)):
            for j in range(len(blocks)):
                pig_magnitude_1, block_magnitude_1 = pigs[i].velocity.magnitude, blocks[j].velocity.magnitude
                pigs[i], blocks[j], is_collision = self.collision(pigs[i], blocks[j])
                pig_magnitude_2, block_magnitude_2 = pigs[i].velocity.magnitude, blocks[j].velocity.magnitude
                if is_collision:
                    if abs(pig_magnitude_2 - pig_magnitude_2) > 2:
                        blocks_to_remove.append(blocks[j])
                        blocks[j].setdestroy()
                    if abs(block_magnitude_2 - block_magnitude_1) > 2:
                        pigs_to_remove.append(pigs[i])
                        pigs[i].setdead()
        # --判断鸟是否撞上木桩
        for i in range(len(birds)):
            if not (birds[i].is_loaded or birds[i].velocity.magnitude == 0):
                for j in range(len(blocks)):
                    bird_magnitude_1, block_magnitude_1 = birds[i].velocity.magnitude, blocks[j].velocity.magnitude
                    birds[i], blocks[j], is_collision = self.collision(birds[i], blocks[j])
                    bird_magnitude_2, block_magnitude_2 = birds[i].velocity.magnitude, blocks[j].velocity.magnitude
                    if is_collision:
                        if abs(bird_magnitude_1 - bird_magnitude_2) > 2:
                            if blocks[j] not in blocks_to_remove:
                                blocks_to_remove.append(blocks[j])
                                blocks[j].setdestroy()
        # --判断猪是否撞上猪或者猪撞墙
        for i in range(len(pigs)):
            pigs[i].move()
            for j in range(i+1, len(pigs)):
                pig1_magnitude_1, pig2_magnitude_1 = pigs[i].velocity.magnitude, pigs[j].velocity.magnitude
                pigs[i], pigs[j], is_collision = self.collision(pigs[i], pigs[j])
                pig1_magnitude_2, pig2_magnitude_2 = pigs[i].velocity.magnitude, pigs[j].velocity.magnitude
                if abs(pig1_magnitude_1 - pig1_magnitude_2) > 2:
                    if pigs[j] not in pigs_to_remove:
                        pigs_to_remove.append(pigs[j])
                        pigs[j].setdead()
                if abs(pig2_magnitude_1 - pig2_magnitude_2) > 2:
                    if pigs[i] not in pigs_to_remove:
                        pigs_to_remove.append(pigs[i])
                        pigs[i].setdead()
            for wall in walls: pigs[i] = self.collision(pigs[i], wall)[0]
            pigs[i].draw()
        # --判断鸟是否撞到猪或者鸟是否撞到墙
        for i in range(len(birds)):
            if (not birds[i].is_loaded) and (birds[i].velocity.magnitude):
                birds[i].move()
                for j in range(len(pigs)):
                    bird_magnitude_1, pig_magnitude_1 = birds[i].velocity.magnitude, pigs[j].velocity.magnitude
                    birds[i], pigs[j], is_collision = self.collision(birds[i], pigs[j])
                    bird_magnitude_2, pig_magnitude_2 = birds[i].velocity.magnitude, pigs[j].velocity.magnitude
                    if is_collision:
                        if abs(bird_magnitude_2 - bird_magnitude_1) > 2:
                            if pigs[j] not in pigs_to_remove:
                                pigs_to_remove.append(pigs[j])
                                pigs[j].setdead()
            if birds[i].is_loaded: birds[i].projectpath()
            for wall in walls: birds[i] = self.collision(birds[i], wall)[0]
            birds[i].draw()
        # --判断木桩是否撞到了木桩或者木桩撞到墙
        for i in range(len(blocks)):
            for j in range(i+1, len(blocks)):
                block1_magnitude_1, block2_magnitude_1 = blocks[i].velocity.magnitude, blocks[j].velocity.magnitude
                blocks[i], blocks[j], is_collision = self.collision(blocks[i], blocks[j])
                block1_magnitude_2, block2_magnitude_2 = blocks[i].velocity.magnitude, blocks[j].velocity.magnitude
                if is_collision:
                    if abs(block1_magnitude_2 - block1_magnitude_1) > 2:
                        if blocks[j] not in blocks_to_remove:
                            blocks_to_remove.append(blocks[j])
                            blocks[j].setdestroy()
                    if abs(block2_magnitude_2 - block2_magnitude_1) > 2:
                        if blocks[i] not in blocks_to_remove:
                            blocks_to_remove.append(blocks[i])
                            blocks[i].setdestroy()
            blocks[i].move()
            for wall in walls: blocks[i] = self.collision(blocks[i], wall)[0]
            blocks[i].draw()
        # --墙
        for wall in walls: wall.draw()
        # --显示文字
        score_label.addtext(f'SCORE: {self.score}', 25, self.cfg.FONTPATH['Comic_Kings'], (236, 240, 241))
        score_label.draw()
        birds_remaining_label.addtext(f"BIRDS REMAINING: {len(birds)}", 25, self.cfg.FONTPATH['Comic_Kings'], (236, 240, 241))
        birds_remaining_label.draw()
        pigs_remaining_label.addtext(f"PIGS REMAINING: {len(pigs)}", 25, self.cfg.FONTPATH['Comic_Kings'], (236, 240, 241))
        pigs_remaining_label.draw()
        carles_label.draw()
        # --画面刷新
        pygame.display.update()
        clock.tick(self.cfg.FPS)
        # --删除无效的元素
        if self.still(birds + pigs + blocks):
            for pig in pigs_to_remove:
                if pig in pigs:
                    pigs.remove(pig)
                    self.score += 100
            for block in blocks_to_remove:
                if block in blocks:
                    blocks.remove(block)
                    self.score += 50
            pigs_to_remove = []
            blocks_to_remove = []