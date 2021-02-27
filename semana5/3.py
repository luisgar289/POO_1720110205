import requests

# This function will pass your text to the machine learning model
# and return the top result with the highest confidence
def classify(text):
    key = "9f2eea10-7854-11eb-bc49-69c2fdecb79d9d87b85e-5cce-49a3-9794-da654b48cd6a"
    url = "https://machinelearningforkids.co.uk/api/scratch/"+ key + "/classify"

    response = requests.get(url, params={ "data" : text })

    if response.ok:
        responseData = response.json()
        topMatch = responseData[0]
        return topMatch
    else:
        response.raise_for_status()


while True:

    texto =  input("Hazme una pregunta sobre matematicas, historia, fisica o biologia: ")
    demo = classify(texto)

    label = demo["class_name"]
    confidence = demo["confidence"]


    if label == "Matematicas":
        print("Tu pregunta es de Matematicas")
        print ("Con %d%% de seguridad te lo digo" % (confidence))
    else:
        if label == "Historia":
            print("Tu pregunta es de Historia")
            print ("Con %d%% de seguridad te lo digo" % (confidence))
        else:
            if label == "Fisica":
                print("Tu pregunta es de fisica")
                print ("Con %d%% de seguridad te lo digo" % (confidence))
            else:
                if label == "Biologia":
                    print("Tu pregunta es de Biologia")
                    print ("Con %d%% de seguridad te lo digo" % (confidence))