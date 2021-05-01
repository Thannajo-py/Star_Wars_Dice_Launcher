import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.pagelayout import PageLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.image import Image
from kivy.uix.widget import Widget
from kivy.graphics import Rectangle, Color
from random import randint


BLUE_DICE = [({}, 'blue_0.png'), ({}, 'blue_0.png'), ({'success': 1}, 'blue_1_s.png'),
             ({'success': 1, 'advantage': 1}, 'blue_1_s_1_a.png'), ({'advantage': 2}, 'blue_2_a.png'),
             ({'advantage': 1}, 'blue_1_a.png')]

BLACK_DICE = [({}, 'black_0.png'), ({}, 'black_0.png'), ({'failure': 1}, 'black_1_f.png'),
              ({'failure': 1}, 'black_1_f.png'), ({'threat': 1}, 'black_1_t.png'), ({'threat': 1}, 'black_1_t.png')]

GREEN_DICE = [({}, 'green_0.png'), ({'success': 1}, 'green_1_s.png'), ({'success': 1}, 'green_1_s.png'),
              ({'success': 2}, 'green_2_s.png'), ({'advantage': 1}, 'green_1_a.png'),
              ({'advantage': 1}, 'green_1_a.png'), ({'advantage': 1, 'success': 1}, 'green_1_s_1_a.png'),
              ({'advantage': 2}, 'green_2_a.png')]

PURPLE_DICE = [({}, 'purple_0.png'), ({'failure': 1}, 'purple_1_f.png'), ({'failure': 2}, 'purple_2_f.png'),
               ({'threat': 1}, 'purple_1_t.png'), ({'threat': 1}, 'purple_1_t.png'),({'threat': 1}, 'purple_1_t.png'),
               ({'threat': 2}, 'purple_2_t.png'), ({'threat': 1, 'failure': 1}, 'purple_1_f.png')]

YELLOW_DICE = [({}, 'yellow_0.png'), ({'success': 1}, 'yellow_1_s.png'), ({'success': 1}, 'yellow_1_s.png'),
               ({'success': 2}, 'yellow_2_s.png'), ({'success': 2}, 'yellow_2_s.png'),
               ({'advantage': 1}, 'yellow_1_a.png'), ({'success': 1, 'advantage': 1}, 'yellow_1_s_1_a.png'),
               ({'success': 1, 'advantage': 1}, 'yellow_1_s_1_a.png'),
               ({'success': 1, 'advantage': 1}, 'yellow_1_s_1_a.png'), ({'advantage': 2}, 'yellow_2_a.png'),
               ({'advantage': 2}, 'yellow_2_a.png'), ({'triumph': 1}, 'yellow_1_t.png')]

RED_DICE = [({}, 'red_0.png'), ({'failure': 1}, 'red_1_f.png'), ({'failure': 1}, 'red_1_f.png'),
            ({'failure': 2}, 'red_2_f.png'), ({'failure': 2}, 'red_2_f.png'), ({'threat': 1}, 'red_1_t.png'),
            ({'threat': 1}, 'red_1_t.png'), ({'threat': 1, 'failure': 1}, 'red_1_f_1_t.png'),
            ({'threat': 1, 'failure': 1}, 'red_1_f_1_t.png'), ({'threat': 2}, 'red_2_t.png'),
            ({'threat': 2}, 'red_2_t.png'), ({'disaster': 1}, 'red_1_d.png')]

WHITE_DICE = [({'black': 1}, 'black_1.png'), ({'black': 1}, 'black_1.png'), ({'black': 1}, 'black_1.png'),
              ({'black': 1}, 'black_1.png'), ({'black': 1}, 'black_1.png'), ({'black': 1}, 'black_1.png'),
              ({'black': 2}, 'black_2.png'), ({'white': 1}, 'white_1.png'), ({'white': 1}, 'white_1.png'),
              ({'white': 2}, 'white_2.png'), ({'white': 2}, 'white_2.png'), ({'white': 2}, 'white_2.png')]


