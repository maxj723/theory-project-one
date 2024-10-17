import argparse;
import random;
from datetime import datetime
import textwrap;

def run(n):
  # Handle arguments
  
  # parser = argparse.ArgumentParser(
  #   prog='knapsackTestCaseGen',
  #   formatter_class=argparse.RawDescriptionHelpFormatter,
  #   description='Creates a given number each of small, medium, and large test cases for the knapsack problem.',
  #   epilog=textwrap.dedent('''
  #       The range for total value, number of coins, and coin size can be configured within the code.
  #       The cases are in format "casetype, totalvalue, coin1value, coin2value, coin3value,...'''))
  
  # parser.add_argument("--file", "-f", required=True, type=argparse.FileType('w'),
  #                     help="File to print test cases to (Will overwrite data).")
  # parser.add_argument("--size", "-s", required=True, type=int,
  #                     help="Number of test cases to generate.")
  
  # args = parser.parse_args()

  # # If something went wrong and the file cannot be opened, exit with error
  # if (not args.file):
  #   print("Error opening file.")
  #   return
  

  
  # Otherwise, print test cases to file

  # Set the total value range for the small, medium, and large test cases
  # Format: [[easy min val, easy max val], [med min, med max], [large min, large max]]
  testcaseTotalValueRange = [[0, 100], [101, 300], [301, 600]]
  # convert float values to ints
  testcaseTotalValueRange = [[int(x[0]), int(x[1])] for x in testcaseTotalValueRange]
  
  # Set the maximum coin value for the small, medium, and large test cases
  # Default is [25, 25, 25] to make them all 25 cents, but could be changed
  testcaseMaxCoinValue = [25, 25, 25]

  # Set the number of coin values to generate (default is 4)
  numCoins = n

  # Set the case types
  testcaseTypes = ["Small", "Medium", "Large"]

  # Set randomization seed
  filename = f'test{n}.txt'
  with open(filename, 'w') as fp:
    random.seed(datetime.now().timestamp())
    for testSize, vals in enumerate(testcaseTotalValueRange):
      
      for _testcase in range(50):

        total_value = random.randint(testcaseTotalValueRange[testSize][0], 
                                     testcaseTotalValueRange[testSize][1])
        
        available_coins = list(range(2, 25 + 1))
        coins = [random.choice(available_coins) for _ in range(numCoins)]

        fp.write(f"{testcaseTypes[testSize]}")
        fp.write(f", {total_value}")
        for coin in coins:
          fp.write(f", {coin}")
        fp.write("\n")

    # Close the file once we are done


def main():
  for i in range(1, 23):
    run(i)

if __name__ == '__main__':
  main()