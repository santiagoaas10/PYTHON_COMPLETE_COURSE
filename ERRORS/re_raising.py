class User:
    def __init__(self, name, engagement):
        self.name = name
        self.engagement_metrics = engagement
        self.valor = 0
    def __repr__(self):
        return f'User {self.name}'
    

def get_user_score(usuario):
    try:
        usuario.valor = perform_calculation(usuario.engagement_metrics)
    except KeyError:
        print('Incorrect values provided to our calculation function')
        raise #para levantar el error :) , es importante  aveces levantar los errores y no solo hacer un print y permitir el programa seguir sin problemas, el raise debe ir dentro del Except, de lo contrario no sabrá que error levantar
    else: #este corre siempre y cuando no se levante el except, pero un finally corre siempre
        send_engagement_notification(usuario)
    return usuario.valor

def perform_calculation(metrics):
    return metrics['click']*8 + metrics['hits']*2

def send_engagement_notification(user):
    print(f'Notification sent to {user}')

usuario = User('santi', { 'clicks':8, 'hits':2 })
metricas = get_user_score(usuario)