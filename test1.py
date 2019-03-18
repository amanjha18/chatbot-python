from flask import Flask, jsonify,request,abort
import random,json
import pprint


task = Flask(__name__)
with open("data/challenges.json","r") as file:
    all_challenges = file.read()
    all_challenges=json.loads(all_challenges)
    # pprint.pprint(all_challenges)
    # pprint.pprint(type(all_challenges))


#getting all the chaallanges
@task.route("/all_challenges",methods = ["GET"])
def get_all_challenges():
    return jsonify(all_challenges)

# getting a challenge by its # ID
@task.route("/all_challenges/<int:challenge_id>",methods = ["GET"])
def get_a_challenge(challenge_id):
    single =[i for i in all_challenges if i["id"] == challenge_id]
    if len(single)== 0:
        abort(600)
    return jsonify(single[0])   

@task.route("/all_challenges/random",methods = ["GET"])
def get_random_challenge():
    string = random.choice(all_challenges)

    return jsonify(string["challenge"])

@task.route("/all_challenges/random/<level>",methods = ["GET"])
def get_by_level(level):
    by_level = [data for data in all_challenges if data["level"]==level]
    string = random.choice(by_level)
    return jsonify({"challenge":string["challenge"]})





if __name__=='__main__':
    task.run(debug= True,port=50000)