import maritalk
import os
from dotenv import load_dotenv
import Metacritic
from WishlistManager import date_passed



def maritalk_review(game_name):
    game_info = Metacritic.retrieve_info(game_name)

    if game_info == 0:
        return_text = "O jogo não existe, ainda não foi lançado, ou houve um possível erro de digitação"
        return return_text
    

    reviews_text = ""

    for i in range(len(game_info["Reviews"])): 
        current_review = ["Review " + str(i+1) + ":" + "\n\n"
            "   Nome do crítico: " + game_info["Reviews"][i]["Name"] + "\n\n"
            "   Pontuação dada: " + game_info["Reviews"][i]["Score"] + "\n\n"
            "   Resumo da review: " + game_info["Reviews"][i]["Summary"] + "\n\n"
            "   Link para a review: " + game_info["Reviews"][i]["Link"] + "\n\n"]
        reviews_text += current_review[0]

    modelo = { 'Dados':
         "Nome do jogo: " + game_info['Name'] + "\n"

         "Data de lançamento: " + "Dia " + str(game_info['Date']['Day']) + "/" + str(game_info['Date']['Month']) + "/" + str(game_info['Date']['Year']) + "\n"

         "Nota no Metacritic: " + game_info['Score'] + "\n\n"

         + reviews_text
    }

    prompt = { "Dados":
        modelo["Dados"] + 
        "Com o conjunto de dados passados, você, em linguagem natural de português brasileiro, deve escrever uma resenha, condensando os resumos dos críticos em um único texto que leva em conta alguns dos elogios ou críticas ao jogo, de modo a servir como uma ferramenta útil para um usuário decidir se deve comprar ou não este jogo"

        }
    
    model = maritalk.MariTalk(
        key= os.getenv('MARITACA_API_KEY'), #Cole a chave aqui Ex: '100088...'
        model="sabia-3"  # No momento, suportamos os modelos sabia-3, sabia-2-medium e sabia-2-small
    )

    response = model.generate(prompt["Dados"], max_tokens=1000)
    answer = response["answer"]

    return_text = modelo["Dados"] + answer

    return return_text


print(maritalk_review("Hollow Knight"))  