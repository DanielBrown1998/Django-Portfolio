from django.shortcuts import render


def home(request):
    return render(request, 'home/home.html')

def projects(request):
    context = {
        'projects': [
            {
                'name': 'Projeto 1',
                'description': 'Descrição do projeto 1',
                'link_github': 'localhost:8000',  
                'imagem': 'imagem/django.svg', 
            },
            {
                'name': 'Projeto 2',
                'description': 'Descrição do projeto 2',
                'link_github': 'localhost:8000',
                'imagem': 'imagem/django.svg', 

            },
            {
                'name': 'Projeto 3',
                'description': 'Descrição do projeto 3',
                'link_github': 'localhost:8000',
                'imagem': 'imagem/django.svg', 

            },
            {
                'name': 'Projeto 3',
                'description': 'Descrição do projeto 3',
                'link_github': 'localhost:8000',
                'imagem': 'imagem/django.svg', 

            },
            {
                'name': 'Projeto 3',
                'description': 'Descrição do projeto 3',
                'link_github': 'localhost:8000',
                'imagem': 'imagem/django.svg', 

            },
            {
                'name': 'Projeto 3',
                'description': 'Descrição do projeto 3',
                'link_github': 'localhost:8000',
                'imagem': 'imagem/django.svg', 

            },
        ]
    }
    return render(request, 'projects/projects.html', context=context)


def card(request, id:int):
    #TODO
    ...
