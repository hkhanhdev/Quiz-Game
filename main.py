import GetData
import Game
game = Game.Game()
game.game_init()

json_file_path = 'questions_data.json'
api_url = 'https://opentdb.com/api.php'
# Fetch questions from the API
questions_data = GetData.fetch_questions_from_apis(api_url,params=game.params)
# Save questions to a JSON file
GetData.save_questions_to_storage(questions_data, json_file_path)
contents = GetData.fetch_questions_from_storage(json_file_path)
game.load_questions(contents['results'])

game.display_question_and_processing(game.questions)






