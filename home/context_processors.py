import datetime

def data(request) -> dict[any] | dict[str, str]:
    context = {
        'name': 'Daniel Brown',
        'email': 'daniel_profissional1998@hotmail.com',
        'phone': '21 9 76788321',
        'linkedin': 'www.linkedin.com/in/daniel-brown-04693b25b',
        'github': 'https://github.com/DanielBrown1998',
        'year': datetime.datetime.now().year,
        'bio': 'Sou estudante de Ciência da Computação na Universidade do Estado do Rio de Janeiro,\n'
        'desde muito jovem fui aficionado por tecnologia, e na programação pude encontrar-me na vida.\n'
        'Hoje, busco minha primeira oportunidade profissional; seja em Web, seja em Mobile.\n'
        'Eu apenas quero construir softwares e traduzi-los à realidade.'
    }
    return context
