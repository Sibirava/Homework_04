#dinosaur's weight calculator
dinosaur_weight = input("Please input the dinosaur weight in gramm: ")
dinosaur_weight = float (dinosaur_weight)
kilotone = round(dinosaur_weight * 0.000000001, 2)
tone = round(dinosaur_weight * 0.000001, 2)
centner = round(dinosaur_weight * 0.00001, 2)
kilogramm = round(dinosaur_weight * 0.001,2)
print("The dinosaur's weight {} gramm is \n {} kilotones, \n {} tones, \n {} centners, \n {} kilogrammes"
      .format(dinosaur_weight, kilotone, tone, centner,kilogramm) )