class DicePool:
    def __init__(self):
        self.green = Label(text='0')
        self.yellow = Label(text='0')
        self.blue = Label(text='0')
        self.white = Label(text='0')
        self.purple = Label(text='0')
        self.red = Label(text='0')
        self.black = Label(text='0')
        self.value = [(self.green, 'vert'), (self.yellow, 'jaune'), (self.blue, 'bleu')]
        self.difficulty_value = [(self.purple, 'violet'),
                      (self.red, 'rouge'), (self.black, 'noir')]
        self.force_value = [(self.white, 'blanc')]
        self.dice_pool = Label(text=self.dice_pool_value(self.value))
        self.difficulty_dice_pool = Label(text=self.dice_pool_value(self.difficulty_value))
        self.force_dice_pool = Label(text=self.dice_pool_value(self.force_value))
        self.exceptional_result = Label(text='')
        self.result = Label(text='')
        self.force_result = Label(text='')

    def dice_pool_value(self, new_pool):
        pool_dice = ''
        for value, color in new_pool:
            if int(value.text) > 0:
                if pool_dice != '':
                    pool_dice += ', '
                if int(value.text) > 1:
                    pool_dice += f'{value.text} {color}s'
                else:
                    pool_dice += f'{value.text} {color}'
        return pool_dice


pool = DicePool()


def refresh(value, arg):
    if arg.text == '-':
        if int(value) > 0:
            value = str(int(value) - 1)
    if arg.text == '+':
        value = str(int(value) + 1)
    return value


def change_value(button):
    if button.dice == 'green':
        pool.green.text = refresh(pool.green.text, button)
    elif button.dice == 'yellow':
        pool.yellow.text = refresh(pool.yellow.text, button)
    elif button.dice == 'blue':
        pool.blue.text = refresh(pool.blue.text, button)
    elif button.dice == 'purple':
        pool.purple.text = refresh(pool.purple.text, button)
    elif button.dice == 'red':
        pool.red.text = refresh(pool.red.text, button)
    elif button.dice == 'black':
        pool.black.text = refresh(pool.black.text, button)
    elif button.dice == 'white':
        pool.white.text = refresh(pool.white.text, button)
    pool.dice_pool.text = DicePool.dice_pool_value(pool, pool.value)
    pool.force_dice_pool.text = DicePool.dice_pool_value(pool, pool.force_value)
    pool.difficulty_dice_pool.text = DicePool.dice_pool_value(pool, pool.difficulty_value)


def color_launch(value, color):
    color_result = []
    face_result = []
    for color_dice in range(value):
        face = randint(0, len(color)-1)
        result, image = color[face]
        color_result.append(result)
        face_result.append(image)
    return color_result, face_result


def show_faces(pool):
    for image in pool:
        for image_space, text_space in root.space_list:
            if image_space.source == 'nothing.png':
                image_space.source = image
                text_space.text = str(pool[image])
                break


def dice_launch(button):
    for image_space, text_space in root.space_list:
        image_space.source = 'nothing.png'
        text_space.text = ''
    pool_result = []
    pool_face_result = {}
    final_result = {'success': 0, 'advantage': 0, 'triumph': 0, 'disaster': 0,  'black': 0, 'white': 0}
    pool_type = [(int(pool.blue.text), BLUE_DICE), (int(pool.green.text), GREEN_DICE),
                 (int(pool.yellow.text), YELLOW_DICE), (int(pool.black.text), BLACK_DICE),
                 (int(pool.purple.text), PURPLE_DICE), (int(pool.red.text), RED_DICE),
                 (int(pool.white.text), WHITE_DICE)]
    white_launch = True
    for dices, color in pool_type[:6]:
        if dices:
            white_launch = False
            break
    for value, color in pool_type:
        numeric_result, image_result = color_launch(value, color)
        pool_result += numeric_result
        for image in image_result:
            if image in pool_face_result:
                pool_face_result[image] += 1
            else:
                pool_face_result[image] = 1

    for face in pool_result:
        if 'success' in face:
            final_result['success'] += face['success']
        if 'failure' in face:
            final_result['success'] -= face['failure']
        if 'advantage' in face:
            final_result['advantage'] += face['advantage']
        if 'threat' in face:
            final_result['advantage'] -= face['threat']
        if 'triumph' in face:
            final_result['triumph'] += face['triumph']
        if 'disaster' in face:
            final_result['disaster'] += face['disaster']
        if 'black' in face:
            final_result['black'] += face['black']
        if 'white' in face:
            final_result['white'] += face['white']

    success = ''
    if not white_launch:
        if final_result['success'] > 0:
            success += f'succès({final_result["success"]})'
        else:
            if final_result['success'] < -1:
                success += f'échecs({-final_result["success"]})'
            else:
                success += f'échec({-final_result["success"]})'
        if final_result['advantage']:
            if final_result['advantage'] > 0:
                if final_result['advantage'] > 1:
                    success += f', avantages({final_result["advantage"]})'
                else:
                    success += f', avantage({final_result["advantage"]})'
            else:
                if final_result['advantage'] < -1:
                    success += f', menaces({-final_result["advantage"]})'
                else:
                    success += f', menace({-final_result["advantage"]})'
    triumph = ''
    if final_result['triumph']:
        if final_result['triumph'] > 1:
            triumph += f'triomphes({final_result["triumph"]})'
        else:
            triumph += f'triomphe({final_result["triumph"]})'
    if final_result['disaster']:
        if triumph != '':
            triumph += ', '
        if final_result['disaster'] > 1:
            triumph += f'désastres({final_result["disaster"]})'
        else:
            triumph += f'désastre({final_result["disaster"]})'

    force_roll = ''
    if final_result['black']:
        if final_result['black'] > 1:
            force_roll += f'points noirs({final_result["black"]})'
        else:
            force_roll += f'point noir({final_result["black"]})'
    if final_result['white']:
        if force_roll != '':
            force_roll += ', '
        if final_result['white'] > 1:
            force_roll += f'points blancs({final_result["white"]})'
        else:
            force_roll += f'point blanc({final_result["white"]})'
    pool.result.text = success
    pool.force_result.text = force_roll
    pool.exceptional_result.text = triumph
    show_faces(pool_face_result)


