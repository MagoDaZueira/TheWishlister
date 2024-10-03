import maritalk
from dotenv import load_dotenv
import Metacritic
from API.Keys import Keys


def maritalk_review(game_name):
    game_info = Metacritic.retrieve_info(game_name)

    if game_info == 0:
        return_text = "O jogo não existe, ainda não foi lançado, ou houve um possível erro de digitação"
        return return_text
    

    reviews_text = ""

    amount = min(len(game_info["Reviews"]), 4)

    for i in range(amount): 
        current_review = ["------ Review " + str(i+1) + " ------\n\n"
            "Crítico: " + game_info["Reviews"][i]["Name"] + "\n\n"
            "Pontuação: " + game_info["Reviews"][i]["Score"] + "\n\n"
            "" + game_info["Reviews"][i]["Summary"] + "\n\n"
            "Link: " + game_info["Reviews"][i]["Link"] + "\n\n"]
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
        key= Keys.getMaritacaKey(),
        model="sabia-3"
    )

    response = model.generate(prompt["Dados"], max_tokens=1000)
    answer = response["answer"]

    return_text = modelo["Dados"] + "-------------------\n\n" + answer

    return return_text


# print(maritalk_review("Hollow Knight"))  