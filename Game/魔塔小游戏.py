
import pygame
import sys
'''按钮类'''
class Button(pygame.sprite.Sprite):
    def __init__(self, text, fontpath, fontsize, position, color_selected=(255, 0, 0), color_default=(255, 255, 255)):
        pygame.sprite.Sprite.__init__(self)
        self.text = text
        self.color_selected = color_selected
        self.color_default = color_default
        self.font = pygame.font.Font(fontpath, fontsize)
        self.font_render = self.font.render(text, True, color_default)
        self.rect = self.font_render.get_rect()
        self.rect.center = position
    '''更新函数: 不断地更新检测鼠标是否在按钮上'''
    def update(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(mouse_pos):
            self.font_render = self.font.render(self.text, True, self.color_selected)
        else:
            self.font_render = self.font.render(self.text, True, self.color_default)
    '''绑定到屏幕上'''
    def draw(self, screen):
        screen.blit(self.font_render, self.rect)



'''游戏开始界面'''
class StartGameInterface():
    def __init__(self, cfg):
        self.cfg = cfg
        self.play_btn = Button('开始游戏', cfg.FONTPATH_CN, 50, (cfg.SCREENSIZE[0]//2, cfg.SCREENSIZE[1] - 400))
        self.intro_btn = Button('游戏说明', cfg.FONTPATH_CN, 50, (cfg.SCREENSIZE[0]//2, cfg.SCREENSIZE[1] - 300))
        self.quit_btn = Button('离开游戏', cfg.FONTPATH_CN, 50, (cfg.SCREENSIZE[0]//2, cfg.SCREENSIZE[1] - 200))
    '''外部调用'''
    def run(self, screen):
        # 魔塔
        font = pygame.font.Font(self.cfg.FONTPATH_CN, 80)
        font_render_cn = font.render('魔塔', True, (255, 255, 255))
        rect_cn = font_render_cn.get_rect()
        rect_cn.center = self.cfg.SCREENSIZE[0] // 2, 200
        # Magic Tower
        font = pygame.font.Font(self.cfg.FONTPATH_EN, 80)
        font_render_en = font.render('Magic Tower', True, (255, 255, 255))
        rect_en = font_render_en.get_rect()
        rect_en.center = self.cfg.SCREENSIZE[0] // 2, 350
        # (Ver 1.12)
        font = pygame.font.Font(self.cfg.FONTPATH_CN, 40)
        font_render_version = font.render('(Ver 1.12)', True, (255, 255, 255))
        rect_ver = font_render_version.get_rect()
        rect_ver.center = self.cfg.SCREENSIZE[0] // 2, 400
        clock = pygame.time.Clock()
        while True:
            screen.fill((0, 0, 0))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit(0)
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        mouse_pos = pygame.mouse.get_pos()
                        if self.play_btn.rect.collidepoint(mouse_pos):
                            return True
                        elif self.quit_btn.rect.collidepoint(mouse_pos):
                            pygame.quit()
                            sys.exit(0)
                        elif self.intro_btn.rect.collidepoint(mouse_pos):
                            self.showgameintro(screen)
            for btn in [self.intro_btn, self.play_btn, self.quit_btn]:
                btn.update()
                btn.draw(screen)
            for fr, rect in zip([font_render_cn, font_render_en, font_render_version], [rect_cn, rect_en, rect_ver]):
                screen.blit(fr, rect)
            pygame.display.flip()
            clock.tick(self.cfg.FPS)
    '''显示游戏简介'''
    def showgameintro(self, screen):
        font = pygame.font.Font(self.cfg.FONTPATH_CN, 20)
        font_renders = [
            font.render('魔塔小游戏.', True, (255, 255, 255)),
            font.render('游戏素材来自: http://www.4399.com/flash/1749_1.htm.', True, (255, 255, 255)),
            font.render('游戏背景故事为公主被大魔王抓走, 需要勇士前往魔塔将其救出.', True, (255, 255, 255)),
            font.render('python工程狮.', True, (255, 255, 255)),
            font.render('微信公众号: python工程狮.', True, (255, 255, 255)),
            font.render('版权所有.', True, (255, 255, 255)),
        ]
        rects = [fr.get_rect() for fr in font_renders]
        for idx, rect in enumerate(rects):
            rect.center = self.cfg.SCREENSIZE[0] // 2, 50 * idx + 100
        clock = pygame.time.Clock()
        while True:
            screen.fill((0, 0, 0))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit(0)
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        mouse_pos = pygame.mouse.get_pos()
                        if self.play_btn.rect.collidepoint(mouse_pos):
                            return True
                        elif self.quit_btn.rect.collidepoint(mouse_pos):
                            pygame.quit()
                            sys.exit(0)
                        elif self.intro_btn.rect.collidepoint(mouse_pos):
                            return
            for btn in [self.intro_btn, self.play_btn, self.quit_btn]:
                btn.update()
                btn.draw(screen)
            for fr, rect in zip(font_renders, rects):
                screen.blit(fr, rect)
            pygame.display.flip()
            clock.tick(self.cfg.FPS)

'''游戏地图解析类'''
class MapParser():
    def __init__(self, blocksize, filepath, element_images, offset=(0, 0), **kwargs):
        self.count = 0
        self.switch_times = 15
        self.image_pointer = 0
        self.offset = offset
        self.blocksize = blocksize
        self.element_images = element_images
        self.map_matrix = self.parse(filepath)
    '''解析'''
    def parse(self, filepath):
        map_matrix = []
        with open(filepath, 'r') as fp:
            for line in fp.readlines():
                line = line.strip()
                if not line: continue
                map_matrix.append([c.strip() for c in line.split(',')])
        return map_matrix
    '''将游戏地图画到屏幕上'''
    def draw(self, screen):
        self.count += 1
        if self.count == self.switch_times:
            self.count = 0
            self.image_pointer = int(not self.image_pointer)
        for row_idx, row in enumerate(self.map_matrix):
            for col_idx, elem in enumerate(row):
                position = col_idx * self.blocksize + self.offset[0], row_idx * self.blocksize + self.offset[1]
                if elem+'.png' in self.element_images:
                    image = self.element_images[elem+'.png'][self.image_pointer]
                    image = pygame.transform.scale(image, (self.blocksize, self.blocksize))
                    screen.blit(image, position)