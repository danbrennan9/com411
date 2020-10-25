def run():
  def sum_weights (beeps_weight, bops_weight):
    sum_weights = beeps_weight + bops_weight
    print("The answer is {}".format(sum_weights))

  def calc_avg_weight (beeps_weight, bops_weight):
    avg_weight = (beeps_weight + bops_weight) / 2
    print("The answer is {}".format(avg_weight))

  def runinner():
    
    print("Please enter beeps weights.")
    beeps_weight = float(input())
    
    print("Please enter bops weights.")
    bops_weight = float(input())

    print("Would you like the sum, or average?")
    answer = input()

    if answer == "sum":
      sum_weights(beeps_weight, bops_weight)
      

    if answer == "average":
      calc_avg_weight(beeps_weight, bops_weight)

  runinner()   


