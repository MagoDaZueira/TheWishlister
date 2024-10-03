import maritalk
from dotenv import load_dotenv
import Metacritic
from API.Keys import Keys


def maritalk_review(game_name):
    game_info = Metacritic.retrieve_info(game_name)

    if game_info == 0:
        return_text = "O jogo não existe, ainda não foi lançado, ou houve um possível erro de digitação"
        return return_text
    
    reviews = game_info["Reviews"]
    reviews_text = ""
    
    amount = min(len(reviews), 4)

    i = 0
    j = len(reviews)-1

    chosen_reviews = []
    for k in range(amount):
        if k % 2 == 0:
            chosen_reviews.append(reviews[i])
            i += 1
        else:
            chosen_reviews.append(reviews[j])
            j -= 1

    i = 1
    for rev in chosen_reviews: 
        current_review = ["------ Review " + str(i) + " ------\n\n"
            "Crítico: " + rev["Name"] + "\n\n"
            "Pontuação: " + rev["Score"] + "\n\n"
            "" + rev["Summary"] + "\n\n"
            "Link: " + rev["Link"] + "\n\n"]
        reviews_text += current_review[0]
        i += 1

    modelo = { 'Dados':
         "Nome do jogo: " + game_info['Name'] + "\n"

         "Data de lançamento: " + str(game_info['Date']['Day']) + "/" + str(game_info['Date']['Month']) + "/" + str(game_info['Date']['Year']) + "\n"

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

    message_list = [modelo["Dados"], answer]

    return message_list