class Layout(GridLayout):

    def __init__(self,**kwargs):
        # make sure we aren't overriding any important functionality
        super(Layout, self).__init__(**kwargs)
        self.space_list = []
        for widget in range(39):
            image = Image(source='nothing.png')
            self.add_widget(image)
            text = Label(text='')
            self.add_widget(text)
            self.space_list.append((image,text))


root = Layout(cols=6, rows=13)


class StarApp(App):
    def _update_rect(self, instance, value):
        self.rect.pos = instance.pos
        self.rect.size = instance.size

    def build(self):
        self.icon = 'tie.png'
        pages = PageLayout()
        layout = BoxLayout(orientation='vertical')
        source_image = [(pool.green, 'greenDice.png', 'green'), (pool.purple, 'purpleDice.png', 'purple'),
                        (pool.yellow, 'yellowDice.png', 'yellow'), (pool.red, 'redDice.png', 'red'),
                        (pool.blue, 'blueDice.png', 'blue'), (pool.black, 'blackDice.png', 'black'),
                        (pool.white, 'whiteDice.png', 'white')]
        count = 0
        for origin, image, dice_type in source_image:
            if count % 2 == 0:
                line = BoxLayout(orientation='horizontal')
            cell = BoxLayout(orientation='horizontal')
            button = Button(text='-', on_press=change_value)
            button.dice = dice_type
            cell.add_widget(button)
            dice = BoxLayout(orientation='vertical')
            dice.add_widget(Image(source=image))
            dice.add_widget(origin)
            cell.add_widget(dice)
            button = Button(text='+', on_press=change_value)
            button.dice = dice_type
            cell.add_widget(button)
            line.add_widget(cell)
            if count % 2 == 1:
                layout.add_widget(line)
            if count == 6:
                line.add_widget(Button(text='Launch Dices', on_press=dice_launch))
                layout.add_widget(line)
            count += 1
        dice_pool = BoxLayout(orientation='vertical')
        dice_pool.add_widget(Label(text='Votre pool de dés:'))
        dice_pool.add_widget(pool.dice_pool)
        dice_pool.add_widget(pool.difficulty_dice_pool)
        dice_pool.add_widget(pool.force_dice_pool)
        layout.add_widget(dice_pool)
        result = BoxLayout(orientation='vertical')
        result.add_widget(Label(text='Résultat:'))
        result.add_widget(pool.exceptional_result)
        result.add_widget(pool.result)
        result.add_widget(pool.force_result)
        layout.add_widget(result)
        pages.add_widget(layout)
        root.bind(size=self._update_rect, pos=self._update_rect)

        with root.canvas.before:
            Color(0, 0, 0, 1)  # green; colors range from 0-1 not 0-255
            self.rect = Rectangle(size=root.size, pos=root.pos)
        pages.add_widget(root)
        return pages


if __name__ == '__main__':
    StarApp().run()
