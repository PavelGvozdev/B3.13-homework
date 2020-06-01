#B3.13-homework.py 

class Tag:

    def __init__(self, name, is_single=False, klass=None, text=None, **kwargs):
        self.name = name
        self.is_single = is_single
        self.text = text
        self.kwargs = kwargs
        self.nested = []
        self.klass = klass

    def __add__(self, other):
        self.nested.append(other)
        return self

    def render(self):
        
        if self.name == 'div':
            rendered_text = f'    <{self.name}'
        elif self.name == 'h1':
            rendered_text = f'    <{self.name}'
        else:
            rendered_text = f'      <{self.name}'

        if self.klass:
            rendered_text += f' class="{self.klass}"'

        if self.kwargs:
            rendered_text += ' ' + ' '.join(f'{k}="{v}"' for k, v in self.kwargs.items())

        if not self.is_single and self.name == 'div':
            rendered_text += '>\n'
        elif not self.is_single:
            rendered_text += '>'

        if self.text:
            rendered_text += self.text

        if self.nested:
            rendered_text += ''.join(tag.render() for tag in self.nested)

        if self.is_single:
            return rendered_text + f'/>\n'
        elif self.name == 'div':
            return rendered_text + f'    </{self.name}>\n'
        else:
            return rendered_text + f'</{self.name}>\n'    

class TopLevelTag:
    def __init__(self, name, **kwargs):
        self.name = name
        self.kwargs = kwargs
        self.nested = []

    def __add__(self, other):
        self.nested.append(other)
        return self

    def render(self):
        rendered_text = f'\n  <{self.name}'

        if self.kwargs:
            rendered_text += ' ' + ' '.join(f'{k}="{v}"' for k, v in self.kwargs.items())

        rendered_text += '>\n'
        
        if self.nested:
            rendered_text += ''.join(tag.render() for tag in self.nested)

        return rendered_text + f'  </{self.name}>'    

class HTML:
    def __init__(self, name, **kwargs):
        self.name = name
        self.kwargs = kwargs
        self.nested = []

    def __add__(self, other):
        self.nested.append(other)
        return self

    def render(self):
        rendered_text = f'<{self.name}'

        if self.kwargs:
            rendered_text += ' ' + ' '.join(f'{k}="{v}"' for k, v in self.kwargs.items())

        rendered_text += '>'

        if self.nested:
            rendered_text += ''.join(tag.render() for tag in self.nested)

        return rendered_text + f'\n</{self.name}>'    

context = (
    HTML('html') + 
        (TopLevelTag('head') + Tag('title', is_single=False, text='hello'))
        +
        (TopLevelTag('body') +
            Tag('h1', is_single=False, text='Test', klass='main-text')
            +
            (Tag('div', is_single=False, klass='container container-fluid', id='lead') +
                Tag('p', is_single=False, text='another test')
                +
                Tag('img', is_single=True, src='/icon.png', data_image='responsive'))) 
)
print(context.render())
