meme_dict = {
  "CRINGE": "Garip ya da utandırıcı bir şey",
  "LOL": "Komik bir şeye verilen cevap",
  "DM":"doğrudan mesaj anlamına geliyor ve sosyal medyada özel mesaj göndermek için kullanılan bir araç.",
  "POV":"bakış açısı anlamına gelir.",
  "ROFL" : "bir şakaya karşılık cevap",
  "SHEESH" : "onaylamamak",
  "CREEPY" : "korkunç",
  "AGGRO" : "agresifleşmek/sinirlenmek"
            }


word = input("Anlamadığınız bir kelime yazın (hepsini büyük harflerle yazın!): ")
if word in meme_dict.keys():
    print(meme_dict[word])
  
else:    
    print("Sözlüğünde böyle bir kelime yok!")
    
