# coding: utf-8

import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import datetime


def conectarFirebase():
    cred = credentials.Certificate(
        'spider/sincere-charmer-137218-firebase-adminsdk-t7g8n-1a5497bdad.json')
    firebase_admin.initialize_app(cred)
    return firestore.client()


def buscarUltimasTemperaturas(login, quantidade=50):
    db = conectarFirebase()

    cams = db.collection(u'chaturbate')
    query = cams.where(
        u'Login', u'==', login).order_by(
        u'DataHora', direction=firestore.Query.DESCENDING).limit(quantidade)
    results = query.stream()
    return formataResposta(results)


def formataResposta(resposta):
    lista = list()
    for post in resposta:
        # print(u'{} => {}'.format(post.id, post.to_dict()))
        cams = post.to_dict()
        lista.append((cams['DataHora'], cams['Login']))
        # print(temp['datahora'])
    return lista


if __name__ == "__main__":
    login = input("Digite o login: ")
    quantidade = int(input("Quantidade: "))
    print(buscarUltimasTemperaturas(login, quantidade))